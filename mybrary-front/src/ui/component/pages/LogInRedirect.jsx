import React from "react";
import { useMsal } from "@azure/msal-react";
// import { loginRequest } from "../../../authConfig.js";
import Button from "react-bootstrap/Button";


/**
 * Renders a button which, when selected, will redirect the page to the login prompt
 */
const LogInRedirect = () => {
    const token = location.hash
    console.log(token)
    sessionStorage.setItem('token', token);
    window.location.href='/'
    return (
        <div>

        </div>
    )
}
export default LogInRedirect
