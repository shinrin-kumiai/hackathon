import * as React from 'react';
import Typography from "@mui/material/Typography";

import Header from "../chunks/Header.jsx";
import BookCard from "../elements/BookCard.jsx";
import BookCards from "../chunks/BookCards.jsx";
import {Card, createTheme, Grid} from "@mui/material";
import {Girl} from "@mui/icons-material";
import Box from "@mui/material/Box";
import FunctionsSpeedDial from "../chunks/FunctionsSpeedDial.jsx";


const theme = createTheme({
    palette:{
        primary:{
            main: '#696c6c'
        }
    }
})


const books = [{title: 'mori', preDate: '2022/8/31'}, {title: 'hayashi', preDate: '2022/12/31'}, {title: 'tanaka', preDate: '2023/1/5'}, {title: 'sonken', preDate: '2023/12/3'}]

const Top = (props) => {
    return (
        <div>
            <Header theme={theme}/>
            <Box>
                <Grid container direction='column' justifyContent='flex-start' alignContent='space-evenly'>
                    <Grid item>
                        <BookCards books={books} theme={theme}/>
                    </Grid>
                </Grid>
            </Box>
        </div>
    )
}

export default Top
