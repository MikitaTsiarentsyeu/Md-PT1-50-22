import React, { useEffect, useState, useRef, useMemo, useContext } from "react";
import { useNavigate } from "react-router-dom";
import Axios from "axios";
import { useImmerReducer } from "use-immer";
import {styles} from '../../elements/utils/Styles'
import StateContext from "../../../Context/StateContext";

// MUI
import {
	Grid,
	Typography,
	Button,
	TextField,
	FormControlLabel,
	Checkbox,
	Snackbar,
    Box,
} from "@mui/material";

import {ReducerFuction} from '../../elements/utils/Reducer'
import {propertyStatusOptions, rentalFrequencyOptions,listingTypeOptions} from '../../elements/utils/Data'


function ListingUpdate(props) {
    const navigate = useNavigate();
    const GlobalState = useContext(StateContext);
    console.log(props.listingData)
    const initialState = {
        titleValue: props.listingData.title,
        listingTypeValue: props.listingData.listing_type,
        descriptionValue: props.listingData.description,
        propertyStatusValue: props.listingData.property_status,
        priceValue: props.listingData.price,
        rentalFrequencyValue: props.listingData.rental_frequency,
        roomsValue: props.listingData.rooms,
        furnishedValue: props.listingData.furnished,
        poolValue: props.listingData.pool,
        elevatorValue: props.listingData.elevator,
        cctvValue: props.listingData.cctv,
        parkingValue: props.listingData.parking,
        sendRequest: 0,
        openSnack: false,
        disabledBtn: false,}
        const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
        function FormSubmit(e) {
            e.preventDefault();
    
            dispatch({ type: "changeSendRequest" });
            dispatch({ type: "disableTheButton" });
        }
    
        useEffect(() => {
            if (state.sendRequest) {
                async function UpdateProperty() {
                    const formData = new FormData();
                    if (state.listingTypeValue === "Office") {
                        formData.append("title", state.titleValue);
                        formData.append("description", state.descriptionValue);
                        formData.append("listing_type", state.listingTypeValue);
                        formData.append("property_status", state.propertyStatusValue);
                        formData.append("price", state.priceValue);
                        formData.append("rental_frequency", state.rentalFrequencyValue);
                        formData.append("rooms", 0);
                        formData.append("furnished", state.furnishedValue);
                        formData.append("pool", state.poolValue);
                        formData.append("elevator", state.elevatorValue);
                        formData.append("cctv", state.cctvValue);
                        formData.append("parking", state.parkingValue);
                        formData.append("seller", GlobalState.userId);
                    } else {
                        formData.append("title", state.titleValue);
                        formData.append("description", state.descriptionValue);
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
                        formData.append("seller", GlobalState.userId);
                    }
    
                    try {
                        const response = await Axios.patch(
                            `http://127.0.0.1:8000/api/listings/${props.listingData.id}/update/`,
                            formData
                        );
    
                        dispatch({ type: "openTheSnack" });
                    } catch (e) {
                        dispatch({ type: "allowTheButton" });
                    }
                }
                UpdateProperty();
            }
        }, [state.sendRequest]);
    
        useEffect(() => {
            if (state.openSnack) {
                setTimeout(() => {
                    navigate(0);
                }, 1500);
            }
        }, [state.openSnack]);
    
        function PriceDisplay() {
            if (
                state.propertyStatusValue === "Rent" &&
                state.rentalFrequencyValue === "Day"
            ) {
                return "Price per Day*";
            } else if (
                state.propertyStatusValue === "Rent" &&
                state.rentalFrequencyValue === "Week"
            ) {
                return "Price per Week*";
            } else if (
                state.propertyStatusValue === "Rent" &&
                state.rentalFrequencyValue === "Month"
            ) {
                return "Price per Month*";
            } else {
                return "Price*";
            }
        }
        
  return (
    <Box  type='container' style={{ padding:'1rem'}}>
    <form onSubmit={FormSubmit} >
        <Grid  container justifyContent="center" sx={{margin:'1rem', width: "6rem"}}>
            <Typography variant="h4">UPDATE</Typography>
        </Grid>

        <Grid  container style={{ marginTop: "1rem"}}>
            <TextField
                id="title"
                label="Title*"
                variant="standard"
                fullWidth
                value={state.titleValue}
                onChange={(e) =>
                    dispatch({
                        type: "catchTitleChange",
                        titleChosen: e.target.value,
                    })
                }
            />
        </Grid>

        <Grid  container justifyContent="space-between">
            <Grid item xs={5} style={{ marginTop: "1rem" }}>
                <TextField
                    id="listingType"
                    label="Listing Type*"
                    variant="standard"
                    fullWidth
                    value={state.listingTypeValue}
                    onChange={(e) =>
                        dispatch({
                            type: "catchListingTypeChange",
                            listingTypeChosen: e.target.value,
                        })
                    }
                    select
                    SelectProps={{
                        native: true,
                    }}
                >
                    {listingTypeOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                    ))}
                </TextField>
            </Grid>

            <Grid item xs={5} style={{ marginTop: "1rem" }}>
                <TextField
                    id="propertyStatus"
                    label="Property Status*"
                    variant="standard"
                    fullWidth
                    value={state.propertyStatusValue}
                    onChange={(e) =>
                        dispatch({
                            type: "catchPropertyStatusChange",
                            propertyStatusChosen: e.target.value,
                        })
                    }
                    select
                    SelectProps={{
                        native: true,
                    }}
                >
                    {propertyStatusOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                    ))}
                </TextField>
            </Grid>
        </Grid>

        <Grid item container justifyContent="space-between">
            <Grid item xs={5} style={{ marginTop: "1rem" }}>
                <TextField
                    id="rentalFrequency"
                    label="Rental Frequency"
                    variant="standard"
                    disabled={state.propertyStatusValue === "Sale" ? true : false}
                    fullWidth
                    value={state.rentalFrequencyValue}
                    onChange={(e) =>
                        dispatch({
                            type: "catchRentalFrequencyChange",
                            rentalFrequencyChosen: e.target.value,
                        })
                    }
                    select
                    SelectProps={{
                        native: true,
                    }}
                >
                    {rentalFrequencyOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                    ))}
                </TextField>
            </Grid>

            <Grid item xs={5} style={{ marginTop: "1rem" }}>
                <TextField
                    id="price"
                    type="number"
                    label={PriceDisplay()}
                    variant="standard"
                    fullWidth
                    value={state.priceValue}
                    onChange={(e) =>
                        dispatch({
                            type: "catchPriceChange",
                            priceChosen: e.target.value,
                        })
                    }
                />
            </Grid>
        </Grid>

        <Grid item container style={{ marginTop: "1rem" }}>
            <TextField
                id="description"
                label="Description"
                variant="outlined"
                multiline
                rows={6}
                fullWidth
                value={state.descriptionValue}
                onChange={(e) =>
                    dispatch({
                        type: "catchDescriptionChange",
                        descriptionChosen: e.target.value,
                    })
                }
            />
        </Grid>

        {state.listingTypeValue === "Office" ? (
            ""
        ) : (
            <Grid item xs={3} container style={{ marginTop: "1rem" }}>
                <TextField
                    id="rooms"
                    label="Rooms"
                    type="number"
                    variant="standard"
                    fullWidth
                    value={state.roomsValue}
                    onChange={(e) =>
                        dispatch({
                            type: "catchRoomsChange",
                            roomsChosen: e.target.value,
                        })
                    }
                />
            </Grid>
        )}

        <Grid item container justifyContent="space-between">
            <Grid item xs={3} style={{ marginTop: "1rem" }}>
                <FormControlLabel
                    control={
                        <Checkbox
                            color="secondary"   
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

            <Grid item xs={3} style={{ marginTop: "1rem" }}>
                <FormControlLabel
                    control={
                        <Checkbox
                            color="secondary"
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

            <Grid item xs={3} style={{ marginTop: "1rem" }}>
                <FormControlLabel
                    control={
                        <Checkbox
                            color="secondary"
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

            <Grid item xs={3} style={{ marginTop: "1rem" }}>
                <FormControlLabel
                    control={
                        <Checkbox
                            color="secondary"
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

            <Grid item xs={3} style={{ marginTop: "1rem" }}>
                <FormControlLabel
                    control={
                        <Checkbox
                            checked={state.parkingValue}
                            color="secondary"
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

        <Grid
            item
            container
            xs={8}
            style={{ marginTop: "1rem", marginLeft: "auto", marginRight: "auto" }}
        >
            <Button
                variant="contained"
                fullWidth
                type="submit"
                disabled={state.disabledBtn}
                sx={styles.agency_btn}
            >
                UPDATE
            </Button>
        </Grid>
    </form>
    <Snackbar
        open={state.openSnack}
        message="You have successfully updated this listing!"
        anchorOrigin={{
            vertical: "bottom",
            horizontal: "center",
        }}
    />
</Box>
  )
}

export default ListingUpdate