import {Button, Grid, ListItem} from "@mui/material";
import MemberList from "../elements/MemberList.jsx";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItemText from "@mui/material/ListItemText";


const CommunityConfig = (props) => {
    // const baseUrl = 'http://localhost:8000/'
    // const params = useParams()
    // const CommunityId = params.id
    // const[communityInfo, setCommunityInfo] = useState({})
    // axios.get(baseUrl + 'community/' + CommunityId).then(response => {setCommunityInfo(response)}).catch(
    //     (err) => {
    //         console.log(err)
    //     }
    // )
    const communityInfo = {
        name: 'hayashi',
        id: 12345666,
        description: 'こんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちはこんにちは',
        members: [
            {
                name: 'hayashi',
                id: 12893798745,

            }
        ]
    }
    return (
        <Box>
            <Header theme={theme}/>
            <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                <Grid item sx={{width:0.05}}/>
                <Grid item sx={{width: 0.9}}>
                    <Grid container direction='column' justifyContent='flex-start' alignContent='flex-start' sx={{width: 1}}>
                        <Grid item sx={{}}>
                            <List sx={{boxShadow: 2}}>
                                <ListItem>
                                    <ListItemText primary={communityInfo.name}/>
                                </ListItem>
                                <ListItem>
                                    <ListItemText primary={communityInfo.description}/>
                                </ListItem>
                            </List>
                        </Grid>
                        <Grid item sx={{width: 1}}>
                            <MemberList members={communityInfo.members}/>
                        </Grid>
                        <Grid item>
                            <Button>
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