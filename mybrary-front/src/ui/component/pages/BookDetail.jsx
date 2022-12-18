import Box from "@mui/material/Box";
import {Button, DialogActions, DialogContent, DialogContentText, DialogTitle, Fab, Grid} from "@mui/material";
import * as React from "react";
import theme from "../../../theme.jsx";
import Header from "../chunks/Header.jsx";
import BookInfo from "../chunks/BookInfo.jsx";
import axios from "axios";
import {useEffect, useState} from "react";
import {useNavigate, useNavigation, useParams} from "react-router-dom";
import {baseUrl} from "../../../infrastructure/apiConfig.js";
import {AuthFab} from "../chunks/AuthoritiesButtons.jsx";
import {Dialog} from "@mui/material";


function AddIcon() {
    return null;
}

const BookDetail = (props) => {

    const navigation = useNavigate()

    const [alert, setAlert] = useState(false)

    const [rentalAlert, setRentalAlaert] = useState(false)

    const [returnAlert, setReturnAlert] = useState(false)

    const params = useParams()

    const id = params.id

    const [response, setResponse] = useState({})

    const token = sessionStorage.getItem('token')

    useEffect(() => {axios.get(baseUrl + '/user/books/' + id + '?token=' + token).then(
        (response) => (setResponse(response.data))
    )}, [])

    const imagePath = baseUrl + '/assets/thumbnails/' + response.isbn

    const deleteRelation = () => {
        axios.delete(baseUrl + '/user/books/' + id).then((response) => (
            window.location.href = '/'
        ))
    }

    const startRental = () => {
        axios.post(baseUrl + '/user/' + id + '/rental-confirm').then((response) => (
            navigation(-1)
        ))
    }
    const endRental = () => {
        axios.post(baseUrl + '/user/' + id + '/return-confirm').then(() => (
            navigation((-1))
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
                                {/*<Fab variant="extended" color="primary" onClick={() => deleteRelation()}>*/}
                                {/*    登録を解除*/}
                                {/*</Fab>*/}
                                <AuthFab auth={(!!(response.has_permission))&(response.latest_state_id===1)} onClickEvent={() => {setAlert(true)}} txt='登録を解除' color={'warning'}/>
                                <AuthFab auth={!!!(response.has_permission)&(response.latest_state_id===1)} onClickEvent={() => {window.location.href='/book/detail/' + params.id + '/request?token=' + token}} txt='貸出リクエスト' color={'secondary'}/>
                                <AuthFab auth={!!(response.has_permission)&(response.latest_state_id===2)} onClickEvent={() => {window.location.href='/book/detail/' + params.id + '/permit?token=' + token}} txt='貸出リクエスト在中' color={'secondary'}/>
                                <AuthFab auth={!!!(response.has_permission)&(response.latest_state_id===3)} onClickEvent={() => {setRentalAlaert(true)}} txt='受け取り報告' color={'secondary'}/>
                                <AuthFab auth={!!(response.has_permission)&(response.latest_state_id===4)} onClickEvent={() => {setReturnAlert(true)}} txt='返却報告' color={'secondary'}/>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
                <Dialog
                    open={alert}
                    onClose={deleteRelation}
                    aria-labelledby=""
                    aria-describedby="alert-dialog-description"
                >
                    <DialogTitle id="alert-dialog-title">
                        {"登録から削除します"}
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText id="alert-dialog-description">
                            {response.title + 'を登録から削除します。'}
                        </DialogContentText>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={() => {setAlert(false)}}>キャンセル</Button>
                        <Button onClick={deleteRelation} autoFocus>
                            はい
                        </Button>
                    </DialogActions>
                </Dialog>

                <Dialog
                    open={rentalAlert}
                    onClose={deleteRelation}
                    aria-labelledby=""
                    aria-describedby="alert-dialog-description"
                >
                    <DialogTitle id="alert-dialog-title">
                        {"レンタル開始"}
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText id="alert-dialog-description">
                            {response.title + 'を受け取りました。'}
                        </DialogContentText>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={() => {setAlert(false)}}>キャンセル</Button>
                        <Button onClick={startRental} autoFocus>
                            はい
                        </Button>
                    </DialogActions>
                </Dialog>
                <Dialog
                    open={returnAlert}
                    onClose={deleteRelation}
                    aria-labelledby=""
                    aria-describedby="alert-dialog-description"
                >
                    <DialogTitle id="alert-dialog-title">
                        {"レンタル終了"}
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText id="alert-dialog-description">
                            {response.title + "が返されました"}
                        </DialogContentText>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={() => {setReturnAlert(false)}}>キャンセル</Button>
                        <Button onClick={endRental} autoFocus>
                            はい
                        </Button>
                    </DialogActions>
                </Dialog>
            </Box>
        </div>
    )
}


export default BookDetail
