import {ButtonBase, Card, CardActionArea, CardContent, CardMedia, Grid} from "@mui/material";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";


const BookTitle = (props) => {
    return (
        <Box sx={{margin: 0}}>

        </Box>
    )
}


const BookCard = (props) => {

    const date = Date.now()
    const preDate = Date.parse(props.book.preDate)

    let cardBgColor;
    if (date > preDate) {
        cardBgColor = '#ffe1b9'
    }else {
        cardBgColor = '#ffffff'
    }

    return (
        <Box>
            <Card sx={{ width: 150, height: 200, boxShadow:6, backgroundColor: cardBgColor}}>
                <CardActionArea sx={{ width: 150, height: 200 }}>
                    <Box sx={{height:160}}>
                        <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                            <Grid item>
                                <CardMedia
                                    component="img"
                                    height="160"
                                    image="https://m.media-amazon.com/images/I/51WG47XKOkL._SX351_BO1,204,203,200_.jpg"
                                    alt="green iguana"
                                />
                            </Grid>
                        </Grid>
                    </Box>
                    <CardContent sx={{maxWidth: 150, paddingY: 1}}>
                        <Typography color="text.secondary" fontSize={13} noWrap>
                            {props.book.title}
                        </Typography>
                    </CardContent>
                </CardActionArea>
            </Card>
        </Box>

    )
}

export default BookCard
