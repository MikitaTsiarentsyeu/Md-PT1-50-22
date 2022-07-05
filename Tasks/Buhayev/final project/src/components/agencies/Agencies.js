import React, { useEffect,  useContext,useState} from 'react';
import {Card, CardActions, CardContent, Stack,  CardMedia, Button, Typography,  CardHeader, Grid,Box} from '@mui/material';
import Axios from "axios";
import {useImmerReducer} from 'use-immer';
import { useNavigate } from "react-router-dom";
import Navbar from '../elements/Navbar';
import Paper from '@mui/material/Paper';
import { styled } from '@mui/material/styles';
import Footer from '../elements/Footer';
import stateContext from '../../Context/StateContext';
import {initialState} from '../elements/utils/InitialState'
import {ReducerFuction} from '../elements/utils/Reducer'
import {styles} from '../elements/utils/Styles'
function Agencies() {
    const navigate = useNavigate();
    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    const GlobalState = useContext(stateContext) 
    const [allProfiles, setAllProfiles] = useState([]);
    const [dataIsLoading, setDataIsLoading] = useState(true);

    useEffect(() => {
		const source = Axios.CancelToken.source();
		async function GetAllListings() {
			try {
				const response = await Axios.get(
					"http://127.0.0.1:8000/api/profiles/",
					{ cancelToken: source.token }
				);

				setAllProfiles(response.data);
				setDataIsLoading(false);
			} catch (error) {}
		}
		GetAllListings();
		return () => {
			source.cancel();
		};
	}, []);
    const Item = styled(Paper)(({ theme }) => ({
        backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
        ...theme.typography.body2,
        padding: theme.spacing(1),
        textAlign: 'center',
        color: theme.palette.text.secondary,
      }));


  return (
    <>
    <Navbar/>
    <Grid container spacing={3}>
    {allProfiles.map((item) =>(
       item.agency_name ?(
        <Grid item xs={6}>
                <Card sx={styles.cardset_card} key={item.id}>
                    <CardHeader title={item.agency_name}/>
                    
                    
                <CardMedia
                    component="img"
                    height= '50%'
                    image = {item.profile_picture}
                    
                />
            
                
                <CardContent>
                    
                    <Stack
                        justifyContent="center"
                        alignItems="center"
                      
                        direction={{ xs: 'column', sm: 'row' }}
                        spacing={{ xs: 1, sm: 2, md: 4 }}
                    >
                        
                        <Item>phone: {item.phone_number}</Item>
                        <Item>listings number: {item.seller_listings.length}</Item>
                        
                    </Stack>
                    <Box sx={{height:'3rem'}}>
                    <Typography variant='body1' sx={styles.cardset_descr}>
                            {item.biography}
                            </Typography></Box>
                </CardContent>
                <CardActions>
                    <Button
                     size="small"
                     onClick={()=>{navigate(`/agencies/${item.seller}`)}}
                     sx={styles.cardset_btn}
                     >More</Button>
                    
                </CardActions>
            </Card>
            </Grid>) : ''
            ))
             }
             </Grid>
                        <Footer/>

    </>
  )
}

export default Agencies