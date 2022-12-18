import { useMsal } from '@azure/msal-react';
import * as React from 'react';
import Header from "../chunks/Header.jsx";
import BookCards from "../chunks/BookCards.jsx";
import {Button, Fab, Grid} from "@mui/material";
import Box from "@mui/material/Box";
import theme from "../../../theme.jsx";
import axios from "axios";
import {useEffect, useState} from "react";
import {useCookies} from "react-cookie";
import AddIcon from '@mui/icons-material/Add';
import Typography from "@mui/material/Typography";
import MenuBookIcon from '@mui/icons-material/MenuBook';
import {loginRequest} from "../../../authConfig"
import { myMSALObj, handleResponse } from '../../../authPopup.js';
// const books = [{title: 'mori', preDate: '2022/8/31', status: 'rental'}, {title: 'hayashi', preDate: '2022/12/31', status: 'rending'}, {title: 'tanaka', preDate: '2023/1/5', status: 'rental'}, {title: 'sonken', preDate: '2023/12/3', status: 'neutral'}]


const Top = (props) => {
    const signIn = () => {

        /**
         * You can pass a custom request object below. This will override the initial configuration. For more information, visit:
         * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/request-response-object.md#request
         */

        myMSALObj.loginRedirect(loginRequest)
            .then(handleResponse)
            .catch(error => {
                console.log(error);
            });
    }
    const token = sessionStorage.getItem('token')
    console.log(token)
    const addAuth = true
    const auth = 'visible'
    const [cookies, setCookie, removeCookie] = useCookies(["tkn"]);
    const [books, setBooks] = useState([])
    useEffect(() => {axios.get('http://localhost:8000/user/books?token=' + token + '&page=1&size=50',{ headers: { Authorization: "JWT " + cookies.tkn } }).then(
        (response) => setBooks(response.data.items)
    )}, [])
    const AuthFab = (props) => {
        if (props.auth) {
            return (
                <Fab variant="extended" color="primary" href='/book/register/'>
                    <AddIcon fontSize='small'/>
                    <MenuBookIcon/>
                </Fab>
            )} else {
            return(
                <Box sx={{width:0, height:0}}/>
            )
        }
    }

    return (
        <div>
            <Header theme={theme}/>
            <Box>
                <Grid container direction='column' justifyContent='flex-start' alignContent='space-evenly'>
                    <Grid item>
                        <Typography sx={{marginTop:5, marginLeft:3}}>
                            My Book Shelf
                        </Typography>
                    </Grid>
                    <Grid item>
                        <BookCards books={books} theme={theme}/>
                    </Grid>
                    <Grid item sx={{padding: 2}}>
                        <Grid container direction='row' justifyContent='flex-end' alignContent='flex-end'>
                            <Grid item visibility={auth}>
                                <AuthFab auth={addAuth}/>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
                <Button onClick={() => {signIn()}}>
                    signiniuooo
                </Button>
            </Box>
        </div>
    )
}

export default Top
