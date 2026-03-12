from llm_client import LLMClient
from vector_store import VectorStore
from prompt_builder import PromptBuilder


class RAGPipeline:
    def __init__(self, db: VectorStore, llm: LLMClient):
        self.db = db
        self.llm = llm
        self.prompt_builder = PromptBuilder()

    def run(self, question: str):
        docs = self.db.similarity_search(question)
        prompt = self.prompt_builder.build_prompt(question, docs)
        return self.llm.invoke(prompt).content
