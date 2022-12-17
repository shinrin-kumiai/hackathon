import Box from "@mui/material/Box";
import {Card, CardMedia, Fab, Grid, ListItem} from "@mui/material";
import List from "@mui/material/List";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";


const BookInfo = (props) => {
    return (
        <Box>
            <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                <Grid item sx={{flexGrow:1, margin:1}}>
                    <Card sx={{boxShadow:0}}>
                        <Box sx={{maxHeight: props.height*0.5, maxWidth:props.width*0.9}}>
                            <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                                <Grid item>
                                    <CardMedia
                                        component="img"
                                        image={props.imagePath}
                                        alt="book_image"
                                        sx={{ boxShadow: 6, maxWidth: props.width*0.9, maxHeight: props.height*0.5}}
                                    />
                                </Grid>
                            </Grid>
                        </Box>
                    </Card>
                </Grid>
                <Grid item sx={{maxWidth: props.width, maxHeight: props.height * 1, boxShadow: 3, margin:1}}>
                    <List sx={{boxShadow: 4}}>
                        <ListItem>
                            <ListItemText primary={'ISBNコード:   ' + props.value.isbn} primaryTypographyProps={{fontSize: 13}}/>
                        </ListItem>
                        <Divider sx={{width: 0.9, marginX: 1}}/>
                        <ListItem>
                            <ListItemText primary={'タイトル:   ' + props.value.title} primaryTypographyProps={{fontSize: 13}}/>
                        </ListItem>
                        <Divider/>
                        <ListItem>
                            <ListItemText primary={'著者:   ' + props.value.creator} primaryTypographyProps={{fontSize: 13}}/>
                        </ListItem>
                        <Divider/>
                        <ListItem>
                            <ListItemText primary={'出版社:   ' + props.value.publisher} primaryTypographyProps={{fontSize: 13}}/>
                        </ListItem>
                        <Divider/>
                        <ListItem>
                            <ListItemText primary={'出版日:   ' + props.value.publish_date} primaryTypographyProps={{fontSize: 13}}/>
                        </ListItem>
                    </List>
                </Grid>

            </Grid>
        </Box>
    )
}

export default BookInfo