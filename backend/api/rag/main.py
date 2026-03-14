from core.embedding_model import EmbeddingModel
from core.llm_client import LLMClient
from core.vector_store import VectorStore
from data_ingestion.ingestion_pipeline import IngestionPipeline
from dotenv import load_dotenv
from rag.rag_pipeline import RAGPipeline

load_dotenv()


def main():
    embedding = EmbeddingModel()
    llm = LLMClient()
    db = VectorStore(embedding)
    rag_pipeline = RAGPipeline(db, llm)
    # ingestion_pipeline = IngestionPipeline(db)

    answer = rag_pipeline.run(
        "Koliko ukupno godina traje faks", print_retrieved_docs=True
    )
    print(answer)

    # ingestion_pipeline = IngestionPipeline(db)
    # ingestion_pipeline.run()


if __name__ == "__main__":
    main()
