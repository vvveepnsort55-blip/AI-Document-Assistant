from database import SessionLocal
from models import Document

from rag.processor import TextProcessor
from rag.embeddings import EmbeddingService
from rag.vector_store import VectorStore



class DocumentService:


    def __init__(self):

        self.db = SessionLocal()

        self.processor = TextProcessor()

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()



    def save_document(
        self,
        user_id,
        filename,
        filepath,
        extracted_pages
    ):


        document = Document(

            user_id=user_id,

            filename=filename,

            filepath=filepath,

            extracted_text=str(extracted_pages)

        )


        self.db.add(
            document
        )


        self.db.commit()


        self.db.refresh(
            document
        )



        chunk_index = 0



        for page in extracted_pages:


            page_number = page["page"]

            page_text = page["text"]



            chunks = self.processor.split_text(
                page_text
            )



            for chunk in chunks:


                embedding = (
                    self.embedding_service
                    .create_embedding(chunk)
                )



                self.vector_store.add_document(

                    chunk_id=f"{document.id}_{chunk_index}",

                    text=chunk,

                    embedding=embedding,

                    document_id=document.id,

                    metadata={

                        "page": page_number,

                        "chunk_index": chunk_index

                    }

                )


                chunk_index += 1



        return document





    def get_document(
        self,
        document_id
    ):

        return (

            self.db.query(Document)

            .filter(

                Document.id == document_id

            )

            .first()

        )





    def delete_document(
        self,
        document_id
    ):


        self.vector_store.delete_document(
            document_id
        )



        document = (

            self.db.query(Document)

            .filter(

                Document.id == document_id

            )

            .first()

        )



        if document:


            self.db.delete(
                document
            )


            self.db.commit()



        return True
