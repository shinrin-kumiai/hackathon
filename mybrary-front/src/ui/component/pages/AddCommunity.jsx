import Box from "@mui/material/Box";
import {useState} from "react";
import {FormControl, FormHelperText, Grid, InputAdornment, InputLabel, OutlinedInput, TextField} from "@mui/material";
import Header from "../chunks/Header.jsx";
import theme from "../../../theme.jsx";
import * as React from "react";
import { useFormControl } from '@mui/material/FormControl';
import {Controller, useForm} from "react-hook-form";


const AddCommunity = (props) => {
    const [communityName, setCommunityName] = useState(null)
    const [descripation, setDescription] = useState(null)

    const {control, handleSubmit, getValues} = useForm()


    return (
        <div>
            <Header theme={theme}/>
            <Box sx={{width: props.windowWidth}}>
                <Grid container direction='column' justifyContent='flex-start' alignContent='center'>
                    <Grid item sx={{margin: 2}}>
                        <Controller
                            control={control}
                            name="name"
                            defaultValue={""}
                            rules={{required: {value: true, message: '入力必須です'}}}
                            render={({field, fieldState: {error}}) =>
                                (<TextField
                                {...field}
                                id="outlined-required"
                                label="Required"
                                defaultValue="John's community"
                                />
                                )}
                        />
                    </Grid>
                    <Grid item sx={{margin: 2, width: props.windowWidth}}>
                        <FormControl fullWidth>
                            <InputLabel htmlFor="outlined-adornment-amount">Description</InputLabel>
                            <OutlinedInput
                                id="outlined-adornment-amount"
                                label="Description"
                            />
                        </FormControl>
                    </Grid>
                </Grid>

            </Box>
        </div>

    )
}

export default AddCommunity