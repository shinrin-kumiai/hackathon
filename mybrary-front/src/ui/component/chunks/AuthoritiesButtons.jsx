import Box from "@mui/material/Box";
import {Button, Fab, Grid} from "@mui/material";


export const AuthButton = (props) => {
    if (props.auth) {
    return (
            <Button
                variant='contained'
                onClick={() => {
                    props.onClickEvent
                }}
            >
                {props.txt}
            </Button>
    )} else {
        return(
            <Box sx={{width:0, height:0}}/>
        )
    }
}


export const AuthFab = (props) => {
    if (props.auth) {
        return (
            <Fab variant="extended" color={props.color} onClick={props.onClickEvent} >
                {props.txt}
            </Fab>
        )} else {
        return(
            <Box sx={{width:0, height:0}}/>
        )
    }
}
