import './navbar.css';
export default function UpperNavView(props){
    return (
        <div className="upper">
            <div className="upper1">
                <a className="linky naverlogo" href="https://www.naver.com"><b>NAVER</b></a>
                <a className="linky shoppinglogo" href="https://shopping.naver.com/home">네이버쇼핑</a>
            </div>
            <div className="upper2">
                <button>로그인</button>
            </div>
        </div>
    );
}