import React, { useEffect, useRef, useMemo, useContext,useState} from 'react';
import {  Button, Card,  Box,Grid,TextField,CardContent,Typography,Snackbar} from '@mui/material';
import {useImmerReducer} from 'use-immer';
import { useNavigate } from "react-router-dom";
import Axios from "axios";
import stateContext from '../../Context/StateContext';
import Carousel from 'react-material-ui-carousel'
import {styles} from './utils/Styles'

function Review() {

    const navigate = useNavigate();
    const initialState = {
        review:'',
        sendRequest:0,
        openSnack: false
    };
    const [dataIsLoading, setDataIsLoading] = useState(true);
    const [allReviews, setallReviews] = useState([]);
    const GlobalState = useContext(stateContext);
    function ReducerFuction(draft, action){
        switch (action.type) {
            case 'catchReview': 
                draft.review = action.reviewChosen;
                break;
            case 'changeSetRequest':
                draft.sendRequest = draft.sendRequest + 1;
                break;
            case 'ReviewList': 
                draft.reviewList = action.reviewCatch
                break
            case "openTheSnack":
                draft.openSnack = true;
                break;
            default: break
        }
    }
    const handleSubmit = (event) => {
        event.preventDefault();
        dispatch({type: 'changeSetRequest'})
        dispatch({ type: "disableTheButton" });
    };

    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
    useEffect(()=>{
		if(state.sendRequest){
			async function AddReview(){
				const formData = new FormData();
					formData.append("user_name", GlobalState.userUsername);
					formData.append("review", state.review);
					
				try{
					const response = await Axios.post('http://127.0.0.1:8000/api/reviews/create/', formData)
					console.log(response.data);
					
					dispatch({type:'openTheSnack'})
					console.log(state.openSnack)
					
				}catch(e){
					
				}
			}
			AddReview();
            
		}
	}, [state.sendRequest])


    useEffect(()=>{
        const source = Axios.CancelToken.source();
		async function getReviews(){
			try{
				const response = await Axios.get(`http://127.0.0.1:8000/api/reviews/`,{ cancelToken: source.token })
				setallReviews(response.data);
                setDataIsLoading(false);
			} catch(e){
				console.log(e.response)
			}
		
	}
	getReviews();
    return () => {
        source.cancel();
    };
	},[])
    let isReview =  false
    function is_Review(){ 
        for (let i of allReviews){
            if (i.user_name === GlobalState.userUsername){
                isReview = true
            }
        }
    }
    is_Review()
    useEffect(() => {
        if (state.openSnack) {
            setTimeout(() => {
                window.location.reload()
            }, 1500);
        }
    }, [state.openSnack]);
  return (
   <>
   <Box sx={styles.review_box}>
    <Typography variant="h4" sx={styles.review_title}>What users said about us</Typography>
   <Carousel sx={{mt:'1rem', }}>
        {allReviews.map((item)=>(
            <Card sx={styles.review_card} key={item.id}>
                <CardContent>
                <Typography sx={styles.review_name} color="text.secondary" gutterBottom>
          {item.user_name}:
          
        </Typography>
        <Typography sx={styles.review_comment} color="text.secondary" gutterBottom>
          {item.review}
          
        </Typography>
                </CardContent>
            </Card>
        ))}
        </Carousel>

   
   {!isReview && GlobalState.userUsername?
   (
   <Grid container sx={{mt:"2rem"}}>
    <Grid item xs={6}>
        <Typography variant="h3" sx={styles.review_title}>
            Please 
        </Typography>
        <Typography variant="h4" sx={styles.review_title}>add your opinion about our site!</Typography>
    </Grid>
    <Grid item xs={6}>
   <Box component="form" noValidate   onSubmit={handleSubmit} sx={{mt: 3}}>
        <TextField
            sx={{width:'40rem'}}
			multiline
            rows={6}
            name="description"
            required
            id="description"
            label="description"
            value={state.review}
            onChange={(event)=>(dispatch({type: 'catchReview', reviewChosen: event.target.value}))}/>
            
                {state.review?(
                    <Box sx={{m:'0 auto'}}>
                        <Button
                            type="submit"
                            variant="contained"
                            sx={styles.review_btn}>
                                Submit
		                </Button>
                    </Box>
                ): (<Box sx={{m:'0 auto'}}>
                <Button
                    disabled
                    type="submit"
                    variant="contained"
                    sx={styles.review_btn}>
                        Submit
                </Button>
            </Box>)}
            
    </Box></Grid></Grid>) : ''
}
<Snackbar
                        sx={{marginTop:'3rem'}}
                        severity="success"
                        open={state.openSnack}
                        message="You Logged in"
                        anchorOrigin={{vertical:'top', horizontal:'center'}}
                    />
                    </Box>
</>
  )
}

export default Review