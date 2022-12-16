import {useCookies} from "react-cookie";
import {useEffect} from "react";


const LogInRedirect = () => {
    const [cookies, setCookie, removeCookie] = useCookies(["tkn"]);
    useEffect(() => {
        setCookie("tkn", location.hash)
        window.location.href='/'
    })
    return (
        <div>

        </div>
    )
}

export default LogInRedirect