from datetime import datetime

from fer_urls import FER_URLS
from langchain_core.documents import Document
from scraper import Scraper
from splitter import Splitter
from url_fetcher import URLFetcher
from vector_store import VectorStore


class IngestionPipeline:
    def __init__(self, db: VectorStore):
        self.fetcher = URLFetcher()
        self.scraper = Scraper()
        self.splitter = Splitter()
        self.db = db

    def run(self):
        """IMPORTANT: Do not run this unless FER URLs have changed"""
        docs = []

        for url in FER_URLS:
            html = self.fetcher.fetch(url)
            text = self.scraper.scrape(html)
            doc = self.generate_document(text, url)
            chunks = self.splitter.split_documents([doc])
            docs.extend(chunks)

        self.db.add_documents(docs)

    def generate_document(self, text: str, url: str):
        return Document(
            page_content=text,
            metadata={"source": url, "scraped_at": str(datetime.now())},
        )
