from langchain_core.documents import Document


class PromptBuilder:
    def __init__(self):
        pass

    def build_prompt(self, question: str, retrieved_docs: list[Document]):
        prompt = f"This is the users question: '{question}'. \
            From the RAG pipline I got this most simmilar documents: '{retrieved_docs}' \
            Answer on users question only based on this documents. \
            If you dont know the answer, say that you dont know. \
            Don't mention the given documents."

        return prompt
