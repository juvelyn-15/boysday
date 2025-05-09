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
        save_join(name)
with col2:
    if st.button("HẸN LẦN SAU NHÉ!"):
        save_not_join(name)



