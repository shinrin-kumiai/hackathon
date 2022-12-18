import Box from "@mui/material/Box";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu.js";
import {ButtonBase, Card, CardActionArea, CardActions, CardMedia, Grid, ThemeProvider} from "@mui/material";
import Typography from "@mui/material/Typography";
import NotificationsIcon from "@mui/icons-material/Notifications.js";
import MenuBookSharpIcon from "@mui/icons-material/MenuBookSharp.js";
import LeftDrawer from "../elements/Drawer.jsx";
import * as React from "react";
import theme from "../../../theme.jsx";
import {useState} from "react";
import gifUrl from "../../../assets/Mybrary.gif"
import logoUrl from '../../../assets/sinrin-kumiai.png'


const width = window.innerWidth
const height = window.innerHeight

const LogOuted = () => {
    return (
        <div>
            <ThemeProvider theme={theme}>
                <Box sx={{ flexGrow: 1, margin:0}}>
                    <AppBar position="static">
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
                        </Toolbar>
                    </AppBar>
                </Box>
                <Box sx={{height:height * 0.9}}>
                    <Grid container justifyContent='center' alignContent='center' sx={{height:height * 0.9}}>
                        <Grid item sx={{boxShadow:1}}>
                            <Card sx={{boxShadow:0}}>
                                <CardActionArea href='/'>
                                    <CardMedia
                                        component="img"
                                        width={width}
                                        image={gifUrl}
                                        alt="bye bye"
                                    />
                                </CardActionArea>
                            </Card>
                        </Grid>
                    </Grid>
                </Box>
            </ThemeProvider>
        </div>
    )
}

export default LogOuted