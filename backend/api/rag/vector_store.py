import os

from embedding_model import EmbeddingModel
from langchain_core.documents import Document
from langchain_postgres import PGVector


class VectorStore:
    def __init__(self, embedding: EmbeddingModel):
        db_user = os.environ["DB_USERNAME"]
        db_pass = os.environ["DB_PASSWORD"]
        db_host = os.environ["DB_HOST"]
        db_port = os.environ["DB_PORT"]
        db_name = os.environ["DB_NAME"]

        connection = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        collection_name = "my_docs"

        self.db = PGVector(
            embeddings=embedding.model,
            collection_name=collection_name,
            connection=connection,
        )

    def similarity_search(self, question: str):
        return self.db.similarity_search_with_score(query=question, k=3)

    def add_documents(self):
        docs = self.documents()
        self.db.add_documents(docs, ids=[doc.metadata["id"] for doc in docs])

    def documents(self):
        return [
            Document(
                page_content="there are cats in the pond",
                metadata={"id": 1, "location": "pond", "topic": "animals"},
            ),
            Document(
                page_content="ducks are also found in the pond",
                metadata={"id": 2, "location": "pond", "topic": "animals"},
            ),
            Document(
                page_content="fresh apples are available at the market",
                metadata={"id": 3, "location": "market", "topic": "food"},
            ),
            Document(
                page_content="the market also sells fresh oranges",
                metadata={"id": 4, "location": "market", "topic": "food"},
            ),
            Document(
                page_content="the new art exhibit is fascinating",
                metadata={"id": 5, "location": "museum", "topic": "art"},
            ),
            Document(
                page_content="a sculpture exhibit is also at the museum",
                metadata={"id": 6, "location": "museum", "topic": "art"},
            ),
            Document(
                page_content="a new coffee shop opened on Main Street",
                metadata={"id": 7, "location": "Main Street", "topic": "food"},
            ),
            Document(
                page_content="the book club meets at the library",
                metadata={"id": 8, "location": "library", "topic": "reading"},
            ),
            Document(
                page_content="the library hosts a weekly story time for kids",
                metadata={"id": 9, "location": "library", "topic": "reading"},
            ),
            Document(
                page_content="a cooking class for beginners is offered at the community center",
                metadata={"id": 10, "location": "community center", "topic": "classes"},
            ),
        ]
