from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


# Models
from models.document import Document
from models.chat import ChatMessage


# Services
from services.document_service import DocumentService


# AI
from ai import AIService


# RAG
from rag.rag_service import RAGService



router = APIRouter(
    prefix="/documents",
    tags=["Chat"]
)



ai = AIService()

rag = RAGService()



class ChatRequest(BaseModel):

    question: str

    document_id: int





@router.post("/chat")
async def chat(
    request: ChatRequest
):

    document_service = DocumentService()


    try:


        document = (
            document_service.db.query(Document)
            .filter(
                Document.id == request.document_id
            )
            .first()
        )


        if not document:

            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )



        context = rag.search_context(
            request.question,
            request.document_id
        )



        if not context:

            answer = (
                "No relevant information "
                "was found in this document."
            )


        else:

            answer = ai.ask(
                request.question,
                context
            )



        chat_message = ChatMessage(

            document_id=document.id,

            question=request.question,

            answer=answer

        )


        document_service.db.add(
            chat_message
        )


        document_service.db.commit()


        document_service.db.refresh(
            chat_message
        )



        return {

            "document": document.filename,

            "answer": answer,

            "chat_id": chat_message.id

        }



    except Exception as e:


        document_service.db.rollback()


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )





@router.get("/{document_id}/history")
async def get_chat_history(
    document_id: int
):

    document_service = DocumentService()


    messages = (
        document_service.db.query(ChatMessage)
        .filter(
            ChatMessage.document_id == document_id
        )
        .all()
    )


    return [

        {
            "id": msg.id,
            "question": msg.question,
            "answer": msg.answer,
            "created_at": msg.created_at
        }

        for msg in messages

    ]
