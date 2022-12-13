import Box from "@mui/material/Box";
import {Fab, Grid} from "@mui/material";
import * as React from "react";
import theme from "../../../theme.jsx";
import Header from "../chunks/Header.jsx";
import BookInfo from "../chunks/BookInfo.jsx";
import Typography from "@mui/material/Typography";
import store from "../../../store/index.js";
import axios from "axios";
import {useState} from "react";


function AddIcon() {
    return null;
}

const BookRegisterConfirm = (props) => {

    const [response, setResponse] = useState(null)

    const value = {
        imageURL: "https://m.media-amazon.com/images/I/51WG47XKOkL._SX351_BO1,204,203,200_.jpg",
        isbn: '1234567890123',
        title: "python爆速fire",
        author: "kazuki moriyama",
        publisher: "sonken shobou",
        publish_date: "2022/08/31"
    }
    axios.get('http://localhost:8000/user/books/register/?isbn=9784003320716', {
        headers: {}}).then((response) => {setResponse(response)})

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
                        <BookInfo response={response} width={props.windowWidth} height={props.windowHeight} ISBN={9784003320716}/>
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
