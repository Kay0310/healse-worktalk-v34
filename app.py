
import streamlit as st
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="WORK TALK 위험성평가", layout="centered")

st.markdown("### 📷 WORK TALK - 위험성평가 입력")
st.markdown("사진 1장 업로드 ➝ 질문 4개 응답 ➝ 저장 ➝ 다음 사진 순서대로 진행해 주세요.")

with st.form("risk_form"):
    name = st.text_input("이름")
    dept = st.text_input("부서")
    uploaded_file = st.file_uploader("작업 사진 업로드", type=["jpg", "jpeg", "png"])

    q1 = st.text_input("어떤 작업을 하고 있는 건가요?")
    q2 = st.text_input("이 작업은 왜 위험하다고 생각하나요?")
    q3 = st.radio("이 작업은 얼마나 자주 하나요?", ["연 1-2회", "반기 1-2회", "월 2-3회", "주 1회 이상", "매일"])
    q4 = st.radio("이 작업은 얼마나 위험하다고 생각하나요?", [
        "약간의 위험: 일회용 밴드 치료 필요 가능성 있음",
        "조금 위험: 병원 치료 필요. 1-2일 치료 및 휴식",
        "위험: 보름 이상의 휴식이 필요한 중상 가능성 있음",
        "매우 위험: 불가역적 장애 또는 사망 가능성 있음"
    ])

    submitted = st.form_submit_button("저장하기")

if submitted:
    save_path = "/mnt/data/worktalk_results.xlsx"
    new_data = {
        "이름": [name],
        "부서": [dept],
        "작업내용": [q1],
        "위험이유": [q2],
        "빈도": [q3],
        "위험도": [q4],
        "작성일시": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }
    df = pd.DataFrame(new_data)

    if os.path.exists(save_path):
        existing = pd.read_excel(save_path)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(save_path, index=False)
    st.success("저장 완료! 다음 사진을 입력해 주세요.")
