import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import LeftDrawer from "../elements/Drawer.jsx";
import {useState} from "react";
import {createTheme, ThemeProvider} from "@mui/material";
import NotificationsIcon from '@mui/icons-material/Notifications';
import MenuBookSharpIcon from '@mui/icons-material/MenuBookSharp';





export default function Header(props) {
    const [isDrawerOpen, setIsDrawerOpen] = useState(false)
    return (
        <ThemeProvider theme={props.theme}>
            <Box sx={{ flexGrow: 1, margin:0}}>
                <AppBar position="static">
                    <Toolbar>
                        <IconButton
                            size="large"
                            edge="start"
                            color="inherit"
                            aria-label="menu"
                            sx={{ mr: 2 }}
                            onClick={() => {setIsDrawerOpen(true)}}
                        >
                            <MenuIcon/>
                        </IconButton>
                        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                            Mybrary
                        </Typography>
                        <IconButton size='large' color='inherit'>
                            <NotificationsIcon/>
                        </IconButton>
                        <IconButton size='large' color='inherit'>
                            <MenuBookSharpIcon/>
                        </IconButton>
                    </Toolbar>
                </AppBar>
                <LeftDrawer isOpen={isDrawerOpen} setIsOpen={setIsDrawerOpen}/>
            </Box>
        </ThemeProvider>
    )};

