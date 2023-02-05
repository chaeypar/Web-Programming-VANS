import './info.css';
import image from '../../image/instagram.png';

export default function VansView(props){
    return (
        <div className="vansinfo">
            <div className="vanstitle">
                <div className="vansmain">
                    <strong className="vansname">반스 공식 온라인스토어</strong><span className='good_service'>굿서비스</span>
                </div>
                <div className="vanssub">오리지널 액션 스포츠 브랜드 VANS의 공식 온라인스토어입니다.</div>
                <div className="channel">
                    <div className="channeltitle">연관 채널</div>
                    <img className="instagram_logo" src={image} alt="Instagram logo"/>
                    <a className="insta_adress" rel="noreferrer" target="_blank" href="https://instagram.com/vans_korea">https://instagram.com/vans_korea</a>
                </div>
            </div>
            <div className="vanscontent">
                <div className="content_title">
                    사업자정보
                </div>
                <div className="content_info">
                    <div className="info_left">
                        <div className="info_sub">
                            <div className="info_sub_1">상호명</div>
                            <div className="info_sub_2">유한회사 브이에프코리아</div>
                        </div>
                        <div className="info_sub">
                            <div className="info_sub_1">대표자</div>
                            <div className="info_sub_2">TZE CHOI THEODORE PANG</div>
                        </div>
                        <div className="info_sub">
                            <div className="info_sub_1">고객센터</div>
                            <div className="info_sub_2">

                            </div>
                        </div>
                    </div>
                    <div className="info_right">
                        <div className="info_sub">
                            <div className="info_sub_3">사업자등록번호</div>
                            <div className="info_sub_4">2208843561</div>
                        </div>
                        <div className="info_sub">
                            <div className="info_sub_3">사업장 소재지</div>
                            <div className="info_sub_4">서울특별시 강남구 테헤란로 317 (동훈타워) 18층 (우: 16151)</div>
                        </div>
                        <div className="info_sub">
                            <div className="info_sub_3">통신판매업번호</div>
                            <div className="info_sub_4">2013-서울강남-02918</div>
                        </div>
                        <div className="info_sub">
                            <div className="info_sub_3">e-mail</div>
                            <div className="info_sub_4">sail173@naver.com</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};
