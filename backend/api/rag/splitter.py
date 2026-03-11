from langchain_text_splitters import RecursiveCharacterTextSplitter


class Splitter:
    def __init__(self):
        pass

    def split_text(self, text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        splitted_text = text_splitter.split_text(text)
        return splitted_text
