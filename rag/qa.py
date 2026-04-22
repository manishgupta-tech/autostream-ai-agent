from rag.retriever import create_retriever

retriever = create_retriever()

def get_rag_answer(query):
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    return f"""
💡 Here’s what I found for you:

📦 **Basic Plan**
- $29/month
- 10 videos/month
- 720p resolution

🚀 **Pro Plan**
- $79/month
- Unlimited videos
- 4K resolution
- AI captions

Let me know if you want to get started 😊
"""