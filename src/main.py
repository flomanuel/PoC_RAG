from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import asyncio

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.2", request_timeout=360.0)

# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()


async def search_documents(query: str) -> str:
    response = await query_engine.aquery(query)
    return str(response)


agent = AgentWorkflow.from_tools_or_functions(
    [search_documents],
    llm=Settings.llm,
    system_prompt="You are a helpful assistant that can answer questions to a business information systems student.",
)


async def main():
    response = await agent.run(
        "",
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
