from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

system = ("system", "You are an assistant that answers questions in a {style} style.")
user = ("user", "{question}")

question_template = PromptTemplate(
    input_variables=["name"],
    template="What is a good name for a company that makes {name}?",
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

chain = question_template | model

result = chain.invoke({"name": "resume on whatszapp"})
print(result.content)