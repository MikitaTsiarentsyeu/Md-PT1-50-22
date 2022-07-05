import React, {useState, useContext} from "react";
import {Link} from "react-router-dom";
import DispatchContext from '../../Context/DispatchContext';
import stateContext from '../../Context/StateContext';
import {styles} from '../elements/utils/Styles'
// MUI imports
import {
    Accordion,
    AccordionSummary,
    AccordionDetails,
    Button,
    Typography,
    Grid,
    AppBar,
    Toolbar,
    Box,
    Menu,
    MenuItem,
    Avatar,
    useMediaQuery
} from "@mui/material";
import MenuIcon from '@mui/icons-material/Menu';
import {useTheme} from '@mui/material/styles';
import {deepOrange, deepPurple} from '@mui/material/colors';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import {useNavigate} from "react-router-dom";
import Axios from 'axios';


function MenuForSmallDisplay() { 

    

    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);
    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };
    const handleClose = () => {
        setAnchorEl(null);
    };

    const handleProfile = () => { 
        setAnchorEl(null);
        navigate('/profile')
 
    }
    const navigate = useNavigate();

    const GlobalState = useContext(stateContext);
    const GlobalDispatch = useContext(DispatchContext);

    return (
        <div>
            <Box sx={{flexGrow: 1, }}>
                <AppBar position="static" sx={styles.navMenuBar} >
                    <Toolbar>
                        <Button onClick={() => navigate("/")}>
                            <Avatar sx={styles.navMenuAvatar}>N</Avatar>
                        </Button>
                        <Button
                            id="basic-button"
                            aria-controls={open ? 'basic-menu' : undefined}
                            aria-haspopup="true"
                            aria-expanded={open ? 'true' : undefined}
                            onClick={handleClick}
                            sx={{
                                color: 'black',
                                textAlign: 'center',
                                margin: '0 auto',
                                position: 'absolute',
                                left: '75%'
                            }}
                        >
                            menu
                        </Button>
                        <Menu
                            id="basic-menu"
                            anchorEl={anchorEl}
                            open={open}
                            onClose={handleClose}
                            MenuListProps={{
                                'aria-labelledby': 'basic-button',
                            }}
                            sx={{position: 'absolute'}}

                        >
                            <MenuItem
                                sx={{backgroundColor: 'black', color: 'blue', '&:hover': {backgroundColor: 'red'}}}
                                onClick={() => navigate("/listings")}>Listings</MenuItem>
                            {GlobalState.userIsLogged ? <MenuItem  color="inherit" sx={{alignSelf: 'end'}} onClick={() => navigate("/newlisting")}>
                                    adding new listing</MenuItem> : <MenuItem color="inherit" sx={{alignSelf: 'end'}} onClick={() => navigate("/SignUp")}>Sign
                                    Up</MenuItem>}
                                    {GlobalState.userIsLogged  ? <MenuItem color="inherit" sx={{alignSelf: 'end'}} onClick={handleClick}>
                                    {GlobalState.userUsername }</MenuItem> : <MenuItem color="inherit" sx={{alignSelf: 'end'}} onClick={() => navigate("/SignIn")}>Sign
                                    In</MenuItem>}
                        </Menu>
                    </Toolbar>
                </AppBar>
            </Box>
        </div>
    );
}


function Query() {
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);
    const GlobalState = useContext(stateContext);
    const GlobalDispatch = useContext(DispatchContext);
    const handleClick = (event) => {

    

      setAnchorEl(event.currentTarget);
    };
    const handleClose = () => {
      setAnchorEl(null);
    };

    const handleProfile = () => { 
        setAnchorEl(null);
        navigate('/profile')
 
    }
    
    async function HandleLogOut (){
        const confirmLogOut = window.confirm('Are you sure you want log out?')
        if (confirmLogOut){
            try {
                setAnchorEl(null);
                const response = await Axios.post('http://127.0.0.1:8000/api-auth-djoser/token/logout/', 
                GlobalState.userToken, 
                {headers: { Authorization: "Token ".concat(GlobalState.userToken) }}
                )
                GlobalDispatch({type:'userLogOut'})
                navigate("/")} catch{
                    console.log('some troble')
                }
        }
        
    }

    const theme = useTheme()
    const display_sm = useMediaQuery(theme.breakpoints.up('sm'));
    const display_md = useMediaQuery(theme.breakpoints.up('md'));
    const display_lg = useMediaQuery(theme.breakpoints.up('lg'));

    const navigate = useNavigate();

    if (display_lg || display_md || display_sm) {
        return (
            <Box sx={{flexGrow: 1}}>
                <AppBar position='relative' sx={styles.navMenuBar}>
                    <Toolbar>
                        <Button onClick={() => navigate("/")}>
                            <Avatar sx={styles.navMenuAvatar}>N</Avatar>
                        </Button>
                        <Grid container direction="row" justifyContent="flex-end" alignItems="center">
                            <Grid item>
                                <Button
                                    color="inherit"
                                    onClick={() => navigate("/listings")}
                                    style={{marginRight: "2rem"}}
                                >
                                    <Typography variant="h6">Properties</Typography>{" "}
                                </Button>
                            </Grid>
                            <Grid item>
                                <Button
                                    color="inherit"
                                    onClick={() => navigate("/agencies")}
                                    style={{marginRight: "2rem"}}
                                >
                                    <Typography variant="h6">Agencies</Typography>{" "}
                                </Button>
                            </Grid>
                            <Grid item>
                                {GlobalState.userIsLogged  ? '' : <Button color="inherit" sx={{alignSelf: 'end'}} onClick={() => navigate("/SignUp")}>Sign
                                    Up</Button>}
                                
                            </Grid>
                            {console.log(GlobalState.data)}
                            <Grid item>
                            {GlobalState.userIsLogged  ? <Button color="inherit" sx={{alignSelf: 'end'}} onClick={handleClick}>
                                    {GlobalState.userUsername }</Button> : <Button color="inherit" sx={{alignSelf: 'end'}} onClick={() => navigate("/SignIn")}>Sign
                                    In</Button>}
                                    <Menu
                                    id="basic-menu"
                                    anchorEl={anchorEl}
                                    open={open}
                                    onClose={handleClose}
                                    MenuListProps={{
                                    'aria-labelledby': 'basic-button',
                                    }}
                                >
                                    <MenuItem onClick={handleProfile}>Profile</MenuItem>
                                    <MenuItem onClick={HandleLogOut}>Logout</MenuItem>
                                </Menu>
                                
                            </Grid>


                        </Grid>

                    </Toolbar>
                </AppBar>
            </Box>
        )
    } else {
        return (<MenuForSmallDisplay/>

        )
    }
}

function Navbar() {
    return Query()
}

export default Navbar