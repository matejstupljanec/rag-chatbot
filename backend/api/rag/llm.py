from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class LLM:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    def ask(self, question):
        return self.model.invoke(question)

    def template(self, question, docs):
        return f"This is the users question: '{question}'. \
                From the RAG pipline I got this most simmilar documents: '{docs}' \
                Answer on users question only based on this documents. \
                If you dont know the answer, say that you dont know. \
                Don't mention the given documents."
