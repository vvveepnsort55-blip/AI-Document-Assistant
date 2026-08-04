import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/axios";


function Login(){


    const navigate = useNavigate();


    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");



    const handleLogin = async (e)=>{

        e.preventDefault();


        try{


            const response = await api.post(
                "/auth/login",
                {
                    email,
                    password
                }
            );



            localStorage.setItem(
                "token",
                response.data.access_token
            );



            alert(
                "Login successful"
            );


            navigate(
                "/dashboard"
            );



        }catch(error){


            console.log(
                error
            );


            alert(
                "Login failed"
            );

        }

    };



    return (

        <div>


            <h2>
                Login
            </h2>



            <form onSubmit={handleLogin}>


                <input

                    type="email"

                    placeholder="Email"

                    value={email}

                    onChange={
                        (e)=>
                        setEmail(e.target.value)
                    }

                />



                <input

                    type="password"

                    placeholder="Password"

                    value={password}

                    onChange={
                        (e)=>
                        setPassword(e.target.value)
                    }

                />



                <button type="submit">

                    Login

                </button>



            </form>


        </div>

    );

}


export default Login;