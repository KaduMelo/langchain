from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

model = OpenAI(model_name="o1-mini-2024-09-12", temperature=0.5)
message = model.invoke("Hello, world!")

print(message.content)