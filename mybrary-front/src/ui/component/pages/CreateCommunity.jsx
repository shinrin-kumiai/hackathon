import {useState} from "react";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import * as React from "react";
import CommunityForm from "../elements/CommunityForm.jsx";
import Typography from "@mui/material/Typography";
import {Button} from "@mui/material";
import {baseUrl} from "../../../infrastructure/apiConfig.js";



const CreateCommunity = (props) => {
    const token = sessionStorage.getItem('token')
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

export default CreateCommunity