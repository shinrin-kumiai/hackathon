import React, { useState } from "react";
import Scanner from "./Scanner";
import {Grid} from "@mui/material";


const ScannerIndex = (props) => {
    const [camera, setCamera] = useState(true);
    const [result, setResult] = useState(null);

    const onDetected = result => {
        setResult(result);
        setCamera(!camera)
        console.log(result)
        // axios.post('http://localhost:8000/book/regist?isbn=' + result)
        window.location.href = '/book/register_confirm/'
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