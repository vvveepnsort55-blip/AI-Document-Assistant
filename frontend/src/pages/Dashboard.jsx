import { useEffect, useState } from "react";

import api from "../api/axios";


function Dashboard(){


    const [documents, setDocuments] = useState([]);



    const loadDocuments = async ()=>{

        try{

            const response = await api.get(
                "/documents/"
            );


            setDocuments(
                response.data
            );


        }catch(error){

            console.log(error);

        }

    };



    useEffect(()=>{

        loadDocuments();

    },[]);



    return (

        <div>


            <h1>
                Dashboard
            </h1>



            <h2>
                My Documents
            </h2>



            {
                documents.map((doc)=>(

                    <div key={doc.id}>


                        <p>
                            {doc.filename}
                        </p>


                        <button>
                            Chat
                        </button>


                        <button>
                            Delete
                        </button>


                    </div>

                ))
            }



        </div>

    );

}


export default Dashboard;