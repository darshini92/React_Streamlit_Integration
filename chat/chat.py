import streamlit as st
from datetime import datetime

# Set up the Streamlit app with a custom theme
st.set_page_config(page_title="Welcome to Vidi", layout="wide")
st.title("Chat with Us 💬")

# Define a function to manage chat history
def chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    return st.session_state.messages

# Display the chat messages with improved styling
messages = chat_history()
for message in messages:
    user, text, time = message
    if user == "user":
        st.markdown(f"""
        <div style='display: flex; align-items: flex-start; margin-bottom: 10px;'>
            <div style='background-color: #DCF8C6; padding: 10px; border-radius: 10px; max-width: 70%;'>
                <strong>You:</strong> {text}<br><span style='font-size: 0.8em; color: gray;'>{time}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='display: flex; align-items: flex-start; margin-bottom: 10px; justify-content: flex-end;'>
            <div style='background-color: #E1E1E1; padding: 10px; border-radius: 10px; max-width: 70%;'>
                <strong>Bot:</strong> {text}<br><span style='font-size: 0.8em; color: gray;'>{time}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Add a separator line for better layout separation
st.markdown("<hr style='border: 1px solid #DDD;' />", unsafe_allow_html=True)

# Create an input box for the user to enter their message
st.markdown("## Send a message")
user_input = st.text_input("Type your message here...", key="input")

# Handle the message when the user submits it
if st.button("Send"):
    if user_input:
        timestamp = datetime.now().strftime('%H:%M:%S')
        st.session_state.messages.append(("user", user_input, timestamp))
        # Simulate a bot response (you can replace this with actual bot logic)
        bot_response = f"Echo: {user_input}"
        st.session_state.messages.append(("bot", bot_response, timestamp))
        st.session_state.input = ""  # Clear the input box
