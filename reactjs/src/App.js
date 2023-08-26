import { BrowserRouter,Routes, Route, Navigate } from "react-router-dom";
import { notification, Button } from 'antd';
import {useState,useEffect} from 'react'

// css
import './App.css';

// views
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import RequireAuth from './components/RequireAuth'
import Home from "./pages/home/Home";



function App() {
  const [token, setToken] = useState(null);
  const [api, contextHolder] = notification.useNotification();

    // useEffect(() => {
    // }, []);

  return (
    <BrowserRouter>
      {contextHolder}
        {token?<div style={{position:'absolute',bottom:'0', margin:'5px'}}><Button danger type="primary" onClick={() => {setToken(null)}}>
            Log out
        </Button></div>:""}
      <div className={'center'}>
          <Routes>
              <Route index element={
                  <RequireAuth token={token}>
                      <Home notif={api} token={token}/>
                  </RequireAuth>
              }/>
              <Route path="/login" element={<Login notif={api}
                  setToken={setToken}/>}
              />
              <Route path="/register" element={<Register notif={api}/>}/>
              <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
