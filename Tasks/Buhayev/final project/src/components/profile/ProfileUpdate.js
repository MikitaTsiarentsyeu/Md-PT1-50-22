import React, { useEffect, useContext} from 'react';
import {Container,  Button, Typography,  Box,Grid,TextField,} from '@mui/material';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Axios from "axios";
import CssBaseline from '@mui/material/CssBaseline';
import {useImmerReducer} from 'use-immer';
import { useNavigate } from "react-router-dom";
import {styles} from '../elements/utils/Styles';
import Snackbar from '@mui/material/Snackbar';

import stateContext from '../../Context/StateContext';





function ProfileUpdate(props) {
    const theme = createTheme();
    const navigate = useNavigate();
    const initialState = {
		agencyNameValue: props.userProfile.agencyName,
		phoneNumberValue: props.userProfile.phone,
		bioValue: props.userProfile.bio,
		uploadedPicture: [],
		profilePictureValue: props.userProfile.agencyPicture,
		sendRequest: 0,
		openSnack: false,
		disabledBtn: false,
	};
    function FormSubmit(e) {
        e.preventDefault();

        dispatch({ type: "changeSendRequest" });
        dispatch({ type: "disableTheButton" });
    }
	function ReducerFuction(draft, action) {
		switch (action.type) {
			case "catchAgencyNameChange":
				draft.agencyNameValue = action.agencyNameChosen;
				break;

			case "catchPhoneNumberChange":
				draft.phoneNumberValue = action.phoneNumberChosen;
				break;

			case "catchBioChange":
				draft.bioValue = action.bioChosen;
				break;

			case "catchUploadedPicture":
				draft.uploadedPicture = action.pictureChosen;
				break;

			case "catchProfilePictureChange":
				draft.profilePictureValue = action.profilePictureChosen;
				break;

			case "changeSendRequest":
				draft.sendRequest = draft.sendRequest + 1;
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
            default: break;
		}
	}

	const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    const GlobalState = useContext(stateContext) 

    const handleSubmit = (event) => {
        event.preventDefault();
    
		dispatch({type: 'changeRequest', })
        console.log('success');
    };
    


    useEffect(()=>{
		if(state.sendRequest){
			async function updateProfile(){
				const formData = new FormData();

				if (
					typeof state.profilePictureValue === "string" ||
					state.profilePictureValue === null
				) {
					formData.append("agency_name", state.agencyNameValue);
					formData.append("phone_number", state.phoneNumberValue);
					formData.append("biography", state.bioValue);
					formData.append("seller", GlobalState.userId);
				} else {
					formData.append("agency_name", state.agencyNameValue);
					formData.append("phone_number", state.phoneNumberValue);
					formData.append("biography", state.bioValue);
					formData.append("profile_picture", state.profilePictureValue);
					formData.append("seller", GlobalState.userId);
				}
                

				
				
				formData.append("seller", GlobalState.userId);
				try{
					const response = await Axios.patch(`http://127.0.0.1:8000/api/profiles/${GlobalState.userId}/update/`, formData)
					
                    dispatch({ type: "openTheSnack" });
				} catch (e) {
					dispatch({ type: "allowTheButton" });
				}
			}
			updateProfile();
		}
	}, [state.sendRequest])

    useEffect(()=>{
		async function getProfile(){
			try{
				const response = await Axios.get(`http://127.0.0.1:8000/api/profiles/${GlobalState.userId}/`)
				dispatch({type: 'catchUserProfileInfo', profileObj: response.data})
				
			} catch(e){
				console.log(e.response)
			}
		
	}
	getProfile()
	},[])
	useEffect(() => {
		if (state.openSnack) {
			setTimeout(() => {
				navigate("/");
			}, 1500);
		}
	}, [state.openSnack]);

    useEffect(() => {
		if (state.uploadedPicture[0]) {
			dispatch({
				type: "catchProfilePictureChange",
				profilePictureChosen: state.uploadedPicture[0],
			});
		}
	}, [state.uploadedPicture[0]]);
    
    function ProfilePictureDisplay() {
		if (typeof state.profilePictureValue !== "string") {
			return (
				<ul>
					{state.profilePictureValue ? (
						<li>{state.profilePictureValue.name}</li>
					) : (
						""
					)}
				</ul>
			);
		} else if (typeof state.profilePictureValue === "string") {
			return (
				<Grid
					item
					style={{
						marginTop: "0.5rem",
						marginRight: "auto",
						marginLeft: "auto",
					}}
				>
					<img
						src={props.userProfile.agencyPicture}
						style={{ height: "6rem" }}
					/>
				</Grid>
			);
		}
	}
  return (
    <>
    {console.log(props.userProfile.phone_number)}
         <div>
            <Typography variant='h4' sx={styles.update_title}> Update profile information</Typography>
         </div>
         <ThemeProvider theme={theme}>
                <Container component="main" maxWidth="xs" sx={styles.update_main}>
                    <CssBaseline/>
                    <Box
                        sx={{
                            marginTop: 8,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                            
                        }}
                    >
                       
                        <Box component="form" onSubmit={FormSubmit} noValidate  sx={{width:'30rem'}}>
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                id="agency_name"
                                label="Agency name"
                                name="agency"
                                
                                value={state.agencyNameValue}
                                
                                onChange={(event)=>(dispatch({type: 'catchAgencyNameChange', agencyNameChosen: event.target.value }))}
                                
                                    
                            />
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                name="phone"
                                label="phone"
                                type="phone"
                                id="phone"
                                
                                value={state.phoneNumberValue}
                                onChange={(event)=>(dispatch({type: 'catchPhoneNumberChange', phoneNumberChosen: event.target.value }))}
                                    
                            />
                            
                            <TextField
                                sx={{width:'100%'}}
                                multiline
                                rows={6}
                                margin="normal"
                                required
                                fullWidth
                                name="biography"
                                label="biography"
                                id="biography"
                                
                                value={state.bioValue}
                                onChange={(event)=>(dispatch({type: 'catchBioChange', bioChosen: event.target.value }))}
                                    
                            />
                            
                                    
                            <Box component='div' sx = {{margin:'0 auto', textAlign: 'center'}}>
                            <hr/>
                            <Box>
                            {ProfilePictureDisplay()}
                            </Box>
							<hr/>
                            <Button
							variant="contained"
							component="label"
							sx={styles.agency_btn}
							fullWidth
							
						>
							PROFILE PICTURE
							<input
								type="file"
								accept="image/png, image/gif, image/jpeg"
								hidden
								onChange={(e) =>
									dispatch({
										type: "catchUploadedPicture",
										pictureChosen: e.target.files,
									})
								}
							/>
						</Button>
                            </Box>
							<hr/>
						<Button
							variant="contained"
							fullWidth
							type="submit"
							sx={styles.agency_btn}
							disabled={state.disabledBtn}
						>
							UPDATE
						</Button>
						<hr/>
                        </Box>
                    </Box>
					<Snackbar
				open={state.openSnack}
				message="Listing succsesfully updated"
				anchorOrigin={{
					vertical: "bottom",
					horizontal: "center",
				}}
			/>
                </Container>
            </ThemeProvider>
    </>
  )
}

export default ProfileUpdate