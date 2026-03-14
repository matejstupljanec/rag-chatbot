from langchain_google_genai import GoogleGenerativeAIEmbeddings


class EmbeddingModel:
    def __init__(self):
        self.model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    def embed(self, text: str):
        return self.model.embed_query(text)
