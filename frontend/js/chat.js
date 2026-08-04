let currentDocumentId = null;



function openChat(documentId){


    currentDocumentId = documentId;



    document.getElementById(
        "chat-section"
    ).style.display = "block";



    document.getElementById(
        "messages"
    ).innerHTML = "";



}





async function sendMessage(){


    const token = localStorage.getItem("token");


    const questionInput =
    document.getElementById("question");


    const question =
    questionInput.value.trim();



    if(!question){

        return;

    }



    if(!currentDocumentId){

        alert(
            "Please select a document first"
        );

        return;

    }




    addMessage(
        question,
        "user"
    );



    questionInput.value = "";



    const loading =
    addMessage(
        "AI is thinking...",
        "ai"
    );





    try{


        const response = await fetch(

            "http://127.0.0.1:8000/documents/chat",

            {

                method:"POST",


                headers:{

                    "Content-Type":"application/json",

                    "Authorization":
                    "Bearer " + token

                },


                body:JSON.stringify({

                    question:question,

                    document_id:currentDocumentId

                })


            }

        );



        const data =
        await response.json();



        loading.remove();



        if(!response.ok){


            addMessage(

                data.detail ||
                "Something went wrong",

                "ai"

            );


            return;

        }



        addMessage(

            data.answer,

            "ai"

        );



    }


    catch(error){


        loading.remove();



        addMessage(

            "Server connection error",

            "ai"

        );


        console.log(error);


    }



}






function addMessage(text,type){


    const messages =
    document.getElementById(
        "messages"
    );



    const div =
    document.createElement(
        "div"
    );



    div.className = "message " + type;



    div.innerHTML = text;



    messages.appendChild(div);



    messages.scrollTop =
    messages.scrollHeight;



    return div;


}