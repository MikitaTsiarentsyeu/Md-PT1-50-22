import React, {useState, useEffect} from 'react';
import {Card, CardActions, CardContent, CardMedia, Button, Typography, CardHeader,Box} from '@mui/material';
import Stack from '@mui/material/Stack';
import Axios from "axios";
import { useNavigate } from "react-router-dom";
import {Item} from '../../elements/utils/Item'
import {styles} from '../../elements/utils/Styles'

export default function ImgMediaCard() {

    const navigate = useNavigate();




    

    const [allListings, setAllListings] = useState([]);
    const [dataIsLoading, setDataIsLoading] = useState(true);

	useEffect(() => {
		const source = Axios.CancelToken.source();
		async function GetAllListings() {
			try {
				const response = await Axios.get(
					"http://127.0.0.1:8000/api/listings/",
					{ cancelToken: source.token }
				);

				setAllListings(response.data);
				setDataIsLoading(false);
			} catch (error) {}
		}
		GetAllListings();
		return () => {
			source.cancel();
		};
	}, []);
    return (
        <>  
            {allListings.map((item) =>(
                <Card sx={styles.cardset_card} key={item.id}>

                    <CardHeader
                            sx={styles.cardset_cardheader}
                            title={item.title}
                           
                        />
                    
                <CardMedia
                    component="img"
                    height= '40%'
                    image = {item.picture}
                    
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
                    <Box sx={{height:'3rem'}}>
                    <Typography variant='body1' sx={styles.cardset_descr}>
                            {item.description}
                            </Typography>
                    </Box>
                    
                </CardContent>
                <CardActions>
                    <Button size="small"
                    onClick={()=>{navigate(`/listings/${item.id}`)}} sx={styles.cardset_btn}>More</Button>
                    <Button 
                        size="small" 
                        onClick={()=>{navigate(`/agencies/${item.seller}`)}} sx={styles.cardset_btn}>Seller</Button>
                    
                </CardActions>
            </Card>
            ))
             }


        </>
    );
}