import streamlit as st

st.title("SUPERKAZUMIBROS.")
st.title("暗号メモ")

user_input1=st.text_input("問題１の暗号")
user_input2=st.text_input("問題２の暗号")
user_input3=st.text_input("問題３の暗号")   
user_input4=st.text_input("問題４の暗号")

st.write("すべての暗号")
st.write(user_input1,user_input2,user_input3,user_input4)
