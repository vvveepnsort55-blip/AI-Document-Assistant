import chromadb



class VectorStore:


    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )


        self.collection = (
            self.client.get_or_create_collection(
                name="documents"
            )
        )



    def add_document(
        self,
        chunk_id: str,
        text: str,
        embedding: list,
        document_id: int,
        metadata: dict = None
    ):

        try:


            final_metadata = {

                "document_id": str(document_id)

            }


            if metadata:

                final_metadata.update(
                    metadata
                )



            self.collection.add(

                ids=[chunk_id],

                documents=[text],

                embeddings=[embedding],

                metadatas=[final_metadata]

            )



        except Exception as e:


            print(
                f"Vector add error: {e}"
            )





    def search(
        self,
        embedding: list,
        document_id: int,
        limit: int = 5
    ):


        try:


            results = self.collection.query(

                query_embeddings=[embedding],

                n_results=limit,

                where={

                    "document_id": str(document_id)

                },

                include=[

                    "documents",

                    "metadatas",

                    "distances"

                ]

            )



            documents = results.get(
                "documents",
                []
            )


            metadatas = results.get(
                "metadatas",
                []
            )


            distances = results.get(
                "distances",
                []
            )



            if not documents:

                return []



            response = []



            for i, doc in enumerate(documents[0]):


                metadata = {}


                if metadatas:

                    metadata = metadatas[0][i]



                response.append(

                    {

                        "text": doc,


                        "score":
                        (
                            distances[0][i]
                            if distances
                            else None
                        ),


                        "page":
                        metadata.get(
                            "page"
                        ),


                        "chunk_index":
                        metadata.get(
                            "chunk_index"
                        )

                    }

                )



            return response



        except Exception as e:


            print(
                f"Vector search error: {e}"
            )


            return []





    def count_documents(self):

        return self.collection.count()





    def delete_document(
        self,
        document_id: int
    ):


        try:


            self.collection.delete(

                where={

                    "document_id":
                    str(document_id)

                }

            )



        except Exception as e:


            print(
                f"Vector delete error: {e}"
            )
