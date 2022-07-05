import React, { useEffect, useRef, useMemo, useContext} from 'react';
import {Container,  Button, Typography,MenuItem,  Box,Grid,TextField,Alert} from '@mui/material';
import {styles} from '../elements/utils/Styles'
import Axios from "axios";
import CssBaseline from '@mui/material/CssBaseline';
import {useImmerReducer} from 'use-immer';
import { useNavigate } from "react-router-dom";
import Navbar from '../elements/Navbar';
import Snackbar from '@mui/material/Snackbar';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { MapContainer, TileLayer, useMap, Marker,Popup,Polygon } from 'react-leaflet'
import stateContext from '../../Context/StateContext';
import {areaOptions, innerLondonOptions, outerLondonOptions, listingTypeOptions, propertyStatusOptions, rentalFrequencyOptions} from '../elements/utils/Data'
import Footer from '../elements/Footer'


// Boroughs
import Camden from "../../Assets/Boroughs/Camden";
import Greenwich from "../../Assets/Boroughs/Greenwich";
import Hackney from "../../Assets/Boroughs/Hackney";
import Hammersmith from "../../Assets/Boroughs/Hammersmith";
import Islington from "../../Assets/Boroughs/Islington";
import Kensington from "../../Assets/Boroughs/Kensington";
import Lambeth from "../../Assets/Boroughs/Lambeth";
import Lewisham from "../../Assets/Boroughs/Lewisham";
import Southwark from "../../Assets/Boroughs/Southwark";
import Hamlets from "../../Assets/Boroughs/Hamlets";
import Wandsworth from "../../Assets/Boroughs/Wandsworth";
import Westminster from "../../Assets/Boroughs/Westminster";
import City_of_London from "../../Assets/Boroughs/City_of_London";
import Barking from "../../Assets/Boroughs/Barking";
import Barnet from "../../Assets/Boroughs/Barnet";
import Bexley from "../../Assets/Boroughs/Bexley";
import Brent from "../../Assets/Boroughs/Brent";
import Bromley from "../../Assets/Boroughs/Bromley";
import Croydon from "../../Assets/Boroughs/Croydon";
import Ealing from "../../Assets/Boroughs/Ealing";
import Enfield from "../../Assets/Boroughs/Enfield";
import Haringey from "../../Assets/Boroughs/Haringey";
import Harrow from "../../Assets/Boroughs/Harrow";
import Havering from "../../Assets/Boroughs/Havering";
import Hillingdon from "../../Assets/Boroughs/Hillingdon";
import Hounslow from "../../Assets/Boroughs/Hounslow";
import Kingston from "../../Assets/Boroughs/Kingston";
import Merton from "../../Assets/Boroughs/Merton";
import Newham from "../../Assets/Boroughs/Newham";
import Redbridge from "../../Assets/Boroughs/Redbridge";
import Richmond from "../../Assets/Boroughs/Richmond";
import Sutton from "../../Assets/Boroughs/Sutton";
import Waltham from "../../Assets/Boroughs/Waltham";





function NewListing() {
    const navigate = useNavigate();
	const initialState = { 
		titleValue: "",
		listingTypeValue: "",
		descriptionValue: "",
		areaValue: "",
		boroughValue: "",
		latitudeValue: "",
		longitudeValue: "",
		propertyStatusValue: "",
		priceValue: "",
		rentalFrequencyValue: "",
		roomsValue: "",
		furnishedValue: false,
		poolValue: false,
		elevatorValue: false,
		cctvValue: false,
		parkingValue: false,
		pictureValue: "",
		mapInstance:null,
		markerPosition:{lat: '51.51', lng: '-0.0782'}, 
		uploadedImages:[],
		sendRequest: 0,
		userProfile: {
			agencyName: '', 
			phone: '',
			agencyPicture:'',
			bio: '',
			sellerId:'',
			sellerListings:''
		},
		dataIsLoading: true,
		listingInfo: "",
		sellerProfileInfo: "",
		openSnack: false,
		disabledBtn: false,
		agencyNameValue: '', 
		phoneValue:'', 
		bioValue:'', 
		uploadedPictureProfileValue: [],
		profilePicture:'',
		token:'',
		titleErrors: {
			hasErrors: false,
			errorMessage: "",
		},
		listingTypeErrors: {
			hasErrors: false,
			errorMessage: "",
		},
		propertyStatusErrors: {
			hasErrors: false,
			errorMessage: "",
		},
		priceErrors: {
			hasErrors: false,
			errorMessage: "",
		},
		areaErrors: {
			hasErrors: false,
			errorMessage: "",
		},
		boroughErrors: {
			hasErrors: false,
			errorMessage: "",
		},
	}

	function ReducerFuction(draft, action) {
		switch (action.type) {
			case 'changeRequest':
				draft.sendRequest = draft.sendRequest + 1
				break;
			case 'catchTitleChange':
				draft.titleValue = action.titleChosen;
				draft.titleErrors.hasErrors = false;
				draft.titleErrors.errorMessage = "";
				break;
			case "catchListingTypeChange":
				draft.listingTypeValue = action.listingTypeChosen;
				draft.listingTypeErrors.hasErrors = false;
				draft.listingTypeErrors.errorMessage = "";
				break;
			case "catchDescriptionChange":
				draft.descriptionValue = action.descriptionChosen;
				break;
			case "catchAreaChange":
				draft.areaValue = action.areaChosen;
				draft.areaErrors.hasErrors = false;
				draft.areaErrors.errorMessage = "";
				break;
			case "catchBoroughChange":
				draft.boroughValue = action.boroughChosen;
				draft.boroughErrors.hasErrors = false;
				draft.boroughErrors.errorMessage = "";
				break;
			case "catchLatitudeChange":
				draft.latitudeValue = action.latitudeChosen;
				break;
	
			case "catchLongitudeChange":
				draft.longitudeValue = action.longitudeChosen;
				break;
	
			case "catchPropertyStatusChange":
				draft.propertyStatusValue = action.propertyStatusChosen;
				draft.propertyStatusErrors.hasErrors = false;
				draft.propertyStatusErrors.errorMessage = "";
				break;
	
			case "catchPriceChange":
				draft.priceValue = action.priceChosen;
				draft.priceErrors.hasErrors = false;
				draft.priceErrors.errorMessage = "";
				break;
			case "catchRentalFrequencyChange":
				draft.rentalFrequencyValue = action.rentalFrequencyChosen;
				break;
	
			case "catchRoomsChange":
				draft.roomsValue = action.roomsChosen;
				break;
	
			case "catchFurnishedChange":
				draft.furnishedValue = action.furnishedChosen;
				break;
	
			case "catchPoolChange":
				draft.poolValue = action.poolChosen;
				break;
	
			case "catchElevatorChange":
				draft.elevatorValue = action.elevatorChosen;
				break;
	
			case "catchCctvChange":
				draft.cctvValue = action.cctvChosen;
				break;
	
			case "catchParkingChange":
				draft.parkingValue = action.parkingChosen;
				break;
			case 'getMap':
				draft.mapInstance = action.mapData;
				break
			case "catchPictureChange":
				draft.pictureValue = action.picture1Chosen[0];
				break;
			case "changeMarkerPosition":
				draft.markerPosition.lat = action.changeLatitude;
				draft.markerPosition.lng = action.changeLongitude;
				draft.latitudeValue = draft.markerPosition.lat;
				draft.longitudeValue = draft.markerPosition.lng;
				
				break;
			case 'catchUploadedPictures':
				draft.uploadedImages = action.imagesChosen
				break;
			case 'catchUserProfileInfo': 
				draft.userProfile.agencyName = action.profileObj.agency_name
				draft.userProfile.phone = action.profileObj.phone_number
				draft.userProfile.agencyPicture = action.profileObj.profile_picture
				draft.userProfile.bio = action.profileObj.biography
				draft.userProfile.sellerListings = action.profileObj.seller_listings
				draft.userProfile.sellerId = action.profileObj.seller
				break
			case 'catchAgencyNameChange':
				
					draft.agencyNameValue = action.agencyNameChosen
				
				break;
			case 'catchAgencyNameChangeClick':
				if (action.agencyNameChosen !== draft.userProfile.agencyName){
					draft.agencyNameValue = action.agencyNameChosen
				}
				else if(!action.agencyNameChosen){
					draft.agencyNameValue = draft.userProfile.agencyName}
				else{
					draft.agencyNameValue = draft.userProfile.agencyName
				}
				break;
	
			case 'catchPhoneChange':
				draft.phoneValue = action.phoneChosen
				break;
			case 'catchBioChange':
				draft.bioValue = action.bioChosen
				break;
			case 'catchPictureProfileChange':
				draft.uploadedPictureProfileValue = action.pictureProfileChosen
				break;
			
			case 'catchProfilePicture':
				draft.profilePicture = action.profilePictureChosen
				break;
	
			case  'catchListingInfo':
				draft.listingInfo = action.listingObject
				break;
	
			case "loadingDone":
					draft.dataIsLoading = false;
					break;
	
			case "catchSellerProfileInfo":
				draft.sellerProfileInfo = action.profileObject;
				break;
	
			case "openTheSnack":
				draft.openSnack = true;
				break;
	
			case "disableTheButton":
				draft.disabledBtn = true;
				break;
	
			case "allowTheButton":
				draft.disabledBtn = false;
				break;
	
	
			case "catchTitleChange":
				draft.titleValue = action.titleChosen;
				break;
	
	
			case "changeSendRequest":
				draft.sendRequest = draft.sendRequest + 1;
				break;
			
			case 'catchToken':
				draft.token = action.tokenValue;
				break; 
	
			case "catchTitleErrors":
				if (action.titleChosen.length === 0) {
					draft.titleErrors.hasErrors = true;
					draft.titleErrors.errorMessage = "This field must not be empty";
				}
				break;
	
			case "catchListingTypeErrors":
				if (action.listingTypeChosen.length === 0) {
					draft.listingTypeErrors.hasErrors = true;
					draft.listingTypeErrors.errorMessage = "This field must not be empty";
				}
				break;
	
			case "catchPropertyStatusErrors":
				if (action.propertyStatusChosen.length === 0) {
					draft.propertyStatusErrors.hasErrors = true;
					draft.propertyStatusErrors.errorMessage =
						"This field must not be empty";
				}
				break;
	
			case "catchPriceErrors":
				if (action.priceChosen.length === 0) {
					draft.priceErrors.hasErrors = true;
					draft.priceErrors.errorMessage = "This field must not be empty";
				}
				break;
	
			case "catchAreaErrors":
				if (action.areaChosen.length === 0) {
					draft.areaErrors.hasErrors = true;
					draft.areaErrors.errorMessage = "This field must not be empty";
				}
				break;
	
			case "catchBoroughErrors":
				if (action.boroughChosen.length === 0) {
					draft.boroughErrors.hasErrors = true;
					draft.boroughErrors.errorMessage = "This field must not be empty";
				}
				break;
	
			case "emptyTitle":
				draft.titleErrors.hasErrors = true;
				draft.titleErrors.errorMessage = "This field must not be empty";
				break;
	
			case "emptyListingType":
				draft.listingTypeErrors.hasErrors = true;
				draft.listingTypeErrors.errorMessage = "This field must not be empty";
				break;
	
			case "emptyPropertyStatus":
				draft.propertyStatusErrors.hasErrors = true;
				draft.propertyStatusErrors.errorMessage =
					"This field must not be empty";
				break;
	
			case "emptyPrice":
				draft.priceErrors.hasErrors = true;
				draft.priceErrors.errorMessage = "This field must not be empty";
				break;
	
			case "emptyArea":
				draft.areaErrors.hasErrors = true;
				draft.areaErrors.errorMessage = "This field must not be empty";
				break;
	
			case "emptyBoroug":
				draft.borougErrors.hasErrors = true;
				draft.borougErrors.errorMessage = "This field must not be empty";
				break;	
			default: break;

		}
	}
	
	


	const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);

    const handleSubmit = (event) => {
        event.preventDefault();
		if (
			!state.titleErrors.hasErrors &&
			!state.listingTypeErrors.hasErrors &&
			!state.propertyStatusErrors.hasErrors &&
			!state.priceErrors.hasErrors &&
			!state.areaErrors.hasErrors &&
			!state.boroughErrors.hasErrors &&
			state.latitudeValue &&
			state.longitudeValue
		) {
			dispatch({ type: "changeSendRequest" });
			dispatch({ type: "disableTheButton" });
		} else if (state.titleValue === "") {
			dispatch({ type: "emptyTitle" });
			window.scrollTo(0, 0);
		} else if (state.listingTypeValue === "") {
			dispatch({ type: "emptyListingType" });
			window.scrollTo(0, 0);
		} else if (state.propertyStatusValue === "") {
			dispatch({ type: "emptyPropertyStatus" });
			window.scrollTo(0, 0);
		} else if (state.priceValue === "") {
			dispatch({ type: "emptyPrice" });
			window.scrollTo(0, 0);
		} else if (state.areaValue === "") {
			dispatch({ type: "emptyArea" });
			window.scrollTo(0, 0);
		} else if (state.boroughValue === "") {
			dispatch({ type: "emptyBorough" });
			window.scrollTo(0, 0);
		}
		dispatch({type: 'changeRequest', })
        console.log('success');
    };

    function TheMapComponent(){
        const map = useMap()
        
        dispatch({type: 'getMap', mapData: map})
        return null;
    }

	//get profile
	useEffect(()=>{
		async function getProfile(){
			try{
				const response = await Axios.get(`http://127.0.0.1:8000/api/profiles/${GlobalState.userId}/`)
				console.log(response.data)
				console.log(state)
				dispatch({type: 'catchUserProfileInfo', profileObj: response.data})
			} catch(e){
				console.log(e.response)
			}
		
	}
	getProfile()
	},[])

	

    // Changing the map view depending on the chosen borough

    useEffect(() => {
		if (state.boroughValue === "Camden") {
			state.mapInstance.setView([51.54103467179952, -0.14870897037846917], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.54103467179952,
				changeLongitude: -0.14870897037846917,
			});
		} else if (state.boroughValue === "Greenwich") {
			state.mapInstance.setView([51.486316313935134, 0.005925763550159742], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.486316313935134,
				changeLongitude: 0.005925763550159742,
			});
		} else if (state.boroughValue === "Hackney") {
			state.mapInstance.setView([51.55421119118178, -0.061054618357071246], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.55421119118178,
				changeLongitude: -0.061054618357071246,
			});
		} else if (state.boroughValue === "Hammersmith and Fulham") {
			state.mapInstance.setView([51.496961673854216, -0.22495912738555046], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.496961673854216,
				changeLongitude: -0.22495912738555046,
			});
		} else if (state.boroughValue === "Islington") {
			state.mapInstance.setView([51.54974373783584, -0.10746608414711818], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.54974373783584,
				changeLongitude: -0.10746608414711818,
			});
		} else if (state.boroughValue === "Kensington and Chelsea") {
			state.mapInstance.setView([51.49779579272461, -0.1908227388030137], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.49779579272461,
				changeLongitude: -0.1908227388030137,
			});
		} else if (state.boroughValue === "Lambeth") {
			state.mapInstance.setView([51.457598293463874, -0.12030697867735651], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.457598293463874,
				changeLongitude: -0.12030697867735651,
			});
		} else if (state.boroughValue === "Lewisham") {
			state.mapInstance.setView([51.45263474786279, -0.017657579903930083], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.45263474786279,
				changeLongitude: -0.017657579903930083,
			});
		} else if (state.boroughValue === "Southwark") {
			state.mapInstance.setView([51.47281414549159, -0.07657080658293915], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.47281414549159,
				changeLongitude: -0.07657080658293915,
			});
		} else if (state.boroughValue === "Tower Hamlets") {
			state.mapInstance.setView([51.52222760075287, -0.03427379217816716], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.52222760075287,
				changeLongitude: -0.03427379217816716,
			});
		} else if (state.boroughValue === "Wandsworth") {
			state.mapInstance.setView([51.45221859319854, -0.1910578642162312], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.45221859319854,
				changeLongitude: -0.1910578642162312,
			});
		} else if (state.boroughValue === "Westminster") {
			state.mapInstance.setView([51.51424692365236, -0.1557886924596714], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.51424692365236,
				changeLongitude: -0.1557886924596714,
			});
		} else if (state.boroughValue === "City of London") {
			state.mapInstance.setView([51.51464652712437, -0.09207257068971077], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.51464652712437,
				changeLongitude: -0.09207257068971077,
			});
		} else if (state.boroughValue === "Barking and Dangenham") {
			state.mapInstance.setView([51.54475354441844, 0.13730036835406337], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.54475354441844,
				changeLongitude: 0.13730036835406337,
			});
		} else if (state.boroughValue === "Barnet") {
			state.mapInstance.setView([51.61505810569654, -0.20104146847921367], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.61505810569654,
				changeLongitude: -0.20104146847921367,
			});
		} else if (state.boroughValue === "Bexley") {
			state.mapInstance.setView([51.45784336604241, 0.1386755093498764], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.45784336604241,
				changeLongitude: 0.1386755093498764,
			});
		} else if (state.boroughValue === "Brent") {
			state.mapInstance.setView([51.55847917911348, -0.2623697479848262], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.55847917911348,
				changeLongitude: -0.2623697479848262,
			});
		} else if (state.boroughValue === "Bromley") {
			state.mapInstance.setView([51.37998089785619, 0.056091833685512606], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.37998089785619,
				changeLongitude: 0.056091833685512606,
			});
		} else if (state.boroughValue === "Croydon") {
			state.mapInstance.setView([51.36613815034951, -0.08597242883896719], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.36613815034951,
				changeLongitude: -0.08597242883896719,
			});
		} else if (state.boroughValue === "Ealing") {
			state.mapInstance.setView([51.52350664933499, -0.33384540332179463], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.52350664933499,
				changeLongitude: -0.33384540332179463,
			});
		} else if (state.boroughValue === "Enfield") {
			state.mapInstance.setView([51.650718869158275, -0.07999628038008409], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.650718869158275,
				changeLongitude: -0.07999628038008409,
			});
		} else if (state.boroughValue === "Haringey") {
			state.mapInstance.setView([51.591214467057085, -0.10319530898095737], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.591214467057085,
				changeLongitude: -0.10319530898095737,
			});
		} else if (state.boroughValue === "Harrow") {
			state.mapInstance.setView([51.60218606442213, -0.33540294600548437], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.60218606442213,
				changeLongitude: -0.33540294600548437,
			});
		} else if (state.boroughValue === "Havering") {
			state.mapInstance.setView([51.57230623503768, 0.2256095005492423], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.57230623503768,
				changeLongitude: 0.2256095005492423,
			});
		} else if (state.boroughValue === "Hillingdon") {
			state.mapInstance.setView([51.5430033964411, -0.4435905982156584], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.5430033964411,
				changeLongitude: -0.4435905982156584,
			});
		} else if (state.boroughValue === "Hounslow") {
			state.mapInstance.setView([51.475988836438525, -0.3660060903075389], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.475988836438525,
				changeLongitude: -0.3660060903075389,
			});
		} else if (state.boroughValue === "Kingston upon Thames") {
			state.mapInstance.setView([51.39401320084246, -0.2841003136670212], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.39401320084246,
				changeLongitude: -0.2841003136670212,
			});
		} else if (state.boroughValue === "Merton") {
			state.mapInstance.setView([51.41148120353897, -0.18805584151013174], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.41148120353897,
				changeLongitude: -0.18805584151013174,
			});
		} else if (state.boroughValue === "Newham") {
			state.mapInstance.setView([51.533282275935306, 0.031692014878610064], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.533282275935306,
				changeLongitude: 0.031692014878610064,
			});
		} else if (state.boroughValue === "Redbridge") {
			state.mapInstance.setView([51.585885574074965, 0.07764760021283491], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.585885574074965,
				changeLongitude: 0.07764760021283491,
			});
		} else if (state.boroughValue === "Richmond upon Thames") {
			state.mapInstance.setView([51.450368976651696, -0.30801386088548505], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.450368976651696,
				changeLongitude: -0.30801386088548505,
			});
		} else if (state.boroughValue === "Sutton") {
			state.mapInstance.setView([51.363672040828504, -0.1702200806863363], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.363672040828504,
				changeLongitude: -0.1702200806863363,
			});
		} else if (state.boroughValue === "Waltham Forest") {
			state.mapInstance.setView([51.59466635701797, -0.012215840493378892], 12);
			dispatch({
				type: "changeMarkerPosition",
				changeLatitude: 51.59466635701797,
				changeLongitude: -0.012215840493378892,
			});
		}
	}, [state.boroughValue]);



	const markerRef = useRef(null)
	const eventHandlers = useMemo(
		() => ({
		dragend() {
			const marker = markerRef.current
			dispatch({
				type: "catchLatitudeChange",
				latitudeChosen: marker.getLatLng().lat,
			});
			dispatch({
				type: "catchLongitudeChange",
				longitudeChosen: marker.getLatLng().lng,
			});
		},
		}),
		[],
	)
	

	function BoroughDisplay() {
		if (state.boroughValue === "Camden") {
			return <Polygon positions={Camden} />;
		} else if (state.boroughValue === "Greenwich") {
			return <Polygon positions={Greenwich} />;
		} else if (state.boroughValue === "Hackney") {
			return <Polygon positions={Hackney} />;
		} else if (state.boroughValue === "Hammersmith and Fulham") {
			return <Polygon positions={Hammersmith} />;
		} else if (state.boroughValue === "Islington") {
			return <Polygon positions={Islington} />;
		} else if (state.boroughValue === "Kensington and Chelsea") {
			return <Polygon positions={Kensington} />;
		} else if (state.boroughValue === "Lambeth") {
			return <Polygon positions={Lambeth} />;
		} else if (state.boroughValue === "Lewisham") {
			return <Polygon positions={Lewisham} />;
		} else if (state.boroughValue === "Southwark") {
			return <Polygon positions={Southwark} />;
		} else if (state.boroughValue === "Tower Hamlets") {
			return <Polygon positions={Hamlets} />;
		} else if (state.boroughValue === "Wandsworth") {
			return <Polygon positions={Wandsworth} />;
		} else if (state.boroughValue === "Westminster") {
			return <Polygon positions={Westminster} />;
		} else if (state.boroughValue === "City of London") {
			return <Polygon positions={City_of_London} />;
		} else if (state.boroughValue === "Barking and Dangenham") {
			return <Polygon positions={Barking} />;
		} else if (state.boroughValue === "Barnet") {
			return <Polygon positions={Barnet} />;
		} else if (state.boroughValue === "Bexley") {
			return <Polygon positions={Bexley} />;
		} else if (state.boroughValue === "Brent") {
			return <Polygon positions={Brent} />;
		} else if (state.boroughValue === "Bromley") {
			return <Polygon positions={Bromley} />;
		} else if (state.boroughValue === "Croydon") {
			return <Polygon positions={Croydon} />;
		} else if (state.boroughValue === "Ealing") {
			return <Polygon positions={Ealing} />;
		} else if (state.boroughValue === "Enfield") {
			return <Polygon positions={Enfield} />;
		} else if (state.boroughValue === "Haringey") {
			return <Polygon positions={Haringey} />;
		} else if (state.boroughValue === "Harrow") {
			return <Polygon positions={Harrow} />;
		} else if (state.boroughValue === "Havering") {
			return <Polygon positions={Havering} />;
		} else if (state.boroughValue === "Hillingdon") {
			return <Polygon positions={Hillingdon} />;
		} else if (state.boroughValue === "Hounslow") {
			return <Polygon positions={Hounslow} />;
		} else if (state.boroughValue === "Kingston upon Thames") {
			return <Polygon positions={Kingston} />;
		} else if (state.boroughValue === "Merton") {
			return <Polygon positions={Merton} />;
		} else if (state.boroughValue === "Newham") {
			return <Polygon positions={Newham} />;
		} else if (state.boroughValue === "Redbridge") {
			return <Polygon positions={Redbridge} />;
		} else if (state.boroughValue === "Richmond upon Thames") {
			return <Polygon positions={Richmond} />;
		} else if (state.boroughValue === "Sutton") {
			return <Polygon positions={Sutton} />;
		} else if (state.boroughValue === "Waltham Forest") {
			return <Polygon positions={Waltham} />;
		}
	}




	const GlobalState = useContext(stateContext);
	useEffect(()=>{
		if(state.sendRequest){
			async function AddProperty(){
				const formData = new FormData();
					formData.append("title", state.titleValue);
					formData.append("description", state.descriptionValue);
					formData.append("area", state.areaValue);
					formData.append("borough", state.boroughValue);
					formData.append("listing_type", state.listingTypeValue);
					formData.append("property_status", state.propertyStatusValue);
					formData.append("price", state.priceValue);
					formData.append("rental_frequency", state.rentalFrequencyValue);
					formData.append("rooms", state.roomsValue);
					formData.append("furnished", state.furnishedValue);
					formData.append("pool", state.poolValue);
					formData.append("elevator", state.elevatorValue);
					formData.append("cctv", state.cctvValue);
					formData.append("parking", state.parkingValue);
					formData.append("latitude", state.latitudeValue);
					formData.append("longitude", state.longitudeValue);
					formData.append("picture", state.pictureValue);
					formData.append("seller", GlobalState.userId);
				try{
					const response = await Axios.post('http://127.0.0.1:8000/api/listings/create/', formData)
					console.log(response.data);
					
					dispatch({type:'openTheSnack'})
					console.log(state.openSnack)
					
				}catch(e){
					
				}
			}
			AddProperty();
		}
	}, [state.sendRequest])

	useEffect(() => {
        if (state.openSnack) {
            setTimeout(() => {
                navigate("/");
            }, 1500);
        }
    }, [state.openSnack]);

	function SubmitButton(){
		if(GlobalState.userIsLogged && state.userProfile.agencyName !== null && state.userProfile.agencyName !== ''
		 && state.userProfile.phone !== null && state.userProfile.phone !== ''){
			return (<Button
			type="submit"
			
			fullWidth
			variant="contained"
			sx={styles.agency_btn}
		>
			Submit
		</Button>)
		} else if (GlobalState.userIsLogged && (!state.userProfile.agencyName || !state.userProfile.phone)){
			return (<Button
			
			fullWidth
			variant="outlined"
			sx={{textAlign:'center',mt: 3, mb: 2, width:'30%'}}
		>
			Complete your profile to add a property
		</Button>)
		}else if (!GlobalState.userIsLogged){
			return (<Button
			
			fullWidth
			variant="outlined"
			sx={{textAlign:'center',mt: 3, mb: 2, width:'30%'}}
		>
			Log In Please
		</Button>)
		}
	}
  return (
    <>
    <Navbar/>
    <Container component="main" maxWidth="xs">
                    <CssBaseline/>
                    <Box
                        sx={{
                            marginTop: 8,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                        }}
                    >
                        <Typography component="h1" variant="h5">
                             Submit a property
                        </Typography>
                        <Box component="form" noValidate   onSubmit={handleSubmit} sx={{mt: 3,width:'60rem'}}>
                            <Grid container spacing={2} >
                                <Grid item xs={12} sm={12}>
                                    <TextField
                                        sx={{width:'100%'}}
                                        
                                        name="title"
                                        required
                                        fullWidth
                                        id="title"
                                        label="Title"
                                        
                                        value={state.titleValue}
                                        onChange={(event)=>(dispatch({type: 'catchTitleChange', titleChosen: event.target.value}))}
										onBlur={(e) =>
											dispatch({
												type: "catchTitleErrors",
												titleChosen: e.target.value,
											})
										}
										error={state.titleErrors.hasErrors ? true : false}
										helperText={state.titleErrors.errorMessage}
                                    />
                                </Grid>
								
                                <Grid item xs={12} sm={12}>
                                    <TextField
                                        sx={{width:'100%'}}
										multiline
                                        rows={6}
                                        name="description"
                                        required
                                        fullWidth
                                        id="description"
                                        label="description"
                                        value={state.descriptionValue}
                                        onChange={(event)=>(dispatch({type: 'catchDescriptionChange', descriptionChosen: event.target.value}))}
										
                                    />
                                </Grid>
                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                       
                                        name="listingType"
                                        required
                                        fullWidth
                                        id="listingType"
                                        label="listingType"
                                        select
                                        value={state.listingTypeValue}
                                        onChange={(event)=>(dispatch({type: 'catchListingTypeChange', listingTypeChosen: event.target.value}))}
										onBlur={(e) =>
											dispatch({
												type: "catchListingTypeErrors",
												listingTypeChosen: e.target.value,
											})
										}
										error={state.listingTypeErrors.hasErrors ? true : false}
										helperText={state.listingTypeErrors.errorMessage}
										
                                    >
										{listingTypeOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                        {option.label}</MenuItem>))}
									</TextField>
                                </Grid>
                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                       
                                        name="propetryStatus"
                                        required
                                        fullWidth
                                        id="propetryStatus"
                                        label="propetry status"
                                        select
                                        value={state.propertyStatusValue}
                                        onChange={(event)=>(dispatch({type: 'catchPropertyStatusChange', propertyStatusChosen: event.target.value}))}
										onBlur={(e) =>
											dispatch({
												type: "catchPropertyStatusErrors",
												propertyStatusChosen: e.target.value,
											})}
										
                                    >
										{propertyStatusOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                        {option.label}</MenuItem>))}
									</TextField>
                                </Grid>

                                
                                

                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                        
                                        name="price"
                                        required
                                        fullWidth
                                        id="price"
                                        label="price"
                                       
                                        value={state.priceValue}
                                        onChange={(event)=>(dispatch({type: 'catchPriceChange', priceChosen: event.target.value}))}
                                    />
                                </Grid>
                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                        disabled ={state.listingTypeValue === 'Office' ? true : false}
                                        name="roms"
                                        required
                                        fullWidth
                                        id="rooms"
                                        label="rooms"
                                       
                                        value={state.roomsValue}
                                        onChange={(event)=>(dispatch({type: 'catchRoomsChange', roomsChosen: event.target.value}))}
                                    />
                                </Grid>
                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                       	select
									   	disabled={state.propertyStatusValue === "Sale" ? true : false}
                                        name="Rental Frequency"
                                        required
                                        fullWidth
                                        id="rentalFrequency"
                                        label="Rental Frequency"
                                     
                                        value={state.rentalFrequencyValue}
                                        onChange={(event)=>(dispatch({type: 'catchRentalFrequencyChange', rentalFrequencyChosen: event.target.value}))}
                                    >
										{rentalFrequencyOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                        {option.label}</MenuItem>))}
									</TextField>
                                </Grid>

								<Grid item container justifyContent="space-between">
					<Grid item xs={2} style={{ marginTop: "1rem" }}>
						<FormControlLabel
							control={
								<Checkbox
									checked={state.furnishedValue}
									onChange={(e) =>
										dispatch({
											type: "catchFurnishedChange",
											furnishedChosen: e.target.checked,
										})
									}
								/>
							}
							label="Furnished"
						/>
					</Grid>

					<Grid item xs={2} style={{ marginTop: "1rem" }}>
						<FormControlLabel
							control={
								<Checkbox
									checked={state.poolValue}
									onChange={(e) =>
										dispatch({
											type: "catchPoolChange",
											poolChosen: e.target.checked,
										})
									}
								/>
							}
							label="Pool"
						/>
					</Grid>

					<Grid item xs={2} style={{ marginTop: "1rem" }}>
						<FormControlLabel
							control={
								<Checkbox
									checked={state.elevatorValue}
									onChange={(e) =>
										dispatch({
											type: "catchElevatorChange",
											elevatorChosen: e.target.checked,
										})
									}
								/>
							}
							label="Elevator"
						/>
					</Grid>

					<Grid item xs={2} style={{ marginTop: "1rem" }}>
						<FormControlLabel
							control={
								<Checkbox
									checked={state.cctvValue}
									onChange={(e) =>
										dispatch({
											type: "catchCctvChange",
											cctvChosen: e.target.checked,
										})
									}
								/>
							}
							label="Cctv"
						/>
					</Grid>

					<Grid item xs={2} style={{ marginTop: "1rem" }}>
						<FormControlLabel
							control={
								<Checkbox
									checked={state.parkingValue}
									onChange={(e) =>
										dispatch({
											type: "catchParkingChange",
											parkingChosen: e.target.checked,
										})
									}
								/>
							}
							label="Parking"
						/>
					</Grid>
				</Grid>
                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                        autoComplete="given-name"
                                        name="area"
                                        required
                                        fullWidth
                                        select
                                        id="area"
                                        label="Area"
                                        autoFocus
                                        value={state.areaValue}
                                        onChange={(event)=>(dispatch({type: 'catchAreaChange', areaChosen: event.target.value}))}
										error={state.areaErrors.hasErrors ? true : false}
										helperText={state.areaErrors.errorMessage}
                                    >
                                        {areaOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                        {option.label}</MenuItem>))}

                                    </TextField> 
                                </Grid>

                                <Grid item xs={6} sm={6}>
                                    <TextField
                                        sx={{width:'100%'}}
                                       
                                        name="borough"
                                        required
                                        select
                                        fullWidth
                                        id="borough"
                                        label="Borough"
                                        
                                        value={state.boroughValue}
                                        onChange={(event)=>(dispatch({type: 'catchBoroughChange', boroughChosen: event.target.value}))}
										onBlur={(e) =>
											dispatch({
												type: "catchBoroughErrors",
												boroughChosen: e.target.value,
											})
										}
										error={state.boroughErrors.hasErrors ? true : false}
										helperText={state.boroughErrors.errorMessage}
                                    >
                                        {state.areaValue === 'Inner London' ? 
                                            innerLondonOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>{option.label}</MenuItem>)) : 
                                            outerLondonOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                            {option.label}</MenuItem>))}
                                    </TextField>
                                </Grid>
                                <Grid item container sx = {{height: '25rem', mt:'1rem'}}>
								{state.latitudeValue && state.longitudeValue ? (
						<Alert severity="success">
							You property is located @ {state.latitudeValue},{" "}
							{state.longitudeValue}
						</Alert>
					) : (
						<Alert severity="warning">
							Locate your property on the map before submitting this form
						</Alert>
					)}
                                <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                                    <TileLayer
                                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                                        />
                                        <TheMapComponent/>
                                        {BoroughDisplay()}
                                        <Marker
                                            draggable={true}
                                            eventHandlers={eventHandlers}
                                            position={state.markerPosition}
                                            ref={markerRef}>
                                        </Marker>
                                    </MapContainer>
                                </Grid>
								
								<Grid item xs={12}>
											
								<Button
                                fullWidth
								component='label'
                                variant="contained"
                                sx={styles.agency_btn}
                            >
								<input type='file' accept="image/png, image/jpeg, image/gif" hidden onChange={(event)=>(dispatch({type: 'catchPictureChange', picture1Chosen: event.target.files}))}/>
                                upload image
                            </Button>
								</Grid>

								<Grid item xs={12}>
									{state.pictureValue ? <p>{state.pictureValue.name}</p> : ''}
								</Grid>
                            </Grid>

                            {SubmitButton()}
                           
                            
                        </Box>
                    </Box>
					<Snackbar
                        sx={{marginTop:'3rem'}}
                        severity="success"
                        open={state.openSnack}
                        message="Listing add to the base"
                        anchorOrigin={{vertical:'top', horizontal:'center'}}
                    />
                </Container>
				<Footer/>
    </>
  )
}

export default NewListing