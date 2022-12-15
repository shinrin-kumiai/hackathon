import * as React from 'react';
import Header from "../chunks/Header.jsx";
import BookCards from "../chunks/BookCards.jsx";
import {Button, Grid} from "@mui/material";
import Box from "@mui/material/Box";
import theme from "../../../theme.jsx";
import axios from "axios";
import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";

// const books = [{title: 'mori', preDate: '2022/8/31', status: 'rental'}, {title: 'hayashi', preDate: '2022/12/31', status: 'rending'}, {title: 'tanaka', preDate: '2023/1/5', status: 'rental'}, {title: 'sonken', preDate: '2023/12/3', status: 'neutral'}]

const CommunityShelf = (props) => {
    const params = useParams()
    const [books, setBooks] = useState([])
    useEffect(() => {axios.get('http://localhost:8000/Community/'+ params.communityId +'books?page=1&size=50').then(
        (response) => setBooks(response.data.items)
    )}, [])

    return (
        <div>
            <Header theme={theme}/>
            <Box>
                <Grid container direction='column' justifyContent='flex-start' alignContent='space-evenly'>
                    <Grid item>
                        <BookCards books={books} theme={theme}/>
                    </Grid>
                    <Grid item sx={{padding: 2}}>
                        <Button href={'/book/register'}>
                            Add Book
                        </Button>
                    </Grid>
                </Grid>
            </Box>
        </div>
    )
}

export default CommunityShelf
