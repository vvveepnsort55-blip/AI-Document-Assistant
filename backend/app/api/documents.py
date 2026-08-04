from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from pydantic import BaseModel

from api.schemas import DocumentResponse

from database import SessionLocal, get_db


# Models
from models.document import Document
from models.chat import ChatMessage
from models.user import User


# Services
from services.document_service import DocumentService


# Utils
from utils import extract_text_from_pdf


# AI
from ai import AIService


# RAG
from rag.rag_service import RAGService


# Security
from core.security import get_current_user


import os
import uuid



ai = AIService()

rag = RAGService()



router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)



UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)



# =========================
# Upload PDF
# =========================

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):

    if file.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )


    contents = await file.read()


    max_size = 10 * 1024 * 1024


    if len(contents) > max_size:

        raise HTTPException(
            status_code=400,
            detail="File size must be less than 10MB"
        )


    safe_filename = (
        str(uuid.uuid4())
        +
        ".pdf"
    )


    file_path = os.path.join(
        UPLOAD_FOLDER,
        safe_filename
    )


    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(contents)



    pages = extract_text_from_pdf(
        file_path
    )



    document_service = DocumentService()


    document = document_service.save_document(
        user_id=current_user.id,
        filename=file.filename,
        filepath=file_path,
        extracted_pages=pages
    )


    return {

        "message": "Uploaded successfully",

        "document_id": document.id,

        "filename": document.filename

    }




# =========================
# Chat Request
# =========================

class ChatRequest(BaseModel):

    question: str

    document_id: int




# =========================
# Chat With PDF
# =========================

@router.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):

    db = SessionLocal()


    document = db.query(
        Document
    ).filter(

        Document.id == request.document_id,

        Document.user_id == current_user.id

    ).first()



    if not document:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )



    context = rag.search_context(

        request.question,

        document.id

    )



    history_messages = db.query(
        ChatMessage
    ).filter(

        ChatMessage.document_id == document.id

    ).order_by(

        ChatMessage.id.desc()

    ).limit(5).all()



    history = []


    for msg in reversed(history_messages):

        history.append({

            "question": msg.question,

            "answer": msg.answer

        })



    answer = ai.ask(

        request.question,

        context,

        history

    )



    chat_message = ChatMessage(

        user_id=current_user.id,

        document_id=document.id,

        question=request.question,

        answer=answer

    )


    db.add(chat_message)

    db.commit()

    db.refresh(chat_message)


    db.close()



    return {

        "document": document.filename,

        "answer": answer,

        "chat_id": chat_message.id

    }





# =========================
# Get Documents
# =========================

@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    documents = (

        db.query(Document)

        .filter(
            Document.user_id == current_user.id
        )

        .all()

    )


    return documents





# =========================
# Get Single Document
# =========================

@router.get("/{document_id}")
def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user)
):

    db = SessionLocal()



    document = db.query(Document).filter(

        Document.id == document_id,

        Document.user_id == current_user.id

    ).first()



    db.close()



    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )



    return {

        "id": document.id,

        "filename": document.filename,

        "created_at": document.created_at

    }





# =========================
# Delete Document
# =========================

@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    current_user: User = Depends(get_current_user)
):

    db = SessionLocal()



    document = db.query(Document).filter(

        Document.id == document_id,

        Document.user_id == current_user.id

    ).first()



    if not document:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )



    if os.path.exists(document.filepath):

        os.remove(document.filepath)



    db.delete(document)

    db.commit()

    db.close()



    return {

        "message":

        "Document deleted successfully"

    }
