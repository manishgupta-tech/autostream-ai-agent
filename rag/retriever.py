from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from rag.loader import load_documents


def create_retriever():
    docs = load_documents()

    embedding_model = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embedding_model)

    return vectorstore.as_retriever(search_kwargs={"k": 2})