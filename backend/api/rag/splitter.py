from langchain_text_splitters import RecursiveCharacterTextSplitter


class Splitter:
    def __init__(self, chunk_size=500, chunk_overlap=100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

    def split_text(self, text):
        return self.splitter.split_text(text)

    def split_document(self, document):
        x = 5
