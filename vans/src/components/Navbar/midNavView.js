import vans from '../../image/Vans_Logo.png';
import search from '../../image/search.png';

import './navbar.css';

export default function MidNavView(props){
    return (
        <div className="mid">

            <img className="logo" src={vans} alt="vans logo"/>
            <div className="searchset">
                <input className="search1" placeholder="검색어를 입력해보세요"/>
                <img className="search2" src={search} alt="search"/>
            </div>
        </div>
    )
}