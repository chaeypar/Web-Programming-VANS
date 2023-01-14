import MidNavView from "./midNavView";
import UpperNavView from "./upperNavView";
import LowerNavView from './lowerNavView';

export default function Navbar(props){
    return (
        <div className="navbar">
            <UpperNavView/>
            <MidNavView/>
            <LowerNavView/>
        </div>
    )
}