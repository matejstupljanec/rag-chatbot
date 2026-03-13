from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class Splitter:
    def __init__(self, chunk_size=500, chunk_overlap=100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

    def split_text(self, text: str):
        return self.splitter.split_text(text)

    def split_documents(self, document: list[Document]):
        return self.splitter.split_documents(document)
