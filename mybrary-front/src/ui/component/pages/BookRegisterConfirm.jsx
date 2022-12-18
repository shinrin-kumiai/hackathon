import Box from "@mui/material/Box";
import {Fab, Grid} from "@mui/material";
import * as React from "react";
import theme from "../../../theme.jsx";
import Header from "../chunks/Header.jsx";
import BookInfo from "../chunks/BookInfo.jsx";
import Typography from "@mui/material/Typography";
import {useEffect, useState} from "react";
import {useSelector} from "react-redux";
import {baseUrl} from "../../../infrastructure/apiConfig.js";
import {useParams} from "react-router-dom";
import axios from "axios";


function AddIcon() {
    return null;
}

const BookRegisterConfirm = (props) => {

    const params = useParams()

    const imagePath = baseUrl + '/assets/thumbnails/' + params.isbn

    const [book, setBook] = useState({})

    const token = sessionStorage.getItem('token')

    useEffect(() => {
        axios.get('http://localhost:8000/user/books/' + params.id + '?token=' + token).then((response) => {setBook(response.data)}).catch((err) => {
            if (err.response.status === 401 ){
                window.location.href='https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN&client_id=ac29ed4e-39b1-4632-b6fd-ff5867d75b66&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A5173&scope=openid&response_type=id_token&prompt=login'
            } else {
                window.location.href='/'
            }
        })
    }, [])

    console.log(useSelector(state => state.bookRegister))

    return (
        <div>
            <Header theme={theme}/>
            <Box>
                <Grid container direction='column' justifyContent='flex-start' alignContent='space-evenly'>
                    <Grid item sx={{padding: 1}}>
                        <Typography>
                            こちらの本が登録されました
                        </Typography>
                    </Grid>
                    <Grid item sx={{padding: 1}}>
                        <BookInfo value={book} width={props.windowWidth} height={props.windowHeight} imagePath={imagePath}/>
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
                                <Fab variant="extended" color="secondary" href='/book/register'>
                                    <AddIcon />
                                    さらに登録
                                </Fab>
                            </Grid>
                        </Grid>
                    </Grid>

                </Grid>
            </Box>
        </div>
    )
}


export default BookRegisterConfirm
