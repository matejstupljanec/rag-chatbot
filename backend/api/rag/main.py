from dotenv import load_dotenv
from embedding import Embedding
from llm import LLM
from scraper import Scraper
from vector_database import VectorDB
from splitter import Splitter

load_dotenv()


def main():
    scraped_text = scrape_page("https://www.fer.unizg.hr/studiji/prijediplomski_studij")
    print(scraped_text)
    print("------------------")
    print(text_splitter(scraped_text))



def create_embedding():
    embeding = Embedding()
    print(embeding.create("hello world")[:5])


def rag(question):
    db_results = VectorDB().search(question)
    for doc in db_results:
        print(doc)
    print("------------------")

    call_LLM(question, db_results)


def call_LLM(question, docs):
    model = LLM()
    template_question = model.template(question, docs)
    print(model.ask(template_question).content)


def ask_LLM(question):
    model = LLM()
    print(model.ask(question).content)


def scrape_page(url):
    scraped_text = Scraper(url).extract_text()
    return scraped_text


def text_splitter(text):
    splitted_text = Splitter().split_text(text)
    return splitted_text


if __name__ == "__main__":
    main()
