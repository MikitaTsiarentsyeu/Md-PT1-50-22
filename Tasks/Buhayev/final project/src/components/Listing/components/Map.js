import React, {useState, useEffect} from 'react';
import {MapContainer, TileLayer, Marker, Popup, } from 'react-leaflet'
import {useTheme} from '@mui/material/styles';
import {
    Typography,
    Box,
    useMediaQuery, Button,List,ListItem,Container
} from "@mui/material";
import Axios from "axios";
import ImgMediaCard from "./CardSet"
import { useNavigate } from "react-router-dom";





function Map() {
    // fetch('http://127.0.0.1:8000/api/listings/').then(response=>response.json()).then(data=>console.log(data))
    const [allData, setAllData] = useState([]);
	const navigate = useNavigate();
    const [latitude, setLatitude] = useState(52.24919907014026)
    const [longitude, setLongitude] = useState(21.021662057671257)
    const theme = useTheme()
    const display_sm = useMediaQuery(theme.breakpoints.up('sm'));
    const display_md = useMediaQuery(theme.breakpoints.up('md'));
    const display_lg = useMediaQuery(theme.breakpoints.up('lg'));

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
    console.log(allListings[0])

    if (display_lg || display_md || display_sm) {
        return (
            <Container fixed>
            <Box sx={{height: '90vh', backgroundColor: 'red', margin: '0 auto', mt: 2, }}>
                <MapContainer center={[51.50886487942717, -0.1289925026760254]} zoom={13} scrollWheelZoom={false}>
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    {allListings.map((item)=>(
                        <Marker key={item.id} position={[item.latitude, item.longitude]}>
                         <Popup>
                             <Typography variant='h5' sx={{fontSize: '1.2rem'}}>{item.title}</Typography>
                            <img src={item.picture} alt={'picture'}style={{width: '100%', height: 'auto'}}/>
                            <Typography variant='body1' sx={{m: 0, fontSize: '.7rem'}}>
                            {item.description}
                            </Typography>
                            <Button variant='contained' fullWidth sx={{padding: '.3rem'}} onClick={()=>{navigate(`/listings/${item.id}`)}}>more</Button>
                        </Popup>
   
                        </Marker>
                    ))}
                </MapContainer>
            </Box>
            </Container>
        )
    } else {
        return (
            <Container fixed>
            <Box sx={{width: '100%', height: '60vh', backgroundColor: 'red', mt: '4rem'}}>
                <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    {allListings.map((item)=>(
                    <Marker key={item.id} position={[item.latitude, item.longitude]}>
                        <Popup>
                            <Typography variant='h5'>Title</Typography>
                            <img src={item.picture} sx={{width: '100%'}}/>
                        </Popup>
                    </Marker>))}

                </MapContainer>
            </Box>
            </Container>
        )
    }
}

export default Map
