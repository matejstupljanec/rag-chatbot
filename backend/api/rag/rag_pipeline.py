from langchain_core.documents import Document
from llm_client import LLMClient
from prompt_builder import PromptBuilder
from vector_store import VectorStore


class RAGPipeline:
    def __init__(self, db: VectorStore, llm: LLMClient):
        self.db = db
        self.llm = llm
        self.prompt_builder = PromptBuilder()

    def run(self, question: str, print_retrieved_docs=False) -> str:
        docs = self.db.similarity_search(question)

        if print_retrieved_docs:
            self.print_retrieved_documents(docs)

        prompt = self.prompt_builder.build_prompt(question, docs)

        return self.llm.invoke(prompt)

    def print_retrieved_documents(self, docs: list[Document]):
        for doc in docs:
            print()
            print(doc)
        print()
