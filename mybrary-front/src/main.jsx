import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import store from "./store/index.js";
import {Provider} from "react-redux";
import { PublicClientApplication } from "@azure/msal-browser";
import { MsalProvider } from "@azure/msal-react";
// import { msalConfig } from "./authConfig";

// const msalInstance = new PublicClientApplication(msalConfig);

ReactDOM.createRoot(document.getElementById('root')).render(
      <Provider store={store}>
        {/*<MsalProvider instance={msalInstance}>*/}
            <App />
        {/*</MsalProvider>*/}
      </Provider>
)
