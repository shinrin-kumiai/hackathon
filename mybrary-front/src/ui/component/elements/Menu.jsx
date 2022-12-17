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
import {useCookies} from "react-cookie";
import {useEffect, useState} from "react";
import axios from "axios";
import {baseUrl} from "../../../infrastructure/apiConfig.js";

const Communities = (props) => {
    return (
        props.comunities.map((community, index) => {
            return (
                <ListItem key={index}>
                    <ListItemButton onClick={() => {
                        window.location.href='/community/' + community.id + '/books'
                    }}>
                        <ListItemIcon>

                        </ListItemIcon>
                        <ListItemText>
                            {community.name}
                        </ListItemText>
                    </ListItemButton>
                </ListItem>
            )
        })
    )
}




const Menu = (props) => {

    const [cookies, setCookie, removeCookie] = useCookies(["tkn"]);
    return (
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
            <Communities comunities={props.communities}/>
            <Divider/>
            <ListItem>
                <ListItemButton href='/community/new'>
                    <ListItemIcon>

                    </ListItemIcon>
                    <ListItemText>
                        CreateCommunity
                    </ListItemText>
                </ListItemButton>
            </ListItem>
            <Divider/>
            <ListItem>
                <ListItemButton onClick={() => {
                    removeCookie("tkn")
                    window.location.href='/bye-bye'
                }}>
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
    )
};

export default Menu
