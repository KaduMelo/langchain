import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()
for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise ValueError(f"Please set the {k} environment variable in the .env file")
    
query = "Tell me about the gpt-5 thinking evalution and performance results comparing to gpt-4"

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

results = store.similarity_search_with_score(query, k=10)

for i, (doc, score) in enumerate(results, start=1):
    print("="*50)
    print(f"Document {i} (Score: {score:.2f}):")
    print("-"*50)
    
    print("\nText:\n")
    print(doc.page_content.strip())

    print("\nMetadata:\n")
    for key, value in doc.metadata.items():
        print(f"{key}: {value}")
