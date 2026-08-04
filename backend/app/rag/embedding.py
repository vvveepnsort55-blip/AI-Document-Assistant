from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(

            "all-MiniLM-L6-v2"

        )


    def embed_documents(

        self,

        chunks: list[str]

    ):

        return self.model.encode(

            chunks,

            convert_to_numpy=True

        )


    def embed_query(

        self,

        question: str

    ):

        return self.model.encode(

            question,

            convert_to_numpy=True

        )
