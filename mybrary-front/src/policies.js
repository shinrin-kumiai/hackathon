export const b2cPolicies = {
    names: {
        signUpSignIn: "B2C_1A_SIGNUP_SIGNIN",
        // forgotPassword: "B2C_1A_SIGNUP_SIGNIN",
        // editProfile: "B2C_1A_SIGNUP_SIGNIN"
    },
    authorities: {
        signUpSignIn: {
            authority: "https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/B2C_1A_SIGNUP_SIGNIN"
        // },
        // forgotPassword: {
        //     authority: "https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/B2C_1A_SIGNUP_SIGNIN",
        // },
        // editProfile: {
        //     authority: "https://usehackathon.b2clogin.com/usehackathon.onmicrosoft.com/B2C_1A_SIGNUP_SIGNIN"
        }
    },
    authorityDomain: "usehackathon.b2clogin.com"
}