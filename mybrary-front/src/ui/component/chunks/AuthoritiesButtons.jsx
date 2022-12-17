import Box from "@mui/material/Box";
import {Button, Grid} from "@mui/material";


export const Edit = (props) => {
    if (props.authenticate) {
    return (
            <Button
                variant='contained'
                onClick={() => {
                    window.location.href='/'
                }}
            />
    )} else {
        return(
            <></>
        )
    }
}

