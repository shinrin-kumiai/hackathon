import Box from "@mui/material/Box";
import {Card, CardMedia, Fab, Grid, ListItem} from "@mui/material";
import List from "@mui/material/List";
import ListItemText from "@mui/material/ListItemText";


const BookInfo = (props) => {
    return (
        <Box>
            <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                <Grid item>
                    <Box sx={{maxWidth: props.width, maxHeight: props.height * 1, boxShadow: 6}}>
                        <Card>
                            <Box sx={{maxHeight: props.height*0.5, maxWidth:props.width*0.9}}>
                                <CardMedia
                                    component="img"
                                    image={props.response.imageURL}
                                    alt="book_image"
                                    sx={{maxWidth: props.width*0.9, maxHeight: props.height*0.5}}
                                />
                            </Box>
                        </Card>
                    </Box>
                </Grid>
                <Grid item>
                    <List>
                        <ListItem>
                            <ListItemText primary={'ISBNコード:   ' + props.response.isbn}/>
                        </ListItem>
                        <ListItem>
                            <ListItemText primary={'タイトル:   ' + props.response.title}/>
                        </ListItem>
                        <ListItem>
                            <ListItemText primary={'著者:   ' + props.response.author}/>
                        </ListItem>
                        <ListItem>
                            <ListItemText primary={'出版社:   ' + props.response.publisher}/>
                        </ListItem>
                        <ListItem>
                            <ListItemText primary={'出版日:   ' + props.response.publish_date}/>
                        </ListItem>
                    </List>
                </Grid>

            </Grid>
        </Box>
    )
}

export default BookInfo