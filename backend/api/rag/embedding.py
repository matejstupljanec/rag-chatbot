from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


class Embedding:
    def __init__(self):
        self.model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    def create(self, query):
        return self.model.embed_query(query)
