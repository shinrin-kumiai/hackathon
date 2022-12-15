import {Card, CardActionArea, CardContent, CardMedia, Grid} from "@mui/material";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";


const BookCard = (props) => {

    // const date = Date.now()
    // const preDate = Date.parse(props.book.preDate)

    // const cardBgColor = (() => {
    //     if (props.book.status==='rental' && date > preDate) {
    //         return ('#ffe1b9')
    //     }else if (props.book.status==='rental') {
    //         return ('#e0ffd6')
    //     }else if (props.book.status==='rending') {
    //         return ('#cecece')
    //     }else {
    //         return ('#ffffff')
    //     }
    // });

    const cardBgColor = '#ffffff'

    return (
        <Box id={props.book.id}>
            <Card sx={{ width: 150, height: 200, boxShadow:6, backgroundColor: cardBgColor}}>
                <CardActionArea sx={{ width: 150, height: 200 }} href={'/book/detail/' + props.book.id}>
                    <Box sx={{height:160}}>
                        <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                            <Grid item>
                                <CardMedia
                                    component="img"
                                    height="160"
                                    image={"http://localhost:8000/assets/thumbnails/" + props.book.isbn}
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
