import './navbar.css';
import items from './NavbarItem.js';
import {Link} from 'react-router-dom';

function Tab(props){
    return (
            <li className={props.char}><Link to={props.url}>{props.title}</Link></li>
    )
}
export default function LowerNavView(props){
    function itemTab(item){
        return Tab(item);
    }
    return (
        <ul className="lowertab">
            {items.map(itemTab)}
        </ul>
    );
}