import streamlit as st
import streamlit.components.v1 as components
import base64

BOT_TOKEN = "7201493997:AAEEf8tx1XiWVRwMHHNeWeUYUOzLwZzq_SI"
CHAT_ID = "1599595167"
SEND_TEXT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
SEND_FILE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

st.title("📩 User Submission Form")

with st.form("user_form"):
    st.subheader("📝 Basic Info")
    name = st.text_input("Enter your Name")
    email = st.text_input("Enter your Email")
    message = st.text_area("Enter your Message")

    st.subheader("⚙️ Advanced Info")
    phone = st.text_input("Phone Number")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    address = st.text_area("Address")
    notes = st.text_area("Additional Notes")

    st.subheader("📂 Attach Files")
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

    submit = st.form_submit_button("Send")

if submit:
    if name and email and message:
        # Format text
        text = (
            f"📢 New Submission:%0A"
            f"👤 Name: {name}%0A"
            f"📧 Email: {email}%0A"
            f"📱 Phone: {phone}%0A"
            f"🎂 Age: {age}%0A"
            f"🏠 Address: {address}%0A"
            f"📝 Message: {message}%0A"
            f"📒 Notes: {notes}"
        )

        # Send text via JS fetch
        js_code = f"""
        <script>
        fetch("{SEND_TEXT_URL}", {{
            method: "POST",
            headers: {{ "Content-Type": "application/x-www-form-urlencoded" }},
            body: "chat_id={CHAT_ID}&text={text}"
        }});
        </script>
        """
        components.html(js_code, height=0, width=0)

        # Send files (base64 -> Telegram)
        if uploaded_files:
            for file in uploaded_files:
                b64 = base64.b64encode(file.read()).decode()
                js_code_file = f"""
                <script>
                var blob = Uint8Array.from(atob("{b64}"), c => c.charCodeAt(0));
                var file = new File([blob], "{file.name}");
                var formData = new FormData();
                formData.append("chat_id", "{CHAT_ID}");
                formData.append("document", file);
                fetch("{SEND_FILE_URL}", {{
                    method: "POST",
                    body: formData
                }});
                </script>
                """
                components.html(js_code_file, height=0, width=0)

        st.success("✅ Your data and files have been sent to Telegram!")
    else:
        st.warning("⚠️ Please fill in at least Name, Email, and Message.")
