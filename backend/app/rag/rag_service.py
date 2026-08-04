from rag.embeddings import EmbeddingService
from rag.vector_store import VectorStore



class RAGService:


    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()



    def search_context(
        self,
        question: str,
        document_id: int,
        top_k: int = 5
    ):

        try:

            # Create embedding for user question
            question_embedding = (
                self.embedding_service
                .create_embedding(question)
            )


            # Search relevant chunks
            chunks = self.vector_store.search(
                question_embedding,
                document_id,
                top_k
            )


            if not chunks:

                return (
                    "No relevant information "
                    "was found in this document."
                )



            cleaned_chunks = []



            for chunk in chunks:


                # New VectorStore response format
                if isinstance(chunk, dict):

                    text = chunk.get(
                        "text"
                    )

                    if text:

                        cleaned_chunks.append(
                            text.strip()
                        )



                # Old response format support
                elif isinstance(chunk, str):

                    cleaned_chunks.append(
                        chunk.strip()
                    )



            if not cleaned_chunks:

                return (
                    "No usable information "
                    "was found in this document."
                )



            context = "\n\n".join(
                cleaned_chunks
            )


            return context



        except Exception as e:


            print(
                f"RAG Search Error: {e}"
            )


            return ""
