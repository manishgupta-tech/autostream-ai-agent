import json
from langchain_core.documents import Document

def load_documents():
    with open("data/knowledge.json", "r") as f:
        data = json.load(f)

    documents = []

    for plan in data["plans"]:
        content = f"""
        {plan['name']}:
        Price: {plan['price']}
        Features: {', '.join(plan['features'])}
        """
        documents.append(Document(page_content=content.strip()))

    for policy in data["policies"]:
        documents.append(Document(page_content=policy))

    return documents