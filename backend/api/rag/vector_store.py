import os

from embedding_model import EmbeddingModel
from langchain_postgres import PGVector
from langchain_core.documents import Document



class VectorStore:
    def __init__(self, embedding: EmbeddingModel):
        db_user = os.environ["DB_USERNAME"]
        db_pass = os.environ["DB_PASSWORD"]
        db_host = os.environ["DB_HOST"]
        db_port = os.environ["DB_PORT"]
        db_name = os.environ["DB_NAME"]

        connection = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        collection_name = "fer_docs"

        self.db = PGVector(
            embeddings=embedding.model,
            collection_name=collection_name,
            connection=connection,
        )

    def similarity_search(self, question: str):
        return self.db.similarity_search(query=question, k=3)

    def add_documents(self, docs: list[Document]):
        self.db.add_documents(docs)
