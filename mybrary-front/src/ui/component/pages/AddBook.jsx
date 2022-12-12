import * as React from 'react';
import ScannerIndex from "../../../scanner/scannerIndex.jsx";
import Box from "@mui/material/Box";
import {Grid} from "@mui/material";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";


const AddBook = (props) => {
    return (
        <div>
            <Header theme={theme}/>
            <Box sx={{maxWidth: props.windowWidth, maxHeight: props.windowHeight}}>
                <Grid container direction='column' justifyContent='center' alignContent='center'>
                    <Grid item>
                        <ScannerIndex width={props.windowWidth}/>
                    </Grid>
                </Grid>
            </Box>
        </div>
    )
}



export default AddBook
