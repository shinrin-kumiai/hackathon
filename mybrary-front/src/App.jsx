import {useLayoutEffect, useState} from 'react'
import Top from "./ui/component/pages/Top.jsx";
import AddBook from "./ui/component/pages/AddBook.jsx";
import BookRegisterConfirm from "./ui/component/pages/BookRegisterConfirm.jsx";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import {Provider} from "react-redux";
import store from "./store/index.js";
import BookDetail from "./ui/component/pages/BookDetail.jsx";
import CreateCommunity from "./ui/component/pages/CreateCommunity.jsx";
import CommunityShelf from "./ui/component/pages/CommunityShelf.jsx";
import CommunityConfig from "./ui/component/pages/CommunityConfig.jsx";
import {CookiesProvider, useCookies} from "react-cookie";
// import {handleLogin} from "./ui/component/pages/LogInRedirect.jsx";
import axios from "axios";
import LogOuted from "./ui/component/pages/LogOuted.jsx";
import Typography from "@mui/material/Typography";
import {CssBaseline, ThemeProvider} from "@mui/material";
import theme from "./theme.jsx";
import NotFound from "./ui/component/pages/NotFound.jsx";
// import { ProfileData } from "./components/ProfileData";
// import { callMsGraph } from "./graph";
import AddUsrtoCommunity from "./ui/component/pages/AddUsrtoCommunity.jsx";
import Welcome from "./ui/component/pages/Welcome.jsx";


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
function ProfileContent() {
    const { instance, accounts, inProgress } = useMsal();
    const [accessToken, setAccessToken] = useState(null);

    const name = accounts[0] && accounts[0].name;

    function RequestAccessToken() {
        const request = {
            ...loginRequest,
            account: accounts[0]
        };

        // Silently acquires an access token which is then attached to a request for Microsoft Graph data
        instance.acquireTokenSilent(request).then((response) => {
            setAccessToken(response.accessToken);
        }).catch((e) => {
            instance.acquireTokenPopup(request).then((response) => {
                setAccessToken(response.accessToken);
            });
        });
    }

    return (
        <>
            <h5 className="card-title">Welcome {name}</h5>
            {accessToken ?
                <p>Access Token Acquired!</p>
                :
                <Button variant="secondary" onClick={RequestAccessToken}>Request Access Token</Button>
            }
        </>
    );
};



axios.interceptors.response.use(
    (response) => response,
    (error) => {
        /* 401 Unauthorized */
        if (error.response?.status === 401) {
            console.log('a')
        }
        /* AxiosError */
        if (error.isAxiosError && error.response?.data?.errors) {
            const errorMessage = error.response.data.errors.messages.join('\n');
            isbn
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
            <ThemeProvider theme={theme}>
                <CssBaseline>
                    <BrowserRouter>
                        <Routes>
                            <Route index element={<Top/>}/>
                            <Route path={"/book/register/"} element={<AddBook windowWidth={width} windowHeight={height}/>}/>
                            <Route path={"/book/register-confirm/:isbn/:id"} element={<BookRegisterConfirm windowWidth={width} windowHeight={height}/>}/>
                            <Route path={"/book/detail/:id"} element={<BookDetail windowWidth={width} windowHeight={height}/>}/>
                            <Route path={"/community/new"} element={<CreateCommunity windowWidth={width} windowHeight={height}/>}/>
                            <Route path={"/community/:communityID/books"} element={<CommunityShelf windowWidth={width} windowHeight={height}/>}/>
                            <Route path={"/community/:communityID/config"} element={<CommunityConfig windowWidth={width} windowHeight={height}/>}/>
                            {/*<Route path={"/login/redirect"} element={<LogInRedirect/>}/>*/}
                            <Route path={"/bye-bye"} element={<LogOuted/>}/>
                            <Route path={"/404-not-found"} element={<NotFound/>}/>
                            <Route path={"/community/:communityID/add-user"} element={<AddUsrtoCommunity windowWidth={width} windowHeight={height}/>}/>
                            <Route path={"/welcome"} element={<Welcome/>}/>
                        </Routes>
                    </BrowserRouter>
                </CssBaseline>

            </ThemeProvider>

        </CookiesProvider>
        )
}

export default App
