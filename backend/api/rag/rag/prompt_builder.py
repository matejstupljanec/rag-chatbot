from pathlib import Path

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

PROMPTS_DIR = Path(__file__).parent.joinpath("prompts")


class PromptBuilder:
    def __init__(self):
        self.prompt_template = ChatPromptTemplate(
            [
                ("system", self.system_prompt()),
                ("human", self.human_prompt()),
            ]
        )

    def build_prompt(self, question: str, docs: list[Document]):
        return self.prompt_template.invoke(
            {"context": self.format_docs(docs), "question": question}
        )

    def format_docs(self, docs: list[Document]):
        return "\n\n".join(doc.page_content for doc in docs)

    def system_prompt(self):
        return self.read_file(PROMPTS_DIR.joinpath("system_prompt.txt"))

    def human_prompt(self):
        return self.read_file(PROMPTS_DIR.joinpath("human_prompt.txt"))

    def read_file(self, path: str):
        with open(path, encoding="utf8") as file:
            return file.read()
