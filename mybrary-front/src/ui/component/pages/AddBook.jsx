import * as React from 'react';
import ScannerIndex from "../../../scanner/scannerIndex.jsx";
import Box from "@mui/material/Box";
import {Alert, Grid} from "@mui/material";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import {Snackbar} from "@mui/material";
import {useEffect, useState} from "react";
import {connect, useSelector} from "react-redux";

const AddBook = (props) => {
    const [openSnackbar, setOpenSnackbar] = useState(false)
    const currentErr = useSelector((state) => state.bookRegister.err)
    const crisbn = useSelector((state) => state.bookRegister.isbn)
    useEffect(() => {
        console.log(currentErr)
        console.log(crisbn)
        if (currentErr !== "none") {
            setOpenSnackbar(true)
    }})


    return (
        <div>
            <Header theme={theme}/>
            <Box sx={{maxWidth: props.windowWidth, maxHeight: props.windowHeight}}>
                <Grid container direction='column' justifyContent='center' alignContent='center'>
                    <Grid item>
                        <ScannerIndex width={props.windowWidth}/>
                    </Grid>
                    <Grid item>
                        <Snackbar open={openSnackbar} autoHideDuration={6000}>
                            <Alert severity="error">{currentErr}</Alert>
                        </Snackbar>
                    </Grid>
                </Grid>
            </Box>
        </div>
    )
}

const getError = (state) => {
    return { err: state.err }
}

export default connect(getError)(AddBook)
