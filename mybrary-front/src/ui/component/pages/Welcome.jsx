import Header from "../chunks/Header";
import Box from "@mui/material/Box";
import {Button, Grid, TextField} from "@mui/material";
import {useForm} from "react-hook-form";
import axios from "axios";
import {baseUrl} from "../../../infrastructure/apiConfig.js";
import {useState} from "react";


const Welcome = () => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const [userInfo, setUserInfo] = useState({})
    const onSubmit = (data) => {
        setUserInfo(data)
    }
    return (
        <>
            <Header/>
            <Box sx={{width:1, height:1}}>
                <Grid container direction='column' justifyContent='center' alignContent='center' sx={{width:1, height:1}} xs={12}>
                    <Grid item sx={{margin:2, width:0.7, height:0.7}}>
                        <TextField
                            variant='standard'
                            fullWidth
                            required
                            id="name"
                            label="ユーザー名"
                            {...register('name', {
                                onBlur: handleSubmit(onSubmit)
                            })}
                        />
                    </Grid>
                    <Grid item sx={{margin:2, width: 0.7, height: 0.7}}>
                        <TextField
                            variant='standard'
                            fullWidth
                            required
                            id="mailAdress"
                            label="メールアドレス　"
                            {...register('mail_address', {
                                onBlur: handleSubmit(onSubmit)
                            })}
                        />
                    </Grid>
                    <Grid item sx={{margin: 2, width: 1, height: 1}}>
                        <Button onClick={() => {
                            axios.post(baseUrl + '/user/signup', userInfo).then(() => {
                                window.location.href = '/'
                            })
                        }}>
                            登録
                        </Button>
                    </Grid>
                </Grid>
            </Box>
        </>
    )
}

export default Welcome