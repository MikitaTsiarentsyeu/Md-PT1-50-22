import React from "react";

import Review from '../elements/Review'

//components
import Navbar from '../elements/Navbar';
import Header from '../elements/Header';
import BestOffers from '../elements/BestOffers';
import Footer from '../elements/Footer';




function Home(){
    return(
        <>

            <Navbar/>
            <Header/>
            <BestOffers/>
            <Review/>
            <Footer/>
        </>
    )
}

export default Home;