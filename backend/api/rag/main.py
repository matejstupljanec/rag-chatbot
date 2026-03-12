from dotenv import load_dotenv
from embedding_model import EmbeddingModel
from llm_client import LLMClient
from scraper import Scraper
from vector_store import VectorStore
from splitter import Splitter
from rag_pipeline import RAGPipeline

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


if __name__ == "__main__":
    main()
