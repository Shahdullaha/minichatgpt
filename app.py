import streamlit as st
import openai

# Access your API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

st.write(response["choices"][0]["message"]["content"])
