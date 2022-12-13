import {configureStore} from "@reduxjs/toolkit";
import bookRegisterSliceReducer from "./createSlice.js";



const store = configureStore({
    reducer: {
        bookRegister: bookRegisterSliceReducer
    }
})

export default store
