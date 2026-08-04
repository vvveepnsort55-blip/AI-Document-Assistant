from pypdf import PdfReader



def extract_text_from_pdf(file_path):

    pages = []


    reader = PdfReader(
        file_path
    )


    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        page_text = page.extract_text()


        if page_text:

            pages.append(

                {
                    "page": page_number,

                    "text": page_text.replace(
                        "\x00",
                        ""
                    )

                }

            )


    return pages
