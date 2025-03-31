from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import asyncio
import chromadb

PROMPT = "What are the core concepts of the REACH regulation from the EU?"

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3.2", request_timeout=360.0)

# Load documents and create an index
print("Loading documents...")
documents = SimpleDirectoryReader("./data").load_data()
node_parser = SimpleNodeParser.from_defaults(chunk_size=512)  # bei großen Dokumenten 1024
nodes = node_parser.get_nodes_from_documents(documents)
chroma_client = chromadb.Client()
chroma_collection = chroma_client.create_collection("report")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(
    nodes,
    storage_context=storage_context
)

# Option 1: run an agent
#query_engine = index.as_query_engine()
# async def search_documents(query: str) -> str:
#     response = await query_engine.aquery(query)
#     return str(response)
#
# agent = AgentWorkflow.from_tools_or_functions(
#     [search_documents],
#     llm=Settings.llm,
#     system_prompt="Sie sind ein hilfreicher Assistent, der einem Studenten der Wirtschaftsinformatik Fragen beantworten kann.",
# )
#
#
# async def main():
#     response = await agent.run(
#         PROMPT,
#     )
#     print(response)

# Option 2: query the engine directly
embeddings = Settings.embed_model.get_text_embedding(PROMPT)
result = chroma_collection.query(embeddings,n_results=5)
query_engine = index.as_query_engine()
response = query_engine.query(PROMPT)
print("Response with context")
print(response)

# Option 1
#if __name__ == "__main__":
#    asyncio.run(main())
