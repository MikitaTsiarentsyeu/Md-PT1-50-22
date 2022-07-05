import React, { useState } from "react";
import Navbar from '../elements/Navbar';
import MapSet from "../Listing/components/MapSet";
import Footer from '../elements/Footer';
import {Typography, } from '@mui/material';


function Listings(){
    return(
        <>

            <Navbar/>
            <Typography variant="h1" sx={{fontFamily:'Uduntu', textAlign: 'center', md:3}}>All Listings</Typography>
            <hr style={{width: '60%', backgroundColor:'#efefef', borderColor:'rgb(239, 239, 239, 0.3)'}}/>
            <MapSet/>
            <Footer/>
        </>
    )
}

export default Listings;