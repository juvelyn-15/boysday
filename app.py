import streamlit as st
import streamlit.components.v1 as components


def save_join(name):
    with open('save.txt', 'a') as file:
        file.write(f"{name} tham gia \n")
def save_not_join(name): 
    with open('save.txt', 'a') as file:
        file.write(f"{name} khong tham gia \n")
# Apply background image using base64
st.image('bg.png')
name = st.text_input("Nhập tên của bạn: ")
# Display it using Streamlit
col1, col2, col3 = st.columns([1, 2, 1])  # center = col2
with col1:
    if st.button('THAM GIA'):
        if name.strip() != "":
            save_join(name)
            st.balloons()  # 🎈 Show balloons!
        else:
            st.warning("Vui lòng nhập tên trước khi chọn.")
with col2:
    if st.button("HẸN LẦN SAU NHÉ!"):
        if name.strip() != "":
            save_not_join(name)
            st.toast("Hẹn gặp bạn lần sau nhé!")  # optional friendly message
        else:
            st.warning("Vui lòng nhập tên trước khi chọn.")



