import Box from "@mui/material/Box";
import {Fab, Grid} from "@mui/material";
import * as React from "react";
import theme from "../../../theme.jsx";
import Header from "../chunks/Header.jsx";
import BookInfo from "../chunks/BookInfo.jsx";
import Typography from "@mui/material/Typography";
import {useState} from "react";
import {useSelector} from "react-redux";


function AddIcon() {
    return null;
}

const BookRegisterConfirm = (props) => {

    // const params = useParams()

    const ConfirmBook = useSelector(state => state.bookRegister.isbn)

    const [response, setResponse] = useState(null)

    const value = {
        imageURL: "https://m.media-amazon.com/images/I/51WG47XKOkL._SX351_BO1,204,203,200_.jpg",
        isbn: ConfirmBook,
        title: "python爆速fire",
        author: "kazuki moriyama",
        publisher: "sonken shobou",
        publish_date: "2022/08/31"
    }
    // axios.get('http://localhost:8000/user/books/?isbn=9784798067278', {
    //     headers: {}}).then((response) => {setResponse(response)})
    // useEffect(() => {
    //     axios.get('http://localhost:8000/assets/thumbnails/9784798067278', {
    //         headers: {}}).then((response) => {setResponse(response)}).catch((err) => {
    //         if (err.response.status === 401 ){
    //             window.location.href='https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN&client_id=ac29ed4e-39b1-4632-b6fd-ff5867d75b66&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A5173&scope=openid&response_type=id_token&prompt=login'
    //         } else {
    //             window.location.href='/'
    //         }
    //     })
    // }, [])

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
