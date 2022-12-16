import Box from "@mui/material/Box";
import {Fab, Grid} from "@mui/material";
import * as React from "react";
import theme from "../../../theme.jsx";
import Header from "../chunks/Header.jsx";
import BookInfo from "../chunks/BookInfo.jsx";
import axios from "axios";
import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import {baseUrl} from "../../../infrastructure/apiConfig.js";


function AddIcon() {
    return null;
}

const BookDetail = (props) => {

    const params = useParams()

    const id = params.id

    const [response, setResponse] = useState({})

    useEffect(() => {axios.get(baseUrl + '/user/books/' + id).then(
        (response) => (setResponse(response.data))
    )}, [])

    const imagePath = baseUrl + '/assets/thumbnails/' + response.isbn

    const deleteRelation = () => {
        axios.delete(baseUrl + '/user/books/' + id).then((response) => (
            window.location.href = '/'
        ))
    }



    const ButtonConfig = (response) => {
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
                        {<ButtonConfig response={response}/>}
                    </Grid>
                    <Grid item sx={{padding: 1}}>
                        <BookInfo value={response} width={props.windowWidth} height={props.windowHeight} imagePath={imagePath}/>
                    </Grid>
                    <Grid item>
                        <Grid container direction='row' justifyContent='space-evenly' alignContent='center'>
                            <Grid item>
                                <Fab variant="extended" color="primary" href='/'>
                                    MyShelf
                                </Fab>
                            </Grid>
                            <Grid item>
                                <Fab variant="extended" color="primary" onClick={() => deleteRelation()}>
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
