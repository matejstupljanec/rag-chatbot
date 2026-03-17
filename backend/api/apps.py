from django.apps import AppConfig
from dotenv import load_dotenv
from api.rag.core.embedding_model import EmbeddingModel
from api.rag.core.llm_client import LLMClient
from api.rag.core.vector_store import VectorStore
from api.rag.rag.rag_pipeline import RAGPipeline

class ApiConfig(AppConfig):
    name = 'api'

    embedding = None
    llm = None
    db = None
    rag_pipeline = None

    def ready(self):

        load_dotenv()

        if ApiConfig.embedding is None:
            ApiConfig.embedding = EmbeddingModel()

        if ApiConfig.llm is None:
            ApiConfig.llm = LLMClient()

        if ApiConfig.db is None:
            ApiConfig.db = VectorStore(ApiConfig.embedding)

        if ApiConfig.rag_pipeline is None:
            ApiConfig.rag_pipeline = RAGPipeline(ApiConfig.db, ApiConfig.llm)
