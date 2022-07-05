import React, {useEffect,  useContext} from 'react';
import { useNavigate } from "react-router-dom";
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Snackbar from '@mui/material/Snackbar';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Navbar from '../elements/Navbar';
import Footer from '../elements/Footer';
import Axios from 'axios';
import {useImmerReducer} from 'use-immer';
import DispatchContext from '../../Context/DispatchContext';
import stateContext from '../../Context/StateContext';



const theme = createTheme();

export default function SignUp() {
    const navigate = useNavigate();
    const Globaldispatch = useContext(DispatchContext)
    const GlobalState = useContext(stateContext)
    
    const initialState = { 
        usernameValue:'',
        emailValue:'', 
        passwordValue:'', 
        rePasswordValue:'', 
        sendRequest:0, 
        openSnack: false,
		disabledBtn: false,
		serverError: false,
        usernameErrors:{
            hasErrors: false,
            errorMessage: ''
        },
        emailErrors:{
            hasErrors: false,
            errorMessage: ''
        },
        passwordErrors:{
            hasErrors: false,
            errorMessage: ''
        },
        passwordReErrors:{
            hasErrors: false,
            errorMessage: ''
        },
        serverMessageUsername: "",
		serverMessageEmail: "",
		serverMessageSimilarPassword: "",
		serverMessageCommonPassword: "",
		serverMessageNumericPassword: "",
    }


    
    
    function ReducerFuction(draft, action) {
        switch (action.type) {
            case 'catchUsernameChange':
                draft.usernameValue = action.usernameChosen;
                draft.usernameErrors.hasErrors = false
                draft.usernameErrors.errorMessage = ''
                draft.serverMessageUsername = "";
                break;
            case 'catchEmailChange':
                draft.emailValue = action.emailChosen;
                draft.emailErrors.hasErrors = false
                draft.emailErrors.errorMessage = ''
                draft.serverMessageEmail = "";

                break;
            case 'catchPasswordChange':
                draft.passwordValue = action.passwordChosen;
                draft.passwordErrors.hasErrors = false;
                draft.passwordErrors.errorMessage = '';
                draft.serverMessageSimilarPassword = "";
				draft.serverMessageCommonPassword = "";
				draft.serverMessageNumericPassword = "";
                break;
            case 'catchRePasswordChange':
                draft.rePasswordValue = action.rePasswordChosen;
                if (action.passwordChosen !== action.rePasswordChosen){
                    draft.passwordReErrors.hasErrors = true
                    draft.passwordReErrors.errorMessage = "passwords must match"
                }else if (action.rePasswordChosen.length === 0 ){
                    draft.passwordReErrors.hasErrors = true
                    draft.passwordReErrors.errorMessage = "This field can't be empty"
                }
                break;
            case 'changeSetRequest':
                draft.sendRequest = draft.sendRequest + 1;
                break;
            case 'catchToken':
                draft.token = action.tokenValue;
                break;
            case "openTheSnack":
                draft.openSnack = true;
                break;
            case "catchUsernameErrors":
                if (action.usernameChosen.length === 0){
                    draft.usernameErrors.hasErrors = true
                    draft.usernameErrors.errorMessage = "This field can't be empty"
                } else if (action.usernameChosen.length < 5){
                    draft.usernameErrors.hasErrors = true
                    draft.usernameErrors.errorMessage = "username must be at least 5 characters"
                } else if (!/^([a-zA-Z0-9]+)$/.test(action.usernameChosen,)){
                    draft.usernameErrors.hasErrors = true
                    draft.usernameErrors.errorMessage = "This field can't have special characters"
                }
                
                break;
            case "catchEmailErrors":
                if (
					!/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/.test(
                        
						draft.emailValue
					)
				) {
					draft.emailErrors.hasErrors = true;
					draft.emailErrors.errorMessage = "Please enter a valid email!";
				}
				
                break;
            case 'catchPasswordErrors':
                if (action.passwordChosen.length === 0){
                    draft.passwordErrors.hasErrors = true
                    draft.passwordErrors.errorMessage = "This field can't be empty"
                } else if (action.passwordChosen.length < 8){
                    draft.passwordErrors.hasErrors = true
                    draft.passwordErrors.errorMessage = "password must be at least 8 characters"
                }
                break;
            case "catchPasswordReErrors":
                
                if (action.passwordChosen !== action.rePasswordChosen){
                    draft.passwordReErrors.hasErrors = true
                    draft.passwordReErrors.errorMessage = "passwords must match"
                }else if (action.rePasswordChosen.length === 0 ){
                    draft.passwordReErrors.hasErrors = true
                    draft.passwordReErrors.errorMessage = "This field can't be empty"
                }
                break;

            case "disableTheButton":
                draft.disabledBtn = true;
                break;
            case "allowTheButton":
                draft.disabledBtn = false;
                break;
            case "usernameExists":
                draft.serverMessageUsername = "This username already exists!";
                break;
    
            case "emailExists":
                draft.serverMessageEmail = "This email already exists!";
                break;
    
            case "similarPassword":
                draft.serverMessageSimilarPassword =
                    "The password is too similar to the username!";
                break;
    
            case "commonPassword":
                draft.serverMessageCommonPassword = "The password is too common!";
                break;
    
            case "numericPassword":
                draft.serverMessageNumericPassword =
                    "The password must not only contain numbers!";
                break;
            default: break;
        }
    }
    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    const handleSubmit = (event) => {
        event.preventDefault();
    
        dispatch({type: 'changeSetRequest'})
        console.log('success');
    };

    useEffect(() => {
		if (state.sendRequest){
            const source = Axios.CancelToken.source();
		async function reg() {
			try {
				const response = await Axios.post('http://127.0.0.1:8000/api-auth-djoser/users/', {
                    username: state.usernameValue,
                    email: state.emailValue,
                    password: state.passwordValue,
                    re_password:state.rePasswordValue
                },{ cancelToken: source.token }
				);
                dispatch({type: 'catchToken', tokenValue: response.data.auth_token})
                Globaldispatch({type: 'catchToken', tokenValue: response.data.auth_token})
                dispatch({type:'openTheSnack'})
			} catch (error) {
                dispatch({type: 'allowTheButton'})
                if (error.response.data.username) {
                    dispatch({ type: "usernameExists" });
                } else if (error.response.data.email) {
                    dispatch({ type: "emailExists" });
                } else if (
                    error.response.data.password[0] === "This password is too common."
                ) {
                    dispatch({ type: "commonPassword" });
                } else if (
                    error.response.data.password[0] ===
                    "This password is entirely numeric."
                ) {
                    dispatch({ type: "numericPassword" });
                }
            }
		}
		reg();
		return () => {
			source.cancel();
		};
	}
        }, [state.sendRequest]);

    useEffect(() => {
        if (state.openSnack) {
            setTimeout(() => {
                navigate("/");
            }, 1500);
        }
    }, [state.openSnack]);

    return (
        <>
            <Navbar/>
            <ThemeProvider theme={theme}>
                <Container component="main" maxWidth="xs">
                    <CssBaseline/>
                    <Box
                        sx={{
                            marginTop: 8,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                        }}
                    >
                        <Avatar sx={{m: 1, bgcolor: 'secondary.main'}}>
                            <LockOutlinedIcon/>
                        </Avatar>
                        <Typography component="h1" variant="h5">
                            Sign up
                        </Typography>
                        <Box component="form" noValidate onSubmit={handleSubmit} sx={{mt: 3}}>
                            <Grid container spacing={2}>
                                <Grid item xs={12} sm={12}>
                                    <TextField
                                        autoComplete="given-name"
                                        name="username"
                                        required
                                        fullWidth
                                        id="username"
                                        label="username"
                                        autoFocus
                                        value={state.usernameValue}
                                        onChange={(event)=>(dispatch({type: 'catchUsernameChange', usernameChosen: event.target.value}))}
                                        onBlur={(event)=>(dispatch({type: 'catchUsernameErrors', usernameChosen: event.target.value}))}
                                        error = {state.usernameErrors.hasErrors ? true : false}
                                        helperText = {state.usernameErrors.errorMessage}
                                    />
                                </Grid>
                                <Grid item xs={12}>
                                    <TextField
                                        required
                                        fullWidth
                                        id="email"
                                        label="Email Address"
                                        name="email"
                                        value={state.emailValue}
                                        onChange={(event)=>(dispatch({type: 'catchEmailChange', emailChosen: event.target.value}))}
                                        onBlur={(event)=>(dispatch({type: 'catchEmailErrors', usernameChosen: event.target.value}))}
                                        error = {state.emailErrors.hasErrors ? true : false}
                                        helperText = {state.emailErrors.errorMessage}
                                        
                                    />
                                </Grid>
                                <Grid item xs={12}>
                                    <TextField
                                        required
                                        fullWidth
                                        name="password"
                                        label="Password"
                                        type="password"
                                        id="password"
                                        value={state.passwordValue}
                                        onChange={(event)=>(dispatch({type: 'catchPasswordChange', passwordChosen: event.target.value}))}
                                        onBlur={(event)=>(dispatch({type: 'catchPasswordErrors', passwordChosen: event.target.value}))}
                                        error = {state.passwordErrors.hasErrors ? true : false}
                                        helperText = {state.passwordErrors.errorMessage}
                                        
                                    />
                                </Grid>
                                <Grid item xs={12}>
                                    <TextField
                                        required
                                        fullWidth
                                        name="password2"
                                        label="Confirm Password"
                                        variant="outlined"
                                        type="password"
                                        id="password2"
                                        value={state.rePasswordValue}
                                        onChange={(event)=>(dispatch({type: 'catchRePasswordChange', rePasswordChosen: event.target.value}))}
                                        helperText = {state.passwordReErrors.errorMessage}
                                        
                                    />
                                </Grid>
                            </Grid>
                            <Button
                                type="submit"
                                fullWidth
                                variant="contained"
                                sx={{mt: 3, mb: 2}}
                            >
                                Sign Up
                            </Button>
                            {GlobalState.globalMessage}
                            <Grid container justifyContent="flex-end">
                                <Grid item>
                                    <Link href="/SignIn" variant="body2">
                                        Already have an account? Sign in
                                    </Link>
                                </Grid>
                            </Grid>
                        </Box>
                    </Box>
                    <Snackbar
                        sx={{marginTop:'3rem'}}
                        severity="success"
                        open={state.openSnack}
                        message="You Logged in"
                        anchorOrigin={{vertical:'top', horizontal:'center'}}
                    />
                </Container>
            </ThemeProvider>
            <Footer/>
        </>
    );
}