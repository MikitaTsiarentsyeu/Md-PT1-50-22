import backgroundCity from '../../../Assets/back.jpeg'

export const styles ={
    main_btn:{
        mt: 8, 
        bgcolor:'#596475', 
        '&:hover':{bgcolor:'#1F2232', 
        transition:'all 1s'
    }},
    navMenuBar:{
        backgroundColor:'#596475',
        
    },
    navMenuAvatar:{
        backgroundColor: '#464F5D',
    },
    header_container:{ 
        backgroundImage: `url(${backgroundCity})`,
        width: '100%',
        height: '90vh',
        backgroundSize: 'cover',
        borderBottom:'10px solid #777'},
    header_title: {
        pt:'3rem',
        '@keyframes moveInLeft': {
            '0%': {
              opacity: '0',
              transform: 'translateY(3rem)', },
            '80%': {
              transform: 'translateY(1rem)' },
            '100%': {
              opacity: '1',
              transform: 'translate(0)', } },
        animation:`moveInLeft 1s ease-out`,
        fontSize: '6rem',
        color: '#fff',
        letterSpacing: '.3rem',
        textShadow:'0.5rem 1rem 2rem rgba(255, 250, 255, 0.4)',
        
    },
    header_subtitle:{ 
        fontSize: '7rem',
        color: '#fff',
        letterSpacing: '.3rem',
        '@keyframes moveInRight': {
            '0%': {
              opacity: '0',
              transform: 'translateX(10rem)' },
            '80%': {
              transform: 'translateX(-1rem)' },
            '100%': {
              opacity: '1',
              transform: 'translate(0)' } },

              animation:'moveInRight 1s ease-out',
    },
    howItWorks_section:{display: 'flex', bgcolor: '#FDE8E9', overflow: 'hidden' },
    howItWorks_container:{
        mt: 10,
        mb: 15,
        position: 'relative',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    howItWorks_number:{
        fontSize: 24,
        fontFamily: 'default',
        color: '#596475',
        fontWeight: 'medium',
    },
    howItWorks_item:{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        px: 5,
    },
    howItWorks_image:{ 
        height: 55,
        my: 4,
    },

    review_box:{
        
        backgroundColor:'#FFFBFC',
        pb:'2rem'
    },
    review_title:{ 
        textAlign: 'center', 
        pt:'2rem'
    },
    review_card:{ 
        maxWidth:'50rem', 
        pl:'7rem',  
        m:'0 auto',
    },
    review_name:{ 
        fontSize:'2rem',
           
    },
   review_comment:{ 
    ml:'2.5rem', fontSize:'1.2rem'
   },
   review_btn:{ 
        display:'block',
        mt: 8, 
        bgcolor:'#596475', 
        width:'10rem',
        '&:hover':{bgcolor:'#1F2232', 
        transition:'all 1s',
        
   }},



   cardset_card_widther:{ 
    width:'100%',
    height: '80vh',
    margin: '0 auto', 
    mt: 2
   },
   cardset_card:{ 
    width:'75%',
    height: '85vh',
    margin: '0 auto', 
    mt: 2, mb:'0.02rem'
   },
   cardset_cardheader:{
    textAlign:'center', 
    fontSize:'2rem'
   },
   cardset_btn:{ 
    mt:10,
    color:'#596474',
    fontSize:'1rem'
    },
    cardset_descr:{ 
        pt:1,
        fontSize: '.7rem',
        height:'10rem', 
        overflow:'hidden'
    },

      cardset_box:{
    pt:'1rem'
   },
    listing_detail_title:{
        display: 'inline-block', 
        fontFamily:'ubuntu',
        fontWeight:'bold',
        ml: '10rem',
        pt:2,
        mb: '2rem'
    },
    listing_detail_description:{
        display: 'inline-block', 
        fontFamily:'ubuntu',
        fontWeight:'bold',
        textAlign:'justify',
        ml:1.5,
        pl:2,
        maxWidth:'90%'
    },
    listing_detail_agency:{
        cursor:'pointer',
        '&:hover':{
            backgroundColor: '#5A5A66', 
            color:'#fff',
            transition: 'all 1s'
        }
    },
    listing_detail_info:{
        mt:2
    },


    agency_btn:{
        bgcolor:'#EFD3D7',
        color:'#1F2232', 
        '&:hover':{bgcolor:'#DFA5AE', 
        transition:'all 1s'},
        mr:1, mt:5
    },

    update_title:{
        textAlign:'center', 
        m:'1rem'
    },
    update_main:{
        m:'0 3rem'
    },
   
   
}