
export const msalConfig= {
    auth: {
        clientId: '34d76626-.............',
        authority: 'https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SIGNUP_SIGNIN&client_id=ac29ed4e-39b1-4632-b6fd-ff5867d75b66&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A5173&scope=openid&response_type=id_token&prompt=login',
        knownAuthorities: ['usehackathon.b2clogin.com'],
        redirectUri: '/',
        postLogoutRedirectUri: '/',
    },
    cache: {
        cacheLocation: 'localStorage',
    },
};

export const loginRequest = {
    scopes: ['openid', 'offline_access'],
};