import {useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import axios from "axios";
import {baseUrl} from "../../../infrastructure/apiConfig.js";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import Box from "@mui/material/Box";
import {Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Fab, Grid} from "@mui/material";
import BookInfo from "../chunks/BookInfo.jsx";
import {AuthFab} from "../chunks/AuthoritiesButtons.jsx";
import * as React from "react";


const PermitRental = (props) => {
    const token = sessionStorage.getItem('token')

    const navigation = useNavigate()

    const [alert, setAlert] = useState(false)

    const params = useParams()

    const id = params.id

    const [response, setResponse] = useState({})

    useEffect(() => {axios.get(baseUrl + '/user/books/' + id + '?token=' + token).then(
        (response) => (setResponse(response.data))
    )}, [])

    const imagePath = baseUrl + '/assets/thumbnails/' + response.isbn

    const permitRental = () => {
        axios.post(baseUrl + '/user/' + id + '/rental-permit').then((response) => (
            navigation(-1)
        ))
    }


    return (
        <div>
            <Header theme={theme}/>
            <Box>
                <Grid container direction='column' justifyContent='flex-start' alignContent='space-evenly'>
                    <Grid item sx={{padding: 1}}>
                        <BookInfo value={response} width={props.windowWidth} height={props.windowHeight} imagePath={imagePath}/>
                    </Grid>
                    <Grid item>
                        <Grid container direction='row' justifyContent='space-evenly' alignContent='center'>
                            <Grid item>
                                <Fab variant="extended" color="primary" onClick={() => {
                                    navigation(-1)
                                }}>
                                    もどる
                                </Fab>
                            </Grid>
                            <Grid item>
                                <Fab variant="extended" color="primary" onClick={() => setAlert(true)}>
                                    貸出許可
                                </Fab>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
                <Dialog
                    open={alert}
                    onClose={permitRental}
                    aria-labelledby=""
                    aria-describedby="alert-dialog-description"
                >
                    <DialogTitle id="alert-dialog-title">
                        {"貸出を許可します"}
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText id="alert-dialog-description">
                            {response.title + 'の貸出を許可します'}
                        </DialogContentText>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={() => {setAlert(false)}}>キャンセル</Button>
                        <Button onClick={() => {permitRental()}} autoFocus>
                            はい
                        </Button>
                    </DialogActions>
                </Dialog>
            </Box>

        </div>
    )
}


export default PermitRental
