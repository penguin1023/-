import streamlit as st

st.set_page_config(
    page_title="축구",
    layout="centered"
)

st.title("축구")

team = st.text_input("응원팀을 입력하세요")

player = st.text_input("좋아하는 선수를 입력하세요")

table = st.number_input("리그 예상 순위를 입력하세요")

trophy = st.selectbox("우승 트로피를 고르세요", ["리그", "리그컵", "챔스", "무관"])

st.markdown("---")
st.subheader("입력 결과 확인")

if team:
  st.write(f"응원팀: {team}")

if player:
  st.write(f"최애선수: {player}")

if table:
  st.write(f"순위: {int(table)}")

if trophy:
  st.write(f"트로피: {trophy}")
