import { b2cPolicies } from "./policies";
import { apiConfig } from "./apiConfig";
import * as msal from "msal"
export const msalConfig = {
  auth: {
    clientId: "f146ba92-5e30-473e-a164-36b2aa6559d8", // This is the ONLY mandatory field; everything else is optional.
    authority: b2cPolicies.authorities.signUpSignIn.authority, // Choose sign-up/sign-in user-flow as your default.
    knownAuthorities: [b2cPolicies.authorityDomain], // You must identify your tenant's domain as a known authority.
    redirectUri: "https://ashy-beach-0bd0cb400.2.azurestaticapps.net/login/redirect", // You must register this URI on Azure Portal/App Registration. Defaults to "window.location.href".
  },
  cache: {
    cacheLocation: "sessionStorage",  
    storeAuthStateInCookie: false, 
  },
  system: {
    loggerOptions: {
      loggerCallback: (level, message, containsPii) => {
        if (containsPii) {
          return;
        }
        switch (level) {
          case msal.LogLevel.Error:
            console.error(message);
            return;
          case msal.LogLevel.Info:
            console.info(message);
            return;
          case msal.LogLevel.Verbose:
            console.debug(message);
            return;
          case msal.LogLevel.Warning:
            console.warn(message);
            return;
        }
      }
    }
  }
};

export const loginRequest = {
scopes: ["openid", ...apiConfig.b2cScopes],
};

const tokenRequest = {
scopes: [...apiConfig.b2cScopes],  // e.g. ["https://fabrikamb2c.onmicrosoft.com/helloapi/demo.read"]
forceRefresh: false // Set this to "true" to skip a cached token and go to the server to get a new token
};