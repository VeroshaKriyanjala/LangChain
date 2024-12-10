import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") or input("Enter your LangChain API key: ")
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY") or input("Enter your Mistral API key: ")

if not os.environ["LANGCHAIN_API_KEY"] or not os.environ["MISTRAL_API_KEY"]:
    raise ValueError("Both LANGCHAIN_API_KEY and MISTRAL_API_KEY must be set.")

model = ChatMistralAI(model="mistral-large-latest")

human_message = HumanMessage(content="Hi! I'm Bob")

output = model.invoke([human_message])

print(output.content)
