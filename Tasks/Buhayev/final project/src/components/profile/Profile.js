import React, { useEffect, useState, useContext} from 'react';
import {Container,  Button, Typography,  Box,Grid,TextField,Card, CardActions, CardContent, CardMedia,Stack,CardHeader} from '@mui/material';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Axios from "axios";
import CssBaseline from '@mui/material/CssBaseline';
import {useImmerReducer} from 'use-immer';
import { useNavigate } from "react-router-dom";
import Navbar from '../elements/Navbar';
import Dialog from '@mui/material/Dialog';
import ProfileUpdate from './ProfileUpdate'
import stateContext from '../../Context/StateContext';
import {Item} from '../elements/utils/Item'
import {initialState} from '../elements/utils/InitialState'
import {ReducerFuction} from '../elements/utils/Reducer'
import {styles} from '../elements/utils/Styles'


function Profile() {
    const theme = createTheme();
    const navigate = useNavigate();
    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    const GlobalState = useContext(stateContext) 

    const handleSubmit = (event) => {
        event.preventDefault();
    
		dispatch({type: 'changeRequest', })
        console.log('success');
    };

    const [open, setOpen] = useState(false);
    
    const handleClickOpen = () => {
        setOpen(true);
      };
    
      const handleClose = () => {
        setOpen(false);
      };

    useEffect(()=>{
		if(state.sendRequest){
			async function updateProfile(){
				const formData = new FormData();
					formData.append("agency_name", state.agencyNameValue);
					formData.append("phone_number", state.phoneValue);
					formData.append("biography", state.bioValue);
					formData.append("profile_picture", state.profilePicture);
					formData.append("seller", GlobalState.userId);
				try{
					const response = await Axios.patch(`http://127.0.0.1:8000/api/profiles/${GlobalState.userId}/update/`, formData)
                    
					navigate('/')
				}catch(e){
					console.log('error')
				}
			}
			updateProfile();
		}
	}, [state.sendRequest])

    useEffect(()=>{
		async function getProfile(){
			try{
				const response = await Axios.get(`http://127.0.0.1:8000/api/profiles/${GlobalState.userId}/`)
				console.log(response.data)
				console.log(state)
				dispatch({type: 'catchUserProfileInfo', profileObj: response.data})
			} catch(e){
				console.log(e.response)
			}
		
	}
	getProfile()
	},[])
    console.log(state.sellerProfileInfo)
    useEffect(()=>{
        if(state.uploadedPictureProfileValue[0]){
            dispatch({type: 'catchProfilePicture', profilePictureChosen: state.uploadedPictureProfileValue[0]})

        }

    },[state.uploadedPictureProfileValue[0]])
    console.log(state.userProfile)
    function WelcomeDisplay(){
        if (!state.userProfile.agencyName || !state.userProfile.phone ){
            return (<><Typography variant='h4' sx={{textAlign: 'center', marginTop:'2rem'}}>Welcome <span style={{color: '#ed6b04'}}>{GlobalState.userUsername}</span>, please adding information in your profile</Typography> 
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
                       
                        <Box component="form" onSubmit={handleSubmit} noValidate sx={{mt: 1, width:'40rem'}}>
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                id="agency_name"
                                label="Agency name"
                                name="agency"
                                
                                
                                value={state.agencyNameValue}
                                onChange={(event)=>(dispatch({type: 'catchAgencyNameChange', agencyNameChosen: event.target.value}))}
                                    
                            />
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                name="phone"
                                label="phone"
                                type="phone"
                                id="phone"
                                
                                value={state.phoneValue}
                                onChange={(event)=>(dispatch({type: 'catchPhoneChange', phoneChosen: event.target.value}))}
                                    
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
                                onChange={(event)=>(dispatch({type: 'catchBioChange', bioChosen: event.target.value}))}
                                    
                            />
                            
                                    
                            <Box component='div' sx = {{margin:'0 auto', textAlign: 'center'}}>
                                <Button
                                    fullWidth
                                    component='label'
                                    variant="contained"
                                    sx={{textAlign:'center',mt: 3, mb: 2, width:'30%'}}
                                >
                                    <input type='file' accept="image/png, image/jpeg, image/gif" hidden onChange={(event)=>(dispatch({type: 'catchPictureProfileChange', pictureProfileChosen: event.target.files}))}/>
                                    upload profile image
                                </Button>
                                <Box component='div'>
									{state.profilePicture ? <p>{state.profilePicture.name}</p> : ''}
								</Box>
                            </Box>
                            <Button
                                type="submit"
                                fullWidth
                                variant="contained"
                                sx={{mt: 3, mb: 2}}
                            >
                                Submit
                            </Button>

                        </Box>
                    </Box>

                </Container>
            </ThemeProvider>
           
            </>)
        } else {
            return (<> <Grid container sx={styles.agency_btn_box} 
            alignItems="center" justifyContent="space-around" spacing={12}>
                <Grid item xs={8}><Typography variant='h4' sx={styles.listing_detail_title}>{state.userProfile.agencyName}</Typography></Grid>
                                  <Grid item xs={1}>
                                      <Button variant="contained" onClick={handleClickOpen} sx={styles.agency_btn}>
                                              Update
                                          </Button>
                                  </Grid>
                                  <Grid item xs={3}>
                                  <Button variant="contained" sx={{mt: '42px'}} color="inherit"   onClick={() => navigate("/newlisting")}>
                                              adding new listing</Button>
          
                                              </Grid>
                                 
                                  </Grid>
            
            <hr style={{width: '60%', backgroundColor:'#efefef', borderColor:'rgb(239, 239, 239, 0.3)'}}/>
                    
            <Grid container   justifyContent="space-around">
            <Grid item sx={4}>
                    <Box  sx={{marginLeft: '5rem'}} >
                        <img src={state.userProfile.agencyPicture} style = {{width:'20rem', marginRight:'3rem', marginTop:'1rem'}}/>
                    </Box>
                    </Grid>
                    <Grid item xs={6}>
                    <Box  sx={{marginLeft: '5rem'}}>
                        <Typography variant='h4'>Phone:</Typography>
                            <p> {state.userProfile.phone}</p>
                            <Typography variant='h4'>Description:</Typography>
                            <p>{state.userProfile.bio}</p>
                    </Box>
                    </Grid>
                    </Grid>
                    <hr style={{width: '60%', backgroundColor:'#efefef', borderColor:'rgb(239, 239, 239, 0.3)'}}/>
                   
                        <Dialog open={open} onClose={handleClose} sx={{margin:'0 auto'}}>
                            <ProfileUpdate userProfile={state.userProfile} />
                        </Dialog>

                        <Grid container>

{state.userProfile.sellerListings.length>0 ? state.userProfile.sellerListings.map((item) =>(
    <Grid item xs={4}>
<Card sx={{width:'94%',height:'70vh', margin: '0 auto', mt: 2}} key={item.id}>

<CardHeader
        
        title={item.title}
       
    />

<CardMedia
component="img"
alt="green iguana"
height= '50%'
image = {`http://127.0.0.1:8000${item.picture}`}

/>


<CardContent>

<Stack
    justifyContent="center"
    alignItems="center"
  
    direction={{ xs: 'column', sm: 'row' }}
    spacing={{ xs: 1, sm: 2, md: 4 }}
>
    <Item>{item.property_status} </Item>
    <Item>price &#36;: {item.property_status ==='Sale' ? item.price : item.price + ' per ' + item.rental_frequency} </Item>
    <Item>rooms: {item.rooms}</Item>
    <Item>agency: {item.seller_agency_name}</Item>
</Stack>
<Typography variant='body1' sx={{m: 0, fontSize: '.7rem'}}>
        {item.description}
        </Typography>
</CardContent>
<CardActions>
<Button size="small" onClick={()=>{navigate(`/listings/${item.id}`)}}>More</Button>


</CardActions>
</Card>
</Grid>
))

: ''}

</Grid>
                               
                
            </>)
        }
    }

  return (
    <>
         <Navbar/>
         <div>
            {WelcomeDisplay()}
         </div>
         
         
    </>
  )
}

export default Profile