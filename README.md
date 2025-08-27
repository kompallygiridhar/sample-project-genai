# 🤖 AI Agent + RAG (Multi-file) with MCP & Groq

This project demonstrates how to build an **AI Agent with RAG (Retrieval-Augmented Generation)** using:

- [LangChain](https://www.langchain.com/)  
- [Groq LLM](https://groq.com/) (`llama-3.1-8b-instant`)  
- [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol) for tool usage  
- [ChromaDB](https://www.trychroma.com/) as the vector store  
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)  

The agent can:
- Use **context from local `.txt` files** in the `docs/` folder.  
- Use **MCP tools** (e.g., browser, APIs) for external actions.  
- Maintain **memory across steps** for better conversations.  

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
