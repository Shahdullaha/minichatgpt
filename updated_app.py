
import streamlit as st

st.set_page_config(page_title="Mini ChatGPT", layout="centered")

st.title("🤖 Mini ChatGPT")
st.markdown("A simple chatbot using Streamlit.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages with chat format
for msg in st.session_state.messages:
    with st.chat_message(msg["role"].lower()):
        st.markdown(msg["content"])

# Input box at the bottom
user_input = st.chat_input("Ask me something...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "User", "content": user_input})

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response logic
    bot_response = f"I heard you say: {user_input}"

    # Save bot message
    st.session_state.messages.append({"role": "Bot", "content": bot_response})

    # Show bot response
    with st.chat_message("bot"):
        st.markdown(bot_response)
