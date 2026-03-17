from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class Splitter:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=[
                "\n\n",
                "\n",
                ". ",
                ", ",
                " ",
                "",
            ],
            keep_separator=False
        )

    def split_text(self, text: str):
        return self.splitter.split_text(text)

    def split_documents(self, document: list[Document]):
        chunks = self.splitter.split_documents(document)
        total_chunks = len(chunks)

        for i, chunk in enumerate(chunks):
            chunk.metadata["chunk_index"] = i
            chunk.metadata["total_chunks"] = total_chunks

        return chunks
