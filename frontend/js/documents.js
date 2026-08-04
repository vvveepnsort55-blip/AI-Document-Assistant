async function loadDocuments(){


    const token = localStorage.getItem("token");


    const response = await fetch(

        "http://127.0.0.1:8000/documents/",

        {

            headers:{

                "Authorization":
                "Bearer " + token

            }

        }

    );



    const documents = await response.json();



    const list =
    document.getElementById(
        "documents-list"
    );



    list.innerHTML = "";



    documents.forEach(doc=>{


        const item =
        document.createElement("div");



        item.className = "document-card";



        item.innerHTML = `


            <div class="document-header">

                <span class="pdf-icon">
                    📄
                </span>


                <span class="document-name">
                    ${doc.filename}
                </span>

            </div>



            <div class="document-info">

                ID: ${doc.id}

            </div>



            <div class="document-actions">


                <button
                class="chat-btn"
                onclick="openChat(${doc.id})">

                    💬 Chat

                </button>



                <button
                class="delete-btn"
                onclick="deleteDocument(${doc.id})">

                    🗑 Delete

                </button>


            </div>


        `;



        list.appendChild(item);



    });



}





async function deleteDocument(documentId){


    const token =
    localStorage.getItem("token");



    const confirmDelete =
    confirm(
        "Delete this document?"
    );



    if(!confirmDelete)
        return;



    const response =
    await fetch(

        `http://127.0.0.1:8000/documents/${documentId}`,

        {

            method:"DELETE",

            headers:{

                "Authorization":
                "Bearer " + token

            }

        }

    );



    const data =
    await response.json();



    if(response.ok){


        alert(
            "Document deleted"
        );


        loadDocuments();


    }

    else{


        alert(
            data.detail
        );


    }



}