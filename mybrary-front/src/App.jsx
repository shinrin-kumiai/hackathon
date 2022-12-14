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


function App() {
    const [width, height] = windowSize()
    return (
        <BrowserRouter>
            <Routes>
                <Route index element={<Top/>}/>
                <Route path={"/book/register/"} element={<AddBook windowWidth={width} windowHeight={height}/>}/>
                <Route path={"/book/register_confirm/:isbn"} element={<BookRegisterConfirm windowWidth={width} windowHeight={height}/>}/>
                <Route path={"/book/detail/:isbn"} element={<BookDetail windowWidth={width} windowHeight={height}/>}/>
                <Route path={"/community/new"} element={<AddCommunity windowWidth={width} windowHeight={height}/>}/>
                <Route path={"/community/:communityID/books"} element={<CommunityShelf windowWidth={width} windowHeight={height}/>}/>
            </Routes>
        </BrowserRouter>
        )
}

export default App
