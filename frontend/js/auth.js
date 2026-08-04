async function login() {

    const email =
    document.getElementById("email").value;

    const password =
    document.getElementById("password").value;


    const response = await fetch(

        "http://127.0.0.1:8000/auth/login",

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                email: email,

                password: password

            })

        }

    );


    const data = await response.json();


    if (response.ok) {

        localStorage.setItem(
            "token",
            data.access_token
        );

        document.getElementById("username").innerHTML =
        email;

        document.getElementById(
            "login-box"
        ).style.display = "none";

        loadDocuments();

    }

    else {

        alert(data.detail);

    }

}


function logout() {

    localStorage.removeItem("token");

    location.reload();

}