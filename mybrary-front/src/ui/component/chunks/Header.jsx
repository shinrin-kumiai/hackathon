import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import LeftDrawer from "../elements/Drawer.jsx";
import {useEffect, useState} from "react";
import {ButtonBase, ThemeProvider} from "@mui/material";
import NotificationsIcon from '@mui/icons-material/Notifications';
import MenuBookSharpIcon from '@mui/icons-material/MenuBookSharp';
import axios from "axios";
import {baseUrl} from "../../../infrastructure/apiConfig.js";





export default function Header(props) {
    const [isDrawerOpen, setIsDrawerOpen] = useState(false)
    const [communities, setCommunities] = useState([])
    useEffect(() => {axios.get(baseUrl + '/user/communities').then(
        (response) => (
            setCommunities(response.data)
        )
    )}, [])
    return (
            <Box sx={{ flexGrow: 1, margin:0}}>
                <AppBar position="fixed">
                    <Toolbar>
                        <Box sx={{ flexGrow: 1 }}>
                            <ButtonBase href='/'>
                                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                                    Mybrary
                                </Typography>
                            </ButtonBase>
                        </Box>

                        <IconButton size='large' color='inherit'>
                            <NotificationsIcon/>
                        </IconButton>
                        <IconButton size='large' color='inherit'>
                            <MenuBookSharpIcon/>
                        </IconButton>
                        <IconButton
                            size="large"
                            edge="start"
                            color="inherit"
                            aria-label="menu"
                            onClick={() => {setIsDrawerOpen(true)}}
                            sx={{paddingRight:0, paddingLeft:3}}
                        >
                            <MenuIcon/>
                        </IconButton>
                    </Toolbar>
                </AppBar>
                <Box sx={{height:50}}/>
                <LeftDrawer isOpen={isDrawerOpen} setIsOpen={setIsDrawerOpen} communities={communities}/>
            </Box>
    )};

