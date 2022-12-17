import { useMsal } from '@azure/msal-react';
import * as React from 'react';
import Header from "../chunks/Header.jsx";
import BookCards from "../chunks/BookCards.jsx";
import {Button, Fab, Grid} from "@mui/material";
import Box from "@mui/material/Box";
import theme from "../../../theme.jsx";
import axios from "axios";
import {useEffect, useState} from "react";
import SignInButton from "./LogInRedirect.jsx";
import {useCookies} from "react-cookie";
import AddIcon from '@mui/icons-material/Add';
import Typography from "@mui/material/Typography";
import MenuBookIcon from '@mui/icons-material/MenuBook';
// const books = [{title: 'mori', preDate: '2022/8/31', status: 'rental'}, {title: 'hayashi', preDate: '2022/12/31', status: 'rending'}, {title: 'tanaka', preDate: '2023/1/5', status: 'rental'}, {title: 'sonken', preDate: '2023/12/3', status: 'neutral'}]


const Top = (props) => {
    const [cookies, setCookie, removeCookie] = useCookies(["tkn"]);
    const [books, setBooks] = useState([])
    useEffect(() => {axios.get('http://localhost:8000/user/books?page=1&size=50',{ headers: { Authorization: "JWT " + cookies.tkn } }).then(
        (response) => setBooks(response.data.items)
    )}, [])

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
                            <Grid item>
                                <Fab variant='extended' color="primary" href='/book/register'>
                                    <AddIcon fontSize='small'/>
                                    <MenuBookIcon/>
                                </Fab>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
                <SignInButton></SignInButton>
            </Box>
        </div>
    )
}

export default Top
