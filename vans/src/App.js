import Navbar from './components/Navbar/NavbarPresenter';
import Footbar from './components/Footbar/FootbarPresenter';
import Main from './components/Main/MainPresenter';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import QnA from './components/QnA/QnAPresenter';
import Info from './components/Info/InfoPresenter'
function App() {
  return (
    <div>
        <Navbar/>
        <Routes>
          <Route path='*' element={<Main/>}/>
          <Route path='/qna' element={<QnA/>}/>
          <Route path='/info' element={<Info/>}/>
        </Routes>
        <Footbar/>
    </div>
  );
}

export default App;
