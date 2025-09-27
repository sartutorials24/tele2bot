import streamlit as st
import streamlit.components.v1 as components

BOT_TOKEN = "7201493997:AAEEf8tx1XiWVRwMHHNeWeUYUOzLwZzq_SI"
CHAT_ID = "1599595167"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

st.title("📩 Send Your Details")

with st.form("user_form"):
    name = st.text_input("Enter your Name")
    email = st.text_input("Enter your Email")
    message = st.text_area("Enter your Message")
    submit = st.form_submit_button("Send")

if submit:
    if name and email and message:
        js_code = f"""
        <script>
        fetch("{TELEGRAM_URL}", {{
            method: "POST",
            headers: {{ "Content-Type": "application/x-www-form-urlencoded" }},
            body: "chat_id={CHAT_ID}&text=📢 New Submission:%0A👤 Name: {name}%0A📧 Email: {email}%0A💬 Message: {message}"
        }})
        .then(r => r.json())
        .then(data => console.log(data));
        </script>
        """
        components.html(js_code, height=0, width=0)
        st.success("✅ Your data has been sent successfully!")
    else:
        st.warning("⚠️ Please fill in all fields.")
