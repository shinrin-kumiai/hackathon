// import apiConfig from "./apiConfig.js";
// import axios from "axios";
//
// const postBook = axios.create({
//         baseURL: apiConfig.postBook.URL,
//         headers: { Authorization: `Bearer ${window.localStorage.getItem('access_token')}` },
//         timeout: apiConfig.postBook.timeout
//     });
//
// const getBookInfo = axios.create({
//     baseURL: apiConfig.getBookInfo.URL,
//     headers: { Authorization: `Bearer ${window.localStorage.getItem('access_token')}` },
//     timeout: apiConfig.getBookInfo.timeout
// })
//
// const instance = {"postBook": postBook, "getBookInfo": getBookInfo}
//
// export default instance