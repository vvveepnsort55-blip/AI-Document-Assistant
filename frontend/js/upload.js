async function uploadPDF(){

    const fileInput =
    document.getElementById("pdf-file");


    const file =
    fileInput.files[0];


    if(!file){

        alert("Please select a PDF file");

        return;

    }



    const formData =
    new FormData();


    formData.append(
        "file",
        file
    );



    const token =
    localStorage.getItem("token");



    const response =
    await fetch(
        "http://127.0.0.1:8000/documents/upload",
        {

            method:"POST",

            headers:{

                "Authorization":
                "Bearer " + token

            },

            body:formData

        }
    );



    const data =
    await response.json();



    console.log(data);



    if(response.ok){

        alert(
            "PDF uploaded successfully"
        );

        console.log(
            "Document ID:",
            data.document_id
        );

    }

    else{

        alert(
            data.detail || "Upload failed"
        );

    }

}