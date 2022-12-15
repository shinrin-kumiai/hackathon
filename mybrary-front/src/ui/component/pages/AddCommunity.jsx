import Box from "@mui/material/Box";
import {useState} from "react";
import {
    Button,
    FormControl,
    FormHelperText,
    Grid,
    InputAdornment,
    InputLabel,
    OutlinedInput,
    TextField
} from "@mui/material";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import * as React from "react";
import { useFormControl } from '@mui/material/FormControl';
import {Controller, useForm} from "react-hook-form";
import {Form} from "react-router-dom";
import axios from "axios";
import CommunityForm from "../elements/CommunityForm.jsx";
import Typography from "@mui/material/Typography";



const AddCommunity = (props) => {
    const baseUrl = 'http://localhost:8000'
    const [postData, setPostData] = useState({})
    const onSubmit = data => {
        console.log(data);
        setPostData(data)
        console.log(postData)
    }

    return (
        <div>
            <Header theme={theme}/>
            <Typography　sx={{margin:2}}>
                コミュニティを作成する
            </Typography>
            <CommunityForm
                width={props.windowWidth} height={props.windowHeight}
                baseUrl={baseUrl}
                onSubmit={onSubmit}
                postData={postData}
                setPostData={setPostData}
            />

        </div>

    )
}

export default AddCommunity