from langchain_google_genai import ChatGoogleGenerativeAI


class LLMClient:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    def invoke(self, question: str):
        answer = self.model.invoke(question).content
        return answer
