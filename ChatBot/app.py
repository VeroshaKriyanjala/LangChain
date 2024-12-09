import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import getpass

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment
mistral_api_key = os.getenv("MISTRAL_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")


if not mistral_api_key:
    raise ValueError("MISTRAL_API_KEY is not set in the .env file")

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
)

prompt=ChatPromptTemplate.from_messages([
    (
        "system",
        "You are as helpful as a coding assistant.",
    ),
    ("human", "{input}"),
])

chain=prompt | llm

st.title("ChatBot")
inputData=st.text_area("User Input", value="", height=100)

ai_msg=chain.invoke(
    {
        "input":inputData
    }
)

outputData=ai_msg.content

st.text_area("AI Output", value=outputData, height=800,disabled=True)
