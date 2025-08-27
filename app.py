import asyncio
import glob
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings


async def run_memory_chat():
    # Load API keys
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Path to your MCP config
    config_file = "browser_mcp.json"

    # Initialize MCP Client
    client = MCPClient.from_config_file(config_file)

    # Initialize LLM (Groq)
    llm = ChatGroq(model="llama-3.1-8b-instant")

 
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    for filepath in glob.glob("docs/*.txt"):   # iterate all text files in docs/
        loader = TextLoader(filepath)
        file_docs = loader.load()
        for d in file_docs:
            d.metadata["source"] = os.path.basename(filepath)
        split_docs = splitter.split_documents(file_docs)
        docs.extend(split_docs)

    if not docs:
        raise RuntimeError("No documents found in docs/ folder. Please add some .txt files.")

    # use Chroma as vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embeddings)


    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True
    )

    print("🤖 AI Agent + RAG (multi-file) is ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # Retrieve docs for context
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        relevant_docs = retriever.get_relevant_documents(user_input)

        if relevant_docs:
            context = "\n\n".join(
                [f"[From {d.metadata.get('source', 'unknown')}]\n{d.page_content}" for d in relevant_docs]
            )
            final_prompt = f"""You are an AI assistant with access to tools. 
Use the following context if useful:

Context:
{context}

Now respond to the user query (use tools if needed):

{user_input}
"""
        else:
            # No RAG context → just forward the query (so MCP tools can trigger)
            final_prompt = user_input

        
        response = await agent.run(final_prompt)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    asyncio.run(run_memory_chat())
