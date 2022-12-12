import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import {ListItemIcon} from "@mui/material";
import ListItemText from "@mui/material/ListItemText";
import * as React from "react";
import Divider from "@mui/material/Divider";

import SettingsIcon from '@mui/icons-material/Settings';
import LogoutIcon from '@mui/icons-material/Logout';
import BookIcon from '@mui/icons-material/Book';

const communitiesList = ['woods', 'waterFront', 'funkyVally']


const Comunities = (props, idx) => {
    return (
        props.comunities.map((name, index) => {
            return (
                <ListItem key={index}>
                    <ListItemButton>
                        <ListItemIcon>

                        </ListItemIcon>
                        <ListItemText>
                            {name}
                        </ListItemText>
                    </ListItemButton>
                </ListItem>
            )
        })
    )
}


const Menu = () => (
    <List>
        <ListItem>
            <ListItemButton href='/'>
                <ListItemIcon>
                    <BookIcon/>
                </ListItemIcon>
                <ListItemText>
                    MyShelf
                </ListItemText>
            </ListItemButton>
        </ListItem>
        <Comunities comunities={communitiesList}/>
        <Divider/>
        <ListItem>
            <ListItemButton>
                <ListItemIcon>
                    <LogoutIcon/>
                </ListItemIcon>
                <ListItemText>
                    LogOut
                </ListItemText>
            </ListItemButton>
        </ListItem>
        <Divider/>
        <ListItem>
            <ListItemButton>
                <ListItemIcon>
                    <SettingsIcon/>
                </ListItemIcon>
                <ListItemText>
                    Settings
                </ListItemText>
            </ListItemButton>
        </ListItem>
    </List>
);

export default Menu
