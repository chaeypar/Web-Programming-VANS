import FootbarItem from "./FootbarItem";
import './footbar.css';

export default function FootbarView(props){
    const style1={textDecoration: 'none', padding: "0px 4px", fontWeight: 'bold', color: 'inherit', fontSize: '12px'}
    const style2={textDecoration: 'none', padding: "0px 4px", color: 'inherit', fontSize: '13px'}
    function infoMap(item){
        return (
            <div classsName={item.char}><a target="_blank" href={item.url} style={item.char==='normal'?style2:style1}>{item.title}</a></div>
        )
    }
    return (
        <div className="footbarcont">
            <div className="footbar1">
                <div className="footbar1_1">
                    반품 배송비, 반품 배송주소 등은 해당 상품 페이지 내 안내를 참고해주세요.
                </div>
                <div className="footbar1_2">
                    유한회사 브이에프코리아 1522-1882 <span className="blue">인증</span>
                    <button>잘못된 번호 신고</button> 판매자정보
                </div>
            </div>
            <div className="footbar2">
                {FootbarItem.map(infoMap)}
            </div>
            <div className="footbar3">

            </div>
            <div className="footbar4">
                <div className="footbar4_1">
                  네이버(주)는 통신판매중개자이며, 통신판매의 당사자가 아닙니다. 상품, 상품정보, 거래에 관한 의무와 책임은 판매자에게 있습니다. <a className="detail" target="_blank" href="https://help.pay.naver.com/faq/content.help?faqId=10909">자세히 보기</a>
                </div>
                <div className="footbar4_2">
                    <div className="footbar4_2_1">
                        Naver
                    </div>
                    <div className="footbar4_2_2">
                        Copyright © <a target="_blank" href="http://www.navercorp.com/" >Naver Corp.</a> All rights Reserved.
                    </div>
                </div>
            </div>
        </div>
    );
};