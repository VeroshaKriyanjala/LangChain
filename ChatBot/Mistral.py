import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment
mistral_api_key = os.getenv("MISTRAL_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

if not mistral_api_key:
    raise ValueError("MISTRAL_API_KEY is not set in the .env file")

# Initialize the language model
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
)

# Create the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful coding assistant. Generate code based on the comment provided."),
    ("human", "{input}"),
])

# Set up Streamlit UI
st.title("Code Assistant")

# Initialize session state for the input and output
if "full_text" not in st.session_state:
    st.session_state["full_text"] = ""

# Text area for user input and output
updated_text = st.text_area(
    "Write a comment in the first line. The generated code will appear below.",
    value=st.session_state["full_text"],
    height=300,
    key="code_text",
)

# Check if the user has provided a comment (first line)
if updated_text.strip():
    # Extract the first line (comment)
    lines = updated_text.split("\n")
    first_line_comment = lines[0].strip()

    # Generate code only if the first line is a comment
    if first_line_comment:
        chain = prompt | llm
        ai_msg = chain.invoke({"input": first_line_comment})
        generated_code = ai_msg.content.strip()

        # Combine the original comment and generated code
        full_text = f"{first_line_comment}\n{generated_code}"

        # Update the session state and text box
        st.session_state["full_text"] = full_text
        st.text_area(
            "Generated Code:",
            value=st.session_state["full_text"],
            height=300,
            key="updated_code_text",
        )
