import React, {useEffect, useState} from "react";
import Scanner from "./Scannera";
import {Grid} from "@mui/material";
import axios from "axios";
import {useDispatch, useSelector, useStore} from "react-redux";
import store from "../store/index.js";
import {connect} from "react-redux";
import {updateErr, updateIsbn} from "../store/createSlice.js";
import {baseUrl} from "../infrastructure/apiConfig.js";


const ScannerIndex = (props) => {

    const crisbn = useSelector((state) => state.bookRegister.isbn)

    const [camera, setCamera] = useState(true);

    const onDetected = result => {
        setCamera(!camera)

        axios.post(baseUrl + '/user/books/register/?isbn=' + result).then((response) => {
                window.location.href = '/book/register-confirm/' + response.data.isbn + '/' + response.data.id
            }).catch((err) => {
            if (err.response?.status === 401) {
                window.location.href = 'https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN&client_id=ac29ed4e-39b1-4632-b6fd-ff5867d75b66&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A5173&scope=openid&response_type=id_token&prompt=login'
            }
            if (err.response?.status === 404) {
                window.location.href = '/404-not-found'
            }
            if (err.isAxiosError && err.response?.data?.errors) {
                window.location.href = '/book/register'
            }
        })

    };

    return (
        <section className="section-wrapper">
            <div className="section-title">
                <h1 className="section-title-text">
                    {camera ? <Grid container direction='column' justifyContent='center' alignContent='center'>
                        <Grid item>
                            <Scanner onDetected={onDetected} width={props.width}/>
                        </Grid>
                    </Grid> : <p>読み込み中...</p> }
                </h1>
            </div>
        </section>
    );
}


export default ScannerIndex