import { BrowserRouter, Route, Routes} from 'react-router-dom';
import logo from './logo.svg';
import {useImmerReducer} from 'use-immer';
import './App.css';
import React, {useEffect} from 'react';
import Home from './components/pages/Home';
import Listings from "./components/Listing/Listings";
import NewListing from "./components/Listing/NewListing";
import SignIn from './components/profile/SignIn';
import SignUp from './components/profile/SignUp';
import Testing from './components/pages/Testing';
import DispatchContext from './Context/DispatchContext';
import stateContext from './Context/StateContext';
import Profile from './components/profile/Profile';
import Agencies from './components/agencies/Agencies';
import AgencyDetail from './components/agencies/AgencyDetail';
import ListingDetail from './components/Listing/ListingDetail'
import {initialState} from './components/elements/utils/InitialState'

function App() {
  const initialState = { 
    userUsername: localStorage.getItem('TheUserUsername'),
    userEmail:localStorage.getItem('TheUserEmail'), 
    userId:localStorage.getItem('TheUserId'), 
    userToken:localStorage.getItem('TheUserToken'),
    userIsLogged: localStorage.getItem('TheUserUsername') ? true : false,
  }




  function ReducerFuction(draft, action) {
    switch (action.type) {
        case 'catchToken':
          draft.userToken = action.tokenValue
          break;
        case 'userSignIn':
          draft.userUsername = action.usernameInfo;
          draft.userEmail = action.emailInfo;
          draft.userId = action.idInfo;
          draft.userIsLogged = true;
          break;
        case 'userLogOut': 
          draft.userIsLogged = false;
          break;
        default: break;
    }
  }
  const [state, dispatch] = useImmerReducer(ReducerFuction, initialState);
  useEffect((()=>{
    if(state.userIsLogged){
      localStorage.setItem('TheUserUsername', state.userUsername)
      localStorage.setItem('TheUserEmail', state.userUserEmail)
      localStorage.setItem('TheUserId', state.userId)
      localStorage.setItem('TheUserToken', state.userToken)
    } else{
      localStorage.removeItem('TheUserUsername')
      localStorage.removeItem('TheUserEmail')
      localStorage.removeItem('TheUserId')
      localStorage.removeItem('TheUserToken')
    }

  }),[state.userIsLogged])
  return (
    <stateContext.Provider value={state}>
  <DispatchContext.Provider value={dispatch}> 
  <BrowserRouter>
  <Routes>
    <Route path='/' element={<Home/>}/>
    <Route path='/listings' element={<Listings/>}/>
    <Route path='/newlisting' element={<NewListing/>}/>
    <Route path='/profile' element={<Profile/>}/>
    <Route path='/signIn' element={<SignIn/>}/>
    <Route path='/signUp' element={<SignUp/>}/>
    <Route path='/testing' element={<Testing/>}/>
    <Route path='/agencies' element={<Agencies/>}/>
    <Route path='/agencies/:id' element={<AgencyDetail/>}/>
    <Route path='/listings/:id' element={<ListingDetail/>}/>

  </Routes>
  </BrowserRouter>
  </DispatchContext.Provider> 
  </stateContext.Provider>
  );
}

export default App;