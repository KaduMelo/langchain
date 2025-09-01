from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

system = ("system", "You are an assistant that answers questions in a {style} style.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="friendly", question="What is a good name for a company that makes resume on whatszapp?")

for message in messages:
    print(f"{message.type}: {message.content}")

# Updated model name to the correct Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
response = model.invoke(messages)
print("Response:", response.content)