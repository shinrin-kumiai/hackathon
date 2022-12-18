import Box from "@mui/material/Box";
import {Button, Grid, TextField} from "@mui/material";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import {useForm} from "react-hook-form";
import {baseUrl} from "../../../infrastructure/apiConfig.js";
import {useState} from "react";
import axios from "axios";
import {useParams} from "react-router-dom";


const AddUsrtoCommunity = () => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const [user, setUser] = useState()
    const onSubmit = user => {
        setUser(user)
    }
    const token = sessionStorage.getItem('token')
    const params = useParams()
    return(
        <>
            <Header theme={theme}/>
            <Grid container direction='row' justifyContent='center' alignContent='center' sx={{width:1, height:1}}>
                <Grid item>
                    <Grid container direction='column' justifyContent='center' alignContent='center' sx={{width:1, height:1}}>
                        <Grid item sx={{margin:3}}>
                            <TextField
                                fullWidth
                                required
                                id="user_id"
                                label="ユーザid"
                                {...register('name', {
                                    onBlur: handleSubmit(onSubmit)
                                })}
                            />
                        </Grid>
                        <Grid item sx={{margin:3}}>
                            <Button variant="contained" onClick={() => {
                                axios.post(baseUrl + '/communities/' + params.communityID + 'add' + user + '?token=' + token).then((response) => {
                                    window.location.href='/community/'+ params.communityID +'/config'
                                })
                            }}>
                                追加
                            </Button>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </>
    )
}


export default AddUsrtoCommunity