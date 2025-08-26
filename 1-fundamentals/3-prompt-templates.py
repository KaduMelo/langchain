from langchain.prompts import PromptTemplate    

template = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

text = template.format(product="resume on whatszapp")
print(text)

