import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") or input("Enter your LangChain API key: ")
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY") or input("Enter your Mistral API key: ")

if not os.environ["LANGCHAIN_API_KEY"] or not os.environ["MISTRAL_API_KEY"]:
    raise ValueError("Both LANGCHAIN_API_KEY and MISTRAL_API_KEY must be set.")

model=ChatMistralAI(model='mistral-large-latest')
model2=ChatMistralAI(model='pixtral-large-latest')

# human=HumanMessage(content='Hi ! i am Vero ')

# output=model.invoke([human])
# output2=model2.invoke([human])

output=model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

print(output.content)
# print(output2.content)

