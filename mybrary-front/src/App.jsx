import {useLayoutEffect, useState} from 'react'
import Top from "./ui/component/pages/Top.jsx";
import AddBook from "./ui/component/pages/AddBook.jsx";
import BookRegisterConfirm from "./ui/component/pages/BookRegisterConfirm.jsx";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import {Provider} from "react-redux";
import store from "./store/index.js";
import BookDetail from "./ui/component/pages/BookDetail.jsx";
import AddCommunity from "./ui/component/pages/AddCommunity.jsx";
import CommunityShelf from "./ui/component/pages/CommunityShelf.jsx";
import CommunityConfig from "./ui/component/pages/CommunityConfig.jsx";
import {CookiesProvider, useCookies} from "react-cookie";
import LogInRedirect from "./ui/component/pages/LogInRedirect.jsx";
import axios from "axios";
import LogOuted from "./ui/component/pages/LogOuted.jsx";
import Typography from "@mui/material/Typography";


const windowSize = () => {
    const [size, setSize] = useState([0, 0]);
    useLayoutEffect(() => {
        const updateSize = () => {
            setSize([window.innerWidth, window.innerHeight]);
        };

        window.addEventListener('resize', updateSize);
        updateSize();

        return () => window.removeEventListener('resize', updateSize);
    }, []);
    return size
}

{/*<Top windowWidth={width} windowHeight={height}/>*/}
{/*<AddBook windowWidth={width} windowHeight={height}></AddBook>*/}

axios.interceptors.response.use(
    (response) => response,
    (error) => {
        /* 401 Unauthorized */
        if (error.response?.status === 401) {
            window.location.href='https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN&client_id=ac29ed4e-39b1-4632-b6fd-ff5867d75b66&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A5173&scope=openid&response_type=id_token&prompt=login'
        }
        /* AxiosError */
        if (error.isAxiosError && error.response?.data?.errors) {
            const errorMessage = error.response.data.errors.messages.join('\n');

            return (<Typography>
                {errorMessage}
            </Typography>)
        }

        /* 例外 */
    }
)



function App() {
    const apiUrl = 'http://localhost:8000'

    const [cookies, setCookie, removeCookie] = useCookies(["tkn"]);

    axios.interceptors.request.use(
        // allowedOriginと通信するときにトークンを付与するようにする設定
        config => {
            const { origin } = new URL(config.url);
            const allowedOrigins = [apiUrl];
            const token = (cookies.tkn);
            if (allowedOrigins.includes(origin)) {
                config.headers.authorization = `Bearer ${token}`;
            }
            return config;
        },
        error => {
            return Promise.reject(error);
        }
    );
    const [width, height] = windowSize()
    return (
        <CookiesProvider>
            <BrowserRouter>
                <Routes>
                    <Route index element={<Top/>}/>
                    <Route path={"/book/register/"} element={<AddBook windowWidth={width} windowHeight={height}/>}/>
                    <Route path={"/book/register-confirm/:isbn"} element={<BookRegisterConfirm windowWidth={width} windowHeight={height}/>}/>
                    <Route path={"/book/detail/:id"} element={<BookDetail windowWidth={width} windowHeight={height}/>}/>
                    <Route path={"/community/new"} element={<AddCommunity windowWidth={width} windowHeight={height}/>}/>
                    <Route path={"/community/:communityID/books"} element={<CommunityShelf windowWidth={width} windowHeight={height}/>}/>
                    <Route path={"/community/:communityID/config"} element={<CommunityConfig windowWidth={width} windowHeight={height}/>}/>
                    <Route path={"/login/redirect"} element={<LogInRedirect/>}/>
                    <Route path={"/bye-bye"} element={<LogOuted/>}/>
                </Routes>
            </BrowserRouter>
        </CookiesProvider>
        )
}

export default App
