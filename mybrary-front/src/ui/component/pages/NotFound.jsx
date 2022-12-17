import Header from "../chunks/Header";
import {Grid} from "@mui/material";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";


const NotFound = () => {
    return (
        <Box>
            <Header/>
            <Grid container justifyContent='flex-start' alignContent='center'>
                <Grid item>
                    <Typography>
                        404 Not Page Found
                    </Typography>
                </Grid>
            </Grid>
        </Box>
    )
}

export default NotFound