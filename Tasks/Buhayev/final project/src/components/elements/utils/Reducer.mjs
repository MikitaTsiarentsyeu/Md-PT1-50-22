import {useImmerReducer} from 'use-immer';



function ReducerFuction(draft, action) {
    switch (action.type) {
        case "catchAgencyNameChange":
			draft.agencyNameValue = action.agencyNameChosen;
			break;
        case "catchPhoneNumberChange":
            draft.phoneNumberValue = action.phoneNumberChosen;
            break;
            
        case "catchBioChange":
            draft.bioValue = action.bioChosen;
            break;
            
        case "catchUploadedPicture":
            draft.uploadedPicture = action.pictureChosen;
            break;
            
        case "catchProfilePictureChange":
            draft.profilePictureValue = action.profilePictureChosen;
            break;
            
        case "changeSendRequest":
            draft.sendRequest = draft.sendRequest + 1;
            break;
            
        case 'changeRequest':
            draft.sendRequest = draft.sendRequest + 1
            break;
        case 'catchTitleChange':
            draft.titleValue = action.titleChosen;
            break;
        case "catchListingTypeChange":
            draft.listingTypeValue = action.listingTypeChosen;
            break;
        case "catchDescriptionChange":
            draft.descriptionValue = action.descriptionChosen;
            break;
        case "catchAreaChange":
            draft.areaValue = action.areaChosen;
            break;
        case "catchBoroughChange":
            draft.boroughValue = action.boroughChosen;
            break;
        case "catchLatitudeChange":
            draft.latitudeValue = action.latitudeChosen;
            break;

        case "catchLongitudeChange":
            draft.longitudeValue = action.longitudeChosen;
            break;

        case "catchPropertyStatusChange":
            draft.propertyStatusValue = action.propertyStatusChosen;
            break;

        case "catchPriceChange":
            draft.priceValue = action.priceChosen;
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
        default: break;
    }
}

export {ReducerFuction}