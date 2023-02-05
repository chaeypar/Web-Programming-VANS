import './info.css';
import VansView from './vansView';

export default function infoView(props){
    return (
        <div className="infocont">
            <div className="infotitle">
                소개 페이지
            </div>
            <div className="infocontent">
                <VansView/>
                <div className="infodatalab">

                </div>
            </div>
        </div>
    );
};