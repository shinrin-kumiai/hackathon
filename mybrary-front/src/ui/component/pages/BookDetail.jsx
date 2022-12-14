import Box from "@mui/material/Box";
import {Fab, Grid} from "@mui/material";
import * as React from "react";
import theme from "../../../theme.jsx";
import Header from "../chunks/Header.jsx";
import BookInfo from "../chunks/BookInfo.jsx";
import Typography from "@mui/material/Typography";
import store from "../../../store/index.js";
import axios from "axios";
import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";


function AddIcon() {
    return null;
}

const BookDetail = (props) => {

    const params = useParams()

    console.log(params)

    const id = params.id

    const [response, setResponse] = useState(null)

    const value = {
        imageURL: "https://m.media-amazon.com/images/I/51WG47XKOkL._SX351_BO1,204,203,200_.jpg",
        isbn: 978134566,
        title: "python爆速fire",
        author: "kazuki moriyama",
        publisher: "sonken shobou",
        publish_date: "2022/08/31",
        state: "waitPermission"
    }
    // axios.get('http://localhost:8000/user/books/?isbn=9784798067278', {
    //     headers: {}}).then((response) => {setResponse(response)})
    // useEffect(() => {
    //     axios.get('http://localhost:8000/book/9784798067278', {
    //         headers: {}}).then((response) => {setResponse(response)})
    // }, [])

    const buttonConfig = (response) => {
        if (response.state === "waitPermission"){
            const config = {
                text: '貸出要望があります！'
            }
            return (
                <Grid container direction='row' justifyContent='space_evenly' alignContent='center'>
                    <Grid item>
                        <Grid item>
                            <Fab variant="extended" color="primary" href='/'>
                                <AddIcon />
                                {config.text}
                            </Fab>
                        </Grid>
                    </Grid>
                </Grid>
            )
        } else {
            return (
                <></>
            )
        }
    }

    return (
        <div>
            <Header theme={theme}/>
            <Box>
                <Grid container direction='column' justifyContent='flex-start' alignContent='space-evenly'>
                    <Grid item>
                        {() => {
                            buttonConfig(value)
                        }}
                    </Grid>
                    <Grid item sx={{padding: 1}}>
                        <BookInfo value={value} width={props.windowWidth} height={props.windowHeight} imagePath={response}/>
                    </Grid>
                    <Grid item>
                        <Grid container direction='row' justifyContent='space-evenly' alignContent='center'>
                            <Grid item>
                                <Fab variant="extended" color="primary" href='/'>
                                    <AddIcon />
                                    MyShelf
                                </Fab>
                            </Grid>
                            <Grid item>
                                <Fab variant="extended" color="primary" href='/'>
                                    <AddIcon />
                                    登録を解除
                                </Fab>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </Box>
        </div>
    )
}


export default BookDetail
