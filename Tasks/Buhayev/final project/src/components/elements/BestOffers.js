import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardHeader from '@mui/material/CardHeader';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import StarIcon from '@mui/icons-material/StarBorder';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import productCurvyLines from '../../Assets/productCurvyLines.png'
import work1 from '../../Assets/productHowItWorks1.svg'
import work2 from '../../Assets/productHowItWorks2.svg'
import work3 from '../../Assets/productHowItWorks3.svg'
import Container from '@mui/material/Container';
import {styles} from '../elements/utils/Styles'
import {useNavigate} from "react-router-dom";



function ProductHowItWorks() {
  const navigate = useNavigate();
  return (
    <Box
      component="section"
      sx={styles.howItWorks_section}
    >
      <Container
        sx={styles.howItWorks_container}
      >
        
        <Box
          component="img"
          src= {productCurvyLines}
          alt="curvy lines"
          sx={{
            pointerEvents: 'none',
            position: 'absolute',
            top: -180,
            opacity: 0.7,
          }}
        />
        <Typography variant="h4" marked="center" component="h2" sx={{ mb: 14 }}>
          How it works
        </Typography>
        <div>
          <Grid container spacing={5}>
            <Grid item xs={12} md={4}>
              <Box sx={styles.howItWorks_item}>
                <Box sx={styles.howItWorks_number}>1.</Box>
                <Box
                  component="img"
                  src={work1}
                  alt="suitcase"
                  sx={styles.howItWorks_image}
                />
                <Typography variant="h5" align="center">
                  All agencies have the same service
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={4}>
              <Box sx={styles.howItWorks_item}>
                <Box sx={styles.howItWorks_number}>2.</Box>
                <Box
                  component="img"
                  src={work2}
                  alt="graph"
                  sx={styles.howItWorks_image}
                />
                <Typography variant="h5" align="center">
                advantageous offers for both agencies and buyers 
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={4}>
              <Box sx={styles.howItWorks_item}>
                <Box sx={styles.howItWorks_number}>3.</Box>
                <Box
                  component="img"
                  src={work3}
                  alt="clock"
                  sx={styles.howItWorks_image}
                />
                <Typography variant="h5" align="center">
                  {'New offers every week. New experiences, new surprises. '}
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </div>
        <Button
          
          size="large"
          variant="contained"
          component="a"
          sx={styles.main_btn}
          onClick={() => navigate("/listings")}
        >
          Get started
        </Button>
      </Container>
    </Box>
  );
}

export default ProductHowItWorks;