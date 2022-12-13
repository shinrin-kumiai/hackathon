import {createSlice} from "@reduxjs/toolkit";

export const bookRegisterSlice = createSlice({
    name: 'bookRegister',
    initialState:{
        isbn: 0,
        err: 'none'
    },
    reducers: {
        updateIsbn: (state, action) => {
            state.isbn = action.payload
        },
        updateErr: (state, action) => {
            state.err = action.payload
        },
    },
})

export const { updateIsbn, updateErr } = bookRegisterSlice.actions;

export default bookRegisterSlice.reducer;
