import streamlit as st
import requests

# Telegram bot details
BOT_TOKEN = "7201493997:AAEEf8tx1XiWVRwMHHNeWeUYUOzLwZzq_SI"
CHAT_ID = "1599595167"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_to_telegram(name, email, message):
    """Send message to Telegram bot."""
    text = f"📢 New Submission:\n\n👤 Name: {name}\n📧 Email: {email}\n💬 Message: {message}"
    response = requests.post(TELEGRAM_URL, data={"chat_id": CHAT_ID, "text": text})
    return response.status_code == 200

st.title("📩 Send Your Details")

# Streamlit form
with st.form("user_form"):
    name = st.text_input("Enter your Name")
    email = st.text_input("Enter your Email")
    message = st.text_area("Enter your Message")
    submit = st.form_submit_button("Send")

if submit:
    if name and email and message:
        if send_to_telegram(name, email, message):
            st.success("✅ Your data has been sent successfully!")
        else:
            st.error("❌ Failed to send message. Please try again.")
    else:
        st.warning("⚠️ Please fill in all fields.")
