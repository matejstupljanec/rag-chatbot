from dotenv import load_dotenv
from api.rag.core.embedding_model import EmbeddingModel
from api.rag.core.llm_client import LLMClient
from api.rag.core.vector_store import VectorStore
from api.rag.rag.rag_pipeline import RAGPipeline

load_dotenv()


def main():
    embedding = EmbeddingModel()
    llm = LLMClient()
    db = VectorStore(embedding)
    rag_pipeline = RAGPipeline(db, llm)
    # ingestion_pipeline = IngestionPipeline(db)

    answer = rag_pipeline.run(
        "Koliko ukupno godina traje diplomski", print_retrieved_docs=True
    )
    print(answer)

    # ingestion_pipeline = IngestionPipeline(db)
    # ingestion_pipeline.run()


if __name__ == "__main__":
    main()
