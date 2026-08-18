import streamlit as st
import random
import os

# 1. UI 설정
st.set_page_config(page_title="WITT-GEN", layout="centered")

# 2. 전체 디자인 & 네온 CSS
st.markdown(
    """
    <style>
    .stApp { background-color: #050505; }
    
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        text-align: center;
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
        margin-top: 50px;
        margin-bottom: 40px;
    }
    
    .quote-container {
        padding: 3rem;
        border: 3px solid #00d2ff;
        border-radius: 25px;
        box-shadow: 0 0 25px #00d2ff, inset 0 0 25px #00d2ff;
        text-align: center;
        color: white;
        font-size: 2rem;
        font-weight: bold;
        font-family: 'Pretendard', sans-serif;
        background: rgba(0, 210, 255, 0.05);
        margin-bottom: 40px;
    }

    .stButton > button {
        width: 100%;
        height: 70px;
        background: transparent !important;
        border: 2px solid #00d2ff !important;
        border-radius: 15px !important;
        color: #00d2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        box-shadow: 0 0 15px #00d2ff, inset 0 0 15px #00d2ff !important;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: #00d2ff !important;
        color: #050505 !important;
        box-shadow: 0 0 30px #00d2ff, 0 0 60px #00d2ff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. 데이터 로드 (생략 없이 그대로 유지)
QUOTES = [
    "나는 똑똑한 척하는 멍청이들을 아주 많이 알고 있다. - 일론 머스크",
    "혁신은 '아니오'라고 말하는 데서 시작된다. - 스티브 잡스",
    "가장 위대한 발견은, 사람이 우연히 하던 일을 멈추고 다른 일을 하다가 일어난다. - 알렉산더 그레이엄 벨",
    "인생은 불공평하다. 그 사실에 익숙해져라. - 빌 게이츠",
    "성공의 80%는 그냥 모습을 드러내는 것이다. - 우디 앨런",
    "내가 아는 유일한 사실은 내가 아무것도 모른다는 사실이다. - 소크라테스",
    "이봐, 해봤어? - 정주영",
    "성공한 사람들의 특징? 운이 좋았다고 말하는 겸손함이다.",
    "노력은 배신하지 않는다. 단지 너를 배신한 것처럼 보일 뿐이다.",
    "오늘 할 수 있는 일을 내일로 미루면, 내일은 오늘 할 수 있는 일보다 더 많아진다.",
    "천재는 노력하는 사람을 이길 수 없고, 노력하는 사람은 즐기는 사람을 이길 수 없다. 그리고 즐기는 사람은 그냥 타고난 놈을 이길 수 없다.",
    "기회가 문을 두드릴 때, 너는 이미 그 문을 열고 있어야 한다. - 밀턴 버를",
    "미래는 예측하는 것이 아니라, 만드는 것이다. - 피터 드러커",
    "남들이 불가능하다고 말할 때, 그게 바로 시작점이다. - 일론 머스크",
    "당신의 시간은 한정되어 있다. 남의 인생을 사느라 낭비하지 마라. - 스티브 잡스",
    "성공한 사람들은 끊임없이 앞으로 나아간다. 실패하는 사람들은 계속 변명한다. - 벤저민 프랭클린",
    "꿈을 크게 가져라. 작은 꿈은 사람의 심장을 움직이지 못한다. - 요한 볼프강 폰 괴테",
    "행동하지 않는 지식은 쓸모없다. - 토마스 에디슨",
    "인생은 짧게 살되, 개같이 살지 마라. - 오스카 와일드",
    "나는 결코 실수하지 않는다. 나는 의도적으로 이상한 결정을 내린다. - 찰스 부코스키",
    "사람은 누구나 미쳐 있다. 단지 어떤 미침이 더 재밌느냐의 차이다. - 프리드리히 니체",
    "세상은 미치광이들의 소굴이다. 그리고 그 미치광이들이 규칙을 만든다. - 마크 트웨인",
    "내가 아는 가장 큰 비극은, 사람들이 자신이 똑똑하다고 믿는 것이다. - 조지 오웰",
    "인간은 생각하는 동물이 아니라, 생각하는 척하는 동물이다. - 쇼펜하우어",
    "성공이란, 실패를 반복하면서도 열정을 잃지 않는 능력이다. - 윈스턴 처칠",
    "나는 미래가 두렵지 않다. 미래가 나를 두려워했으면 좋겠다. - 알베르트 아인슈타인",
    "모든 사람은 천재다. 단, 물고기를 나무 오르기 능력으로 평가하면 물고기는 평생 자신이 멍청하다고 믿을 것이다. - 알베르트 아인슈타인",
    "인생은 담배 한 개비와 같다. 너무 빨리 타들어가고, 결국 재만 남는다. - 장 폴 사르트르",
    "나는 결코 늙지 않는다. 나는 단지 더 복잡해질 뿐이다. - 파블로 피카소",
    "세상은 공평하지 않다. 그래서 내가 더 열심히 불공평하게 산다. - 찰스 부코스키",
    "사람들이 너를 비웃을 때, 그게 네가 제대로 가고 있다는 증거다. - 오스카 와일드",
    "나는 신을 믿지 않는다. 하지만 신을 믿는 사람들을 더욱 믿지 않는다. - 프리드리히 니체",
    "인간은 자유롭게 태어났으나, 어디서나 사슬에 묶여 있다. 그 사슬을 스스로 찬 경우가 제일 많다. - 장 자크 루소",
    "나는 절대 실수하지 않는다. 나는 단지 예상치 못한 결과를 만들어낼 뿐이다. - 찰스 부코스키",
    "인생은 너무 짧아서 진지하게 살 여유가 없다. - 오스카 와일드",
    "사람은 누구나 미쳤다. 단지 남들이 알아채지 못하게 잘 숨기는 놈이 정상인 취급을 받는다. - 마크 트웨인",
    "나는 신을 만나본 적이 없다. 그런데 신을 만났다는 사람들은 대부분 정신병원에 있다. - 프리드리히 니체",
    "미래는 이미 와 있다. 단지 아직 모두에게 골고루 배분되지 않았을 뿐이다. - 윌리엄 깁슨",
    "나는 실패를 두려워하지 않는다. 실패를 성공이라고 부르는 사람들을 두려워한다. - 그로초 마르크스",
    "세상은 미치광이들로 가득하다. 문제는 그 미치광이들이 규칙을 만들고 있다는 점이다. - 마크 트웨인",
    "인간이 생각하는 동물이라는 주장은, 인간이 스스로에게 한 가장 큰 거짓말이다. - 쇼펜하우어",
    "나는 결코 늙지 않는다. 나는 단지 더 이상해질 뿐이다. - 살바도르 달리",
    "성공한 사람들의 가장 큰 특징은, 자신이 운이 좋았다고 말하는 겸손함이다. 그 말은 대부분 거짓이다. - 나심 탈레브",
    "인생은 담배와 같다. 너무 빨리 타들어가고, 결국 재만 남는다. 그래도 피운다. - 장 폴 사르트르",
    "사람들이 너를 비웃기 시작하면, 그때가 바로 네가 제대로 된 길을 가고 있다는 신호다. - 오스카 와일드",
    "나는 절대 죽지 않을 것이다. 나는 단지 더 이상 참석하지 않을 뿐이다. - 우디 앨런",
    "세상은 공평하지 않다. 그래서 나는 더 불공평하게 살기로 결심했다. - 찰스 부코스키",
    "인간의 가장 큰 문제는, 자신이 이성적이라고 믿는 것이다. - 시몬 드 보부아르"
]

st.markdown('<h1 class="neon-title">⚡ WITT-GEN</h1>', unsafe_allow_html=True)

# 4. 상태 관리
if 'quote' not in st.session_state:
    st.session_state.quote = random.choice(QUOTES)

# 명언 출력 박스
st.markdown(f'<div class="quote-container">{st.session_state.quote}</div>', unsafe_allow_html=True)


if st.button("🚀 드립 뽑기"):
    st.session_state.quote = random.choice(QUOTES)
