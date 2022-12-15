import List from "@mui/material/List";
import {ListItem, ListItemIcon} from "@mui/material";
import ListItemButton from "@mui/material/ListItemButton";
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import ListItemText from "@mui/material/ListItemText";


const MemberList = (props) => {
    return (
        <List sx={{boxShadow:2, width: 1}}>
            <ListItem sx={{width: 1}}>
                <ListItemText primary='メンバー'/>
            </ListItem>
            {props.members.map((member, index) => {
                return (
                    <ListItem key={index}>
                        <ListItemButton>
                            <ListItemIcon>
                                <AccountCircleIcon/>
                            </ListItemIcon>
                            <ListItemText primary={member.name}/>
                        </ListItemButton>
                    </ListItem>
                )
            })}

        </List>
    )
}

export default MemberList