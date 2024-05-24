# Installing Dependencies
import os
from environ import apikey
import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# UI setup
st.title('Basic Chatbot')
prompt = st.text_input('Enter Prompt')