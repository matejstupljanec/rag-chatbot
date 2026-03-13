from dotenv import load_dotenv
from embedding_model import EmbeddingModel
from langchain_core.documents import Document
from llm_client import LLMClient
from rag_pipeline import RAGPipeline
from scraper import Scraper
from splitter import Splitter
from vector_store import VectorStore

load_dotenv()


def main():
    embedding = EmbeddingModel()
    llm = LLMClient()
    db = VectorStore(embedding)
    pipeline = RAGPipeline(db, llm)

    answer = pipeline.run("Što je prijediplomski studij FER?")
    print(answer)


def scrape_page(url):
    scraped_text = Scraper(url).extract_text()
    return scraped_text


def text_splitter(text):
    splitted_text = Splitter().split_text(text)
    return splitted_text


def scrape_and_split():
    url = "https://www.fer.unizg.hr/studiji/prijediplomski_studij"
    text = scrape_page(url)
    document = Document(page_content=text, metadata={"source": url})
    print(document)

    print("---------")

    docs = Splitter().split_documents([document])
    for doc in docs:
        print(doc)
        print("////////////")


if __name__ == "__main__":
    main()
