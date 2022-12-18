import Box from "@mui/material/Box";
import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogContentText,
    DialogTitle,
    Grid,
    TextField
} from "@mui/material";
import {useForm} from "react-hook-form";
import {useEffect, useState} from "react";
import axios from "axios";
import {baseUrl} from "../../../infrastructure/apiConfig.js";
import {useParams} from "react-router-dom";
import * as React from "react";
import Header from "../chunks/Header";
import dayjs from "dayjs";


const RentalRequest = () => {
    const token = sessionStorage.getItem('token')
    const [confirm, setConfirm] = useState(false)
    const params = useParams()
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const [data, setData] = useState({})
    const [url, setUrl] = useState(baseUrl + '/user/' + params.id + '/rental-request' + '?token=' + token)
    useEffect(() => {
        if (data.dueDate) {
            setUrl(baseUrl + '/user/' + params.id + '/rental-request?return_due_date=' + data.dueDate + '&token=' + token)
        }
    })
    return (
        <div>
            <Box>
                <Header/>
                <Grid container direction='row' justifyContent='center' alignContent='center' sx={{marginTop:4}}>
                    <Grid item sx={{width:0.05}}/>
                    <Grid item sx={{width:0.9}}>
                        <Grid container direction='column' justifyContent='flex-start' alignContent='flex-start'>
                            <Grid item>
                                <TextField
                                    fullWidth
                                    required
                                    id="communityName"
                                    label="返却予定日"
                                    type="date"
                                    defaultValue={'2022-12-25'}
                                    {...register('dueDate', {
                                        onBlur: handleSubmit(setData)
                                    })}
                                />
                            </Grid>
                            <Grid item>
                                <Button onClick={() => {
                                    axios.post(url).then(() => {
                                        setConfirm(true)
                                    })
                                }}>
                                    送信
                                </Button>
                            </Grid>
                        </Grid>
                    </Grid>
                    <Grid item sx={{width:0.05}}/>
                </Grid>
            </Box>
            <Dialog
                open={confirm}
                aria-labelledby="reequest"
                aria-describedby="request-dialog-description"
            >
                <DialogTitle id="request-dialog-title">
                    {"リクエスト送信"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="request-dialog-description">
                        {data.dueDate + 'までの貸出リクエストを送りました'}
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => {window.location.href='/'}}>OK❗️</Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}

export default RentalRequest