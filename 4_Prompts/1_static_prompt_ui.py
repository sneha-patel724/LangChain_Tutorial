from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

st.header("Research Tool")
user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = model.invoke(user_input)
            
            # 1. Access the text specifically
            # Some versions return a list of parts, we want the text part.
            if isinstance(result.content, list):
                clean_text = result.content[0].get("text", "")
            else:
                clean_text = result.content
            
            # 2. Display it nicely
            st.markdown("### Research Summary")
            st.info(clean_text)
    else:
        st.warning("Please enter a prompt first!")