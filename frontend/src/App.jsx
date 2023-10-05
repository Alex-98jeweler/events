import {BasePage} from './components/BasePage/BasePage'
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Login from './components/Login/Login';
import EventList from './components/Events/EventList';
import EventDetail from './components/Events/EventDetail';
import UserDetail from './components/Users/UserDetail';
import UserList from './components/Users/UserList';
import { useContext, useEffect } from 'react';
import { Context } from './main';
import EmptyComp from './components/BasePage/EmptyComponent';
import { observer } from 'mobx-react-lite';

function App() {
  const {store} = useContext(Context);
  console.log(store.isAuth)


  useEffect(() => {
      if (localStorage.getItem('jwt_token')) {
        console.log("CHECKING")
        store.checkAuth();
      }
    }, []
  )

  if (store.isLoading) {
    return <div>Loading...</div>
  }

  if (!store.isAuth) {
    return (
      <div>
        <Login />
      </div>
    )
  }
    return (
      <>
      <Routes>
        <Route path='/' element={<BasePage />} >
          <Route index element={<EmptyComp />}/>
          <Route path='events' element={<EventList/>}/>
          <Route path='events/:id' element={<EventDetail/>}/>
          <Route path='users' element={<UserList/>}/>
          <Route path='users/:id' element={<UserDetail/>}/>
        </Route>
      </Routes>
      </>
    )
}

export default observer(App);
