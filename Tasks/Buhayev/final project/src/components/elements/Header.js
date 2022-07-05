import {
   
    Typography,
   
    Box,
   
    useMediaQuery
} from "@mui/material";

import {useTheme} from '@mui/material/styles';
import {Link, useNavigate} from "react-router-dom";
import {styles} from '../elements/utils/Styles'
import backgroundCity from '../../Assets/city.jpg'

function Header() {
    const theme = useTheme()
    const display_sm = useMediaQuery(theme.breakpoints.up('sm'));
    const display_md = useMediaQuery(theme.breakpoints.up('md'));
    const display_lg = useMediaQuery(theme.breakpoints.up('lg'));


    if (display_lg || display_md || display_sm) {
        return (
            <>
                <Box component='header' sx={styles.header_container}>
                    <Typography variant="h1" align='center' sx={
                       styles.header_title
                    }>
                        Your apartments
                    </Typography>
                    <Typography variant="h1" align='center' sx={
                       styles.header_subtitle
                    }>
                        our concern
                    </Typography>
                </Box>
               

                
            </>
        )
    } else {
        return (
            <>
                <Box component='header'>
                    <Typography variant="h1" align='center' sx={{
                        fontSize: '4rem',
                        color: '#fff',
                        letterSpacing: '.5rem',
                        pt: '10rem',
                        height: '60vh',
                        backgroundSize: 'cover',
                        backgroundImage: `url(${backgroundCity})`
                    }}>
                        Geoproject
                    </Typography>

                </Box>
                <Box sx={{height: '12vh', width: '100%', backgroundColor: '#000'}}>

                </Box>
            </>
        )
    }
}

export default Header