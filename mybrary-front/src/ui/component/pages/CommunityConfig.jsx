import {Button, Grid, ListItem} from "@mui/material";
import MemberList from "../elements/MemberList.jsx";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItemText from "@mui/material/ListItemText";
import {useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import axios from "axios";
import Typography from "@mui/material/Typography";


const CommunityConfig = (props) => {
    // const baseUrl = 'http://localhost:8000/'
    const params = useParams()
    // const CommunityId = params.id
    // const[communityInfo, setCommunityInfo] = useState({})
    // axios.get(baseUrl + 'community/' + CommunityId).then(response => {setCommunityInfo(response)}).catch((err) => {
    //         if (err.response.status === 401 ){
    //             window.location.href='https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN&client_id=ac29ed4e-39b1-4632-b6fd-ff5867d75b66&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A5173&scope=openid&response_type=id_token&prompt=login'
    //         } else {
    //             window.location.href='/'
    //         }
    //     })
    const [communityInfo, setCommunityInfo] = useState({})
    useEffect(() => {axios.get('http://localhost:8000/communities/' + params.communityID  + '?token=' + token).then(
        (response) => setCommunityInfo(response.data)
    )}, [])
    const [communityMembers, setCommunityMembers] = useState([])
    useEffect(() => {axios.get('http://localhost:8000/communities/' + params.communityID + '/members' + '?token=' + token).then(
        (response) => setCommunityMembers(response.data)
    )}, [])
    const token = sessionStorage.getItem('token')
    return (
        <Box>
            <Header theme={theme}/>
            <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                <Grid item sx={{width:0.05}}/>
                <Grid item sx={{width: 0.9}}>
                    <Grid container direction='column' justifyContent='flex-start' alignContent='flex-start' sx={{width: 1}}>
                        <Grid item sx={{padding:3}}>
                            <Typography fontSize={22}>
                                {communityInfo.name}
                            </Typography>
                        </Grid>
                        <Grid item sx={{width:1}}>
                            <List sx={{boxShadow: 2}}>
                                <ListItem>
                                    <ListItemText primary={communityInfo.description}/>
                                </ListItem>
                            </List>
                        </Grid>
                        <Grid item sx={{width: 1}}>
                            <MemberList members={communityMembers}/>
                        </Grid>
                        <Grid item>
                            <Button href={"/community/" + params.communityID + "/add-user"}>
                                メンバー追加
                            </Button>
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item sx={{width:0.05}}/>
            </Grid>
        </Box>

    )
}

export default CommunityConfig