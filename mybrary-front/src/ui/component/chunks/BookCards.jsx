import * as React from 'react';
import {Grid, ThemeProvider} from "@mui/material";
import BookCard from "../elements/BookCard.jsx";
import Box from "@mui/material/Box";


const BookCards = (props) => {
    return (
        <ThemeProvider theme={props.theme}>
            <Box flex>
                <Grid container direction='row' justifyContent='space-evenly' alignContent='baseline'>
                    {props.books.map((book) => {
                        return(
                            <Grid item sx={{marginTop: 4, marginX: 2}}>
                                <BookCard book={book}/>
                            </Grid>
                        )
                    })}
                </Grid>
            </Box>
        </ThemeProvider>
    )
}

export default BookCards
