import { MapContainer, TileLayer, useMap, Marker,Popup,Polygon } from 'react-leaflet'

// Boroughs
import Camden from "../../../Assets/Boroughs/Camden";
import Greenwich from "../../../Assets/Boroughs/Greenwich";
import Hackney from "../../../Assets/Boroughs/Hackney";
import Hammersmith from "../../../Assets/Boroughs/Hammersmith";
import Islington from "../../../Assets/Boroughs/Islington";
import Kensington from "../../../Assets/Boroughs/Kensington";
import Lambeth from "../../../Assets/Boroughs/Lambeth";
import Lewisham from "../../../Assets/Boroughs/Lewisham";
import Southwark from "../../../Assets/Boroughs/Southwark";
import City_of_London from "../../../Assets/Boroughs/City_of_London";
import Hamlets from "../../../Assets/Boroughs/Hamlets";
import Wandsworth from "../../../Assets/Boroughs/Wandsworth";
import Westminster from "../../../Assets/Boroughs/Westminster";
import Barking from "../../../Assets/Boroughs/Barking";
import Barnet from "../../../Assets/Boroughs/Barnet";
import Bexley from "../../../Assets/Boroughs/Bexley";
import Brent from "../../../Assets/Boroughs/Brent";
import Bromley from "../../../Assets/Boroughs/Bromley";
import Croydon from "../../../Assets/Boroughs/Croydon";
import Ealing from "../../../Assets/Boroughs/Ealing";
import Enfield from "../../../Assets/Boroughs/Enfield";
import Haringey from "../../../Assets/Boroughs/Haringey";
import Harrow from "../../../Assets/Boroughs/Harrow";
import Havering from "../../../Assets/Boroughs/Havering";
import Hillingdon from "../../../Assets/Boroughs/Hillingdon";
import Hounslow from "../../../Assets/Boroughs/Hounslow";
import Kingston from "../../../Assets/Boroughs/Kingston";
import Merton from "../../../Assets/Boroughs/Merton";
import Newham from "../../../Assets/Boroughs/Newham";
import Redbridge from "../../../Assets/Boroughs/Redbridge";
import Richmond from "../../../Assets/Boroughs/Richmond";
import Sutton from "../../../Assets/Boroughs/Sutton";
import Waltham from "../../../Assets/Boroughs/Waltham";

import {useImmerReducer} from 'use-immer';
import {ReducerFuction} from './Reducer'
import { initialState } from './InitialState';




function BoroughDisplay() {
    const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
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


export {BoroughDisplay}