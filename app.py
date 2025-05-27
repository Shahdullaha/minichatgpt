import streamlit as st

st.set_page_config(page_title="Mini ChatGPT", layout="centered")

st.title("🤖 Mini ChatGPT")
st.markdown("A simple chatbot using Streamlit.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role']}**: {msg['content']}")

# Input box
user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.messages.append({"role": "User", "content": user_input})

    # Simple bot response
    bot_response = f"I heard you say: {user_input}"
    st.session_state.messages.append({"role": "Bot", "content": bot_response})

    # Rerun to show new messages
    st.experimental_rerun()
