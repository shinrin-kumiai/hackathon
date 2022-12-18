import { TextField, Button, Grid} from '@mui/material'
import { useForm } from 'react-hook-form'
import axios from "axios";


const Form = (props) => {
    const token = sessionStorage.getItem('token')
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    return (
        <>
            <Grid container direction="column" justifyContent="flex-start" alignContent="flex-start">
                <Grid item sx={{padding: 2, width:props.width}}>
                    <TextField
                        fullWidth
                        required
                        id="communityName"
                        label="コミュニティ名"
                        {...register('name', {
                            onBlur: handleSubmit(props.onSubmit)
                        })}
                    />
                </Grid>
                <Grid item sx={{padding:2, width:props.width}}>
                    <TextField
                        fullWidth
                        id="description"
                        label="説明書き"
                        multiline
                        rows={5}
                        {...register('description', {
                            onBlur: handleSubmit(props.onSubmit)
                        })}
                    />
                </Grid>
                <Grid item sx={{padding:2, width:props.width}}>
                    <Button onClick={() => {
                        axios.post(props.baseUrl + '/community/create?token=' + token, {
                            name: props.postData.name,
                            description: props.postData.description
                        }).then((response) => {
                            window.location.href = ('/community/' + response.data.id + '/config')
                        })
                    }}>
                        登録
                    </Button>
                </Grid>
            </Grid>

        </>
    )
}

export default Form