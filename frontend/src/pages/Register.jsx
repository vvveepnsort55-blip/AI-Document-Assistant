import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/axios";

function Register() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");


    const handleRegister = async (e) => {

        e.preventDefault();

        try {

            await api.post("/auth/register", {

                username,

                email,

                password

            });

            alert("Registration successful");

            navigate("/login");

        } catch (error) {

            console.log(error);

            alert("Registration failed");

        }

    };


    return (

        <div>

            <h2>Register</h2>

            <form onSubmit={handleRegister}>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button type="submit">
                    Register
                </button>

            </form>

        </div>

    );

}

export default Register;