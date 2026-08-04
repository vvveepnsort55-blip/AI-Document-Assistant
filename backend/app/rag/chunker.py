from langchain.text_splitter import RecursiveCharacterTextSplitter



class DocumentChunker:


    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200,

            separators=[

                "\n\n",

                "\n",

                " ",

                ""

            ]

        )



    def split(
        self,
        text: str
    ):

        chunks = self.splitter.split_text(
            text
        )


        result = []


        for index, chunk in enumerate(chunks):

            result.append(

                {
                    "text": chunk,

                    "chunk_index": index

                }

            )


        return result
