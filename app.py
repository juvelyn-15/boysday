import streamlit as st
import streamlit.components.v1 as components
import requests

def save_join(name):
    with open('save.txt', 'a') as file:
        file.write(f"{name} tham gia \n")
def save_not_join(name): 
    with open('save.txt', 'a') as file:
        file.write(f"{name} khong tham gia \n")

WEBHOOK_URL = "https://discord.com/api/webhooks/1370273647658532934/yzdW2MFdHA0Qvz_CdudVuTWHevbT1PH1M4jpRuohj8VLKg_fY12epGhxWD-OjKGZAtXV"

def notify_discord(name, status):
    content = f"🚨 **{name}** đã **{status}**!"
    data = {"content": content}
    requests.post(WEBHOOK_URL, json=data)
# Apply background image using base64
st.image('bg.png')
name = st.text_input("Nhập tên của bạn: ")
# Display it using Streamlit
col1, col2, col3 = st.columns([1, 2, 1])  # center = col2
with col1:
    if st.button('THAM GIA'):
        if name.strip() != "":
            notify_discord(name, "tham gia")
            #save_join(name)
            st.balloons()  # 🎈 Show balloons!
        else:
            st.warning("Nhập tên trước nha!")
with col2:
    if st.button("HẸN LẦN SAU NHÉ!"):
        if name.strip() != "":
            notify_discord(name, 'khong tham gia')
            #save_not_join(name)
            st.toast("Hẹn gặp bạn lần sau nhé!")  # optional friendly message
        else:
            st.warning("Nhập tên trước nha!.")



