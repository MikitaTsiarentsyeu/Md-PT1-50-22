import React, {useEffect, useContext} from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Snackbar from '@mui/material/Snackbar';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Navbar from '../elements/Navbar';
import Footer from '../elements/Footer';
import { useNavigate } from "react-router-dom";
import Axios from 'axios';
import {useImmerReducer} from 'use-immer';
import DispatchContext from '../../Context/DispatchContext';
import stateContext from '../../Context/StateContext';
import {Alert} from '@mui/material'


const theme = createTheme();

export default function SignIn() {
    const navigate = useNavigate();
  
    const Globaldispatch = useContext(DispatchContext)
    const GlobalState = useContext(stateContext)


    const initialState = { 
        emailValue:'', 
        passwordValue:'', 
        sendRequest:0,
        token:'',
        openSnack: false,
		disabledBtn: false,
		serverError: false,
    }


    
    
    function ReducerFuction(draft, action) {
        switch (action.type) {
            
            case 'catchEmailChange':
                draft.emailValue = action.emailChosen;
                draft.serverError = false;
                break;
            case 'catchPasswordChange':
                draft.passwordValue = action.passwordChosen;
                draft.serverError = false;
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
            case "disableTheButton":
                draft.disabledBtn = true;
                break;
    
            case "allowTheButton":
                draft.disabledBtn = false;
                break;
    
            case "catchServerError":
                draft.serverError = true;
                break;
            default: break;
        }
    }

    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);

    const handleSubmit = (event) => {
        event.preventDefault();
        dispatch({type: 'changeSetRequest'})
        dispatch({ type: "disableTheButton" });
    };
    useEffect(() => {
		if (state.sendRequest ){
            const source = Axios.CancelToken.source();
		async function signin() {
			try {
				const response = await Axios.post('http://127.0.0.1:8000/api-auth-djoser/token/login/', {
                    email: state.emailValue,
                    password: state.passwordValue,
                },{ cancelToken: source.token }
				);
                console.log(response)
                dispatch({type: 'catchToken', tokenValue: response.data.auth_token})
                Globaldispatch({type: 'catchToken', tokenValue: response.data.auth_token})
                // navigate('/')
			} catch (error) {
                dispatch({ type: "allowTheButton" });
				dispatch({ type: "catchServerError" });
            }
		}
		signin();
		return () => {
			source.cancel();
		};
	}
        }, [state.sendRequest]);

    useEffect(() => {
            if (state.token !== '' ){
                const source = Axios.CancelToken.source();
            async function getUserInfo() {
                try {
                    const response = await Axios.get('http://127.0.0.1:8000/api-auth-djoser/users/me/', {
                        headers: {Authorization: 'Token '.concat(state.token)}
                    },{ cancelToken: source.token }
                    );
                    console.log(response)
                    Globaldispatch({type: 'userSignIn', usernameInfo: response.data.username, emailInfo: response.data.email, idInfo: response.data.id})
                    dispatch({type:'openTheSnack'})
                } catch (error) {}
            }
            getUserInfo();
            return () => {
                source.cancel();
            };
        }
            }, [state.token]);

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
                            Sign in
                        </Typography>

                        {state.serverError ? (
					<Alert severity="error">Incorrect username or password!</Alert>
				) : (
					""
				)}

                        <Box component="form" onSubmit={handleSubmit} noValidate sx={{mt: 1}}>
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                id="email"
                                label="Email Address"
                                name="email"
                                autoComplete="email"
                                autoFocus
                                value={state.emailValue}
                                onChange={(event)=>(dispatch({type: 'catchEmailChange', emailChosen: event.target.value}))}
                                error={state.serverError ? true : false}
                            />
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                name="password"
                                label="Password"
                                type="password"
                                id="password"
                                autoComplete="current-password"
                                value={state.passwordValue}
                                onChange={(event)=>(dispatch({type: 'catchPasswordChange', passwordChosen: event.target.value}))}
                                error={state.serverError ? true : false}
                                    
                            />
                            
                            <Button
                                type="submit"
                                fullWidth
                                variant="contained"
                                sx={{mt: 3, mb: 2}}
                            >
                                Sign In
                            </Button>

                            <Grid container>
                                
                                <Grid item>
                                    <Link href="#" variant="body2">
                                        {"Don't have an account? Sign Up"}
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