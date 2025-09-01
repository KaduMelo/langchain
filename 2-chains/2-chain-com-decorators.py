from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import chain
from dotenv import load_dotenv
load_dotenv()

@chain
def square(input_dict: dict) -> dict:
    x = input_dict["x"]
    return { "square_result": x * x }

@chain
def square_root(input_dict: dict) -> dict:
    square_result = input_dict["square_result"]
    return { "square_root_result": square_result ** 0.5 }

question_template = PromptTemplate(
    input_variables=["name"],
    template="What is a good name for a company that makes {name}?",
)

question_template2 = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}?",
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

chain = question_template | model
chain2 = square | question_template2 | model

result = chain2.invoke({ "x": 10 })
print(result.content)