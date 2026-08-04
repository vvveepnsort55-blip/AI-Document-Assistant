const API_URL = "http://127.0.0.1:8000";


function getToken(){

    return localStorage.getItem(
        "token"
    );

}



async function apiRequest(
    endpoint,
    options = {}
){

    const token = getToken();


    if(!options.headers){

        options.headers = {};

    }



    if(token){

        options.headers[
            "Authorization"
        ] = "Bearer " + token;

    }



    const response = await fetch(
        API_URL + endpoint,
        options
    );



    const data = await response.json();



    if(!response.ok){

        throw new Error(
            data.detail || "API Error"
        );

    }


    return data;

}