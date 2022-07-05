import React from 'react';
import {Card, CardActions, CardContent, CardMedia, Button, Typography, useMediaQuery, Grid,Container} from '@mui/material';
import { useTheme } from '@mui/material/styles';
import Map from "./Map";
import CardSet from "./CardSet";



export default function MapSet() {
    const theme = useTheme()
    const display_md = useMediaQuery(theme.breakpoints.up('md'));
    const display_lg = useMediaQuery(theme.breakpoints.up('lg'));

      if(display_lg || display_md) {
         return (
         
         <Grid container spacing={3} justifyContent="center" alignItems="flex-start">
                <Grid item md={6} xs={6} lg={6} >
                    
                    <Map/>
    
                    
                </Grid>
                <Grid item md={6} xs={6} lg={6} >
                <Container sx = {{overflowY: 'scroll', height:'90vh', margin:'0', padding:'0'}}>
                    <CardSet/>
                    </Container>
                </Grid>
            </Grid>
            
         )}else{
          return <CardSet/>
      };
}