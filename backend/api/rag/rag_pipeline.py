from llm_client import LLMClient
from vector_store import VectorStore


class RAGPipeline:
    def __init__(self, db: VectorStore, llm: LLMClient):
        self.db = db
        self.llm = llm

    def run(self, question: str):
        docs = self.db.similarity_search(question)
        prompt = self.llm.template(question, docs)
        return self.llm.invoke(prompt).content
