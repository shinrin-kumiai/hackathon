import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
import {Grid, SwipeableDrawer} from "@mui/material";
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Menu from "./Menu.jsx";


const drawerWidth = 1000;

const DrawerHeader = styled('div')(({ theme }) => ({
    display: 'flex',
    alignItems: 'center',
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
    justifyContent: 'flex-end',
}));

const LeftDrawer = (props) => {
    return (
        <div>
            <SwipeableDrawer open={props.isOpen} onOpen={() => {props.setIsOpen(true)}} onClose={() => {props.setIsOpen(false)}} sx={{width:drawerWidth}} anchor='right'>
                <DrawerHeader sx={{backgroundColor:'#878989'}}>
                    <Grid sx={{width:240}}>
                        <Typography sx={{color:'#ffffff'}}>
                            Mybrary
                        </Typography>
                    </Grid>
                </DrawerHeader>
                <Divider/>
                <Menu communities={props.communities}/>
            </SwipeableDrawer>
        </div>
    );
}

export default LeftDrawer
