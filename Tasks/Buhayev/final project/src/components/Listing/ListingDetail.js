import React, { useEffect, useState, useContext} from 'react';
import {Container,  Typography,Link,  Box,Grid,Breadcrumbs, Button, } from '@mui/material';

import Axios from "axios";
import {useImmerReducer} from 'use-immer';
import { useNavigate,useParams } from "react-router-dom";
import Navbar from '../elements/Navbar';
import {Item} from '../elements/utils/Item'
import Footer from '../elements/Footer';
import Dialog from '@mui/material/Dialog';
import ListingUpdate from './components/ListingUpdate'

import { MapContainer, TileLayer, useMap, Marker,Popup,Polygon } from 'react-leaflet'
import stateContext from '../../Context/StateContext';
import {styles} from '../elements/utils/Styles'

import {initialState} from '../elements/utils/InitialState'
import {ReducerFuction} from '../elements/utils/Reducer'

function ListingDetail() {
   
    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    const navigate = useNavigate();
    const GlobalState = useContext(stateContext) 
    const params = useParams()
    const [open, setOpen] = useState(false);
    
    const handleClickOpen = () => {
        setOpen(true);
      };
    
      const handleClose = () => {
        setOpen(false);
      };
    
    useEffect(()=>{
		async function getListingDetail(){
			try{
				const response = await Axios.get(`http://127.0.0.1:8000/api/listings/${params.id}/`)
                console.log(response.data)
				dispatch({type: 'catchListingInfo', listingObject: response.data})
			} catch(e){
				console.log(e.response)
			}
		
	}
	getListingDetail()
	},[])

    useEffect(() => {
		if (state.listingInfo) {
			async function GetProfileInfo() {
				try {
					const response = await Axios.get(
						`http://127.0.0.1:8000/api/profiles/${state.listingInfo.seller}/`
					);
                        
					dispatch({
						type: "catchSellerProfileInfo",
						profileObject: response.data,
					});
					dispatch({ type: "loadingDone" });
				} catch (e) {}
			}
			GetProfileInfo();
		}
	}, [state.listingInfo]);

    async function deleteListing(){
        let confirmDelete = window.confirm('Are you sure you want to delete?')
        if (confirmDelete){
        try{
            const response = await Axios.delete(`http://127.0.0.1:8000/api/listings/${params.id}/delete/`)
            navigate('/listings');
        } catch(e){
            console.log(e.response)
        }}
    }



    let position = [state.listingInfo.latitude, state.listingInfo.longitude]
    let price = 0
    if(state.listingInfo.property_status === 'Sale'){
        price = `price: $${state.listingInfo.price}`
    } else { price = `price: $${state.listingInfo.price} per ${state.listingInfo.rental_frequency}`}

    let cctv = 0
    if(state.listingInfo.cctv){
        cctv = 'cctv: yes'
    }else{ cctv = 'cctv: no' }

    let elevator = 0
    if(state.listingInfo.elevator){
        elevator = 'elevator: yes'
    }else{ elevator = 'elevator: no' }

    let parking = 0
    if(state.listingInfo.parking){
        parking = 'parking: yes'
    }else{ parking = 'parking: no' }

    let pool = 0
    if(state.listingInfo.pool){
        pool = 'pool: yes'
    }else{ pool = 'pool: no' }




    if(state.listingInfo.latitude){

    
  return (
    
    <>
    <Navbar/>
    <Box >
        <Breadcrumbs aria-label="breadcrumb">
            <Link underline="hover" color="inherit" onClick={()=>navigate('/listings/')}>
                listings
            </Link>
            <Typography color="text.primary">{state.listingInfo.title}</Typography>
        </Breadcrumbs>
    </Box>
    <Grid container spacing={12} sx={styles.cardset_box} alignItems="center">
        <Grid item xs={9}><Typography variant='h2' sx={styles.listing_detail_title}>{state.listingInfo.title}</Typography></Grid>
        {parseInt(GlobalState.userId) === state.listingInfo.seller ? (<Grid item xs={3}>
                    
                    <Button variant="contained" sx={styles.agency_btn} onClick={deleteListing}>delete</Button>
                   
                        <Button variant="contained" onClick={handleClickOpen} sx={styles.agency_btn}>
                            Update
                        </Button>
                        <Dialog open={open} onClose={handleClose} sx={{margin:'0 auto'}}>
                            <ListingUpdate listingData={state.listingInfo} />
                        </Dialog>
               
                </Grid>) : ''}
       
    </Grid>
    <hr style={{width: '60%', backgroundColor:'#efefef', borderColor:'rgb(239, 239, 239, 0.3)'}}/>
    
    
    <Grid container>
        <Grid item xs={6}><Container fixed>
            <Box sx={{height: '57vh', backgroundColor: 'red', margin: '0 auto', mt: 2, }}>
                <MapContainer center={position} zoom={13} scrollWheelZoom={true}>
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                        
                        
                        <Marker key={state.listingInfo.id} position={position}>
                         <Popup>
                             <Typography variant='h5' sx={{fontSize: '1.2rem'}}>{state.listingInfo.title}</Typography>
                            <img src={state.listingInfo.picture} alt={'picture'}style={{width: '100%', height: 'auto'}}/>
                            <Typography variant='body1' sx={{m: 0, fontSize: '.7rem'}}>
                            {state.listingInfo.description}
                            </Typography>
                            
                        </Popup>
   
                        </Marker>
                   
                </MapContainer>

            </Box>
            </Container>
            <Typography sx={styles.listing_detail_description}><Typography variant='h6' sx={styles.listing_detail_info}>description:</Typography><br></br>{state.listingInfo.description}</Typography></Grid>
        <Grid item xs={6} alignItems="flex-start" sx={{pt:'1rem'}}>
            <Container>
            <Box component='div' sx={{textAlign:'center'}} >
                <img src={state.listingInfo.picture} style={{width:'85vh'}}/>
            </Box>
            <Typography variant='h6' sx={styles.listing_detail_info}>Agency info:</Typography>
            <Grid container spacing={2} sx={{mt:'1rem'}}>
                
                <Grid item xs={6}>
                
                <Item key={state.listingInfo.id} elevation={4} sx={styles.listing_detail_agency} onClick={()=>{navigate(`/agencies/${state.sellerProfileInfo.seller}`)}}>
                  {`Agency: ${state.listingInfo.seller_agency_name}`}
                </Item>
                
                </Grid>
               
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                {`Phone: ${state.sellerProfileInfo.phone_number}`}
                </Item>
                </Grid>
               
                
            </Grid>
                    <Typography variant='h6' sx={styles.listing_detail_info}>Main info:</Typography>
            <Grid container spacing={2} sx={{mt:'1rem'}}>
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                  {`rooms: ${state.listingInfo.rooms}`}
                </Item>
                
                </Grid>
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                  {price}
                </Item>
                </Grid>
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                  {cctv}
                </Item>
                </Grid>
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                  {elevator}
                </Item>
                </Grid>
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                  {parking}
                </Item>
                </Grid>
                <Grid item xs={6}>
                <Item key={state.listingInfo.id} elevation={4}>
                  {pool}
                </Item>
                </Grid>
            </Grid>
            </Container>
        </Grid>
        
    </Grid>
    <Footer/>
    </>
  )
}}

export default ListingDetail