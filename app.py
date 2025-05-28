import streamlit as st
import openai

# 🔐 Load your API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 🧠 Title of your app
st.title("Ask AI Anything")

# 📝 Input box for user prompt
user_input = st.text_input("Ask something:")

# 🔘 Button to send the prompt
if st.button("Submit"):
    if user_input:
        # 🤖 Send the message to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        # 📤 Show the response
        st.write("AI:", response["choices"][0]["message"]["content"])
