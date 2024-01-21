import streamlit as st
from twilio.rest import Client

# Twilio credentials
account_sid = 'AC260e7f002c79dc8d82b9fd5c2b94be78'
auth_token = '2c383cba5689336165d4048accbf6a18'
twilio_phone_number = '+9609844800'

# Function to send SMS
def send_sms(to, body):
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            to=to,
            from_=twilio_phone_number,
            body=body
        )
        return message.sid
    except Exception as e:
        return str(e)

# Streamlit app
def main():
    st.title("SMS Sender App with Twilio")

    # User input
    recipient_number = st.text_input("Enter recipient's phone number:")
    message_body = st.text_area("Enter your message:")

    # Send SMS button
    if st.button("Send SMS"):
        if recipient_number and message_body:
            result = send_sms(recipient_number, message_body)
            st.success(f"SMS sent successfully! SID: {result}")
        else:
            st.warning("Please enter recipient's number and message.")

if __name__ == "__main__":
    main()
