import streamlit as st
import requests

# Telegram bot token and chat ID
BOT_TOKEN = "7201493997:AAEEf8tx1XiWVRwMHHNeWeUYUOzLwZzq_SI"
CHAT_ID = "1599595167"

def send_to_telegram(message: str):
"""Send message to Telegram bot."""
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": message}
response = requests.post(url, data=payload)
return response.json()

def generate_python_code(user_name, company_name, website_url, address, phone_number, feedback, ip_address):
"""Generate Python code that stores user information in variables."""
python_code = f"""
# User Info
user_name = "{user_name}"
company_name = "{company_name}"
website_url = "{website_url}"
address = "{address}"
phone_number = "{phone_number}"
feedback = "{feedback}"
ip_address = "{ip_address}"

# Example function using user data
def display_user_info():
print(f"Name: {user_name}")
print(f"Company: {company_name}")
print(f"Website: {website_url}")
print(f"Address: {address}")
print(f"Phone Number: {phone_number}")
print(f"Feedback: {feedback}")
print(f"IP Address: {ip_address}")

# Call the function
display_user_info()
"""
return python_code

def get_ip_address():
"""Get the public IP address of the user."""
try:
# Using an external API to get the public IP address
response = requests.get('https://api.ipify.org?format=json')
ip_address = response.json().get("ip")
return ip_address
except requests.exceptions.RequestException:
return "Unable to fetch IP"

def main():
st.title("Business Information Collector")

# Collecting user input
user_name = st.text_input("Enter your name:")
company_name = st.text_input("Enter your company name:")
website_url = st.text_input("Enter your company website:")
address = st.text_area("Enter your address:")
phone_number = st.text_input("Enter your phone number:")
feedback = st.text_area("Enter your feedback:")

# Get the user's IP address
ip_address = get_ip_address()

# Button to generate Python code
if st.button("Generate Python Code and Send to Telegram"):
if all([user_name, company_name, website_url, address, phone_number, feedback]):
# Generate Python code
python_code = generate_python_code(user_name, company_name, website_url, address, phone_number, feedback, ip_address)

# Display generated Python code
st.subheader("Generated Python Code:")
st.code(python_code, language="python")

# Prepare the message to send to Telegram
telegram_message = f"""
New business feedback received:
Name: {user_name}
Company: {company_name}
Website: {website_url}
Address: {address}
Phone Number: {phone_number}
Feedback: {feedback}
IP Address: {ip_address}
"""

# Send the message to the Telegram bot
send_to_telegram(telegram_message)

# Confirm message was sent
st.success("The information has been sent to the Telegram bot!")
else:
st.error("Please fill in all the fields!")

if __name__ == "__main__":
main()
