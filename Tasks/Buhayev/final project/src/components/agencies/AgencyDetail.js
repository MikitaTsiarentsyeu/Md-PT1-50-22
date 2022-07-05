import React, { useEffect, useContext} from 'react';
import {Card, CardActions, CardContent, CardMedia, Button, Typography,  Box, CardHeader,Stack, Grid} from '@mui/material';
import {createTheme} from '@mui/material/styles';
import Axios from "axios";
import {useImmerReducer} from 'use-immer';
import { useNavigate, useParams } from "react-router-dom";
import Navbar from '../elements/Navbar';
import Footer from '../elements/Footer'
import {styles} from '../elements/utils/Styles'
import {Item} from '../elements/utils/Item'



import stateContext from '../../Context/StateContext';

import {initialState} from '../elements/utils/InitialState'
import {ReducerFuction} from '../elements/utils/Reducer'


function AgencyDetail(props) {
    const theme = createTheme();
    const navigate = useNavigate();
    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    const GlobalState = useContext(stateContext) 
    const params = useParams()

    const handleSubmit = (event) => {
        event.preventDefault();
    
		dispatch({type: 'changeRequest', })
        console.log('success');
    };

    


    useEffect(()=>{
		async function getProfile(){
			try{
				const response = await Axios.get(`http://127.0.0.1:8000/api/profiles/${params.id}/`)
				dispatch({type: 'catchUserProfileInfo', profileObj: response.data})
			} catch(e){
				console.log(e.response)
			}
		
	}
	getProfile()
	},[])

    useEffect(()=>{
        if(state.uploadedPictureProfileValue[0]){
            dispatch({type: 'catchProfilePicture', profilePictureChosen: state.uploadedPictureProfileValue[0]})

        }

    },[state.uploadedPictureProfileValue[0]])
  return (<>
  
  <Navbar/>
  <Typography variant='h4' sx={styles.listing_detail_title}>{state.userProfile.agencyName}</Typography>
  <hr style={{width: '60%', backgroundColor:'#efefef', borderColor:'rgb(239, 239, 239, 0.3)'}}/>
                <Grid container   justifyContent="space-around">
                    <Grid item sx={4}>
                    <Box  sx={{marginLeft: '5rem'}} >

                        <img src={state.userProfile.agencyPicture} style = {{width:'30rem', marginRight:'3rem', marginTop:'1rem'}}/>
                    </Box>

                    </Grid>
                    <Grid item xs={6}>
                    <Box  sx={{marginLeft: '5rem', marginTop: '1rem'}}>
                        <Typography variant='h4'>Phone:</Typography>
                            <p> {state.userProfile.phone}</p>
                            <Typography variant='h4'>Description:</Typography>
                            <p style={{textAlign: 'justify'}}>{state.userProfile.bio}</p>
                    </Box>
                    </Grid>
                    </Grid>
                    <hr style={{width: '60%', backgroundColor:'#efefef', borderColor:'rgb(239, 239, 239, 0.3)'}}/>
                   <Grid container spacing={12}>

                    {state.userProfile.sellerListings.length>0 ? state.userProfile.sellerListings.map((item) =>(
                        <Grid item xs={4}>
                <Card sx={styles.cardset_card_widther} key={item.id}>

                    <CardHeader
                            
                            title={item.title}
                           
                       sx={{height: '2rem'}} />
                    
                <CardMedia
                    component="img"
                    height= '40%'
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
                    <Button size="small" sx={styles.cardset_btn} onClick={()=>{navigate(`/listings/${item.id}`)}}>More</Button>
                  
                    
                </CardActions>
            </Card>
            </Grid>
            ))
            
             : ''}
             
             </Grid>
             <Footer/>
    </>
  )
}

export default AgencyDetail