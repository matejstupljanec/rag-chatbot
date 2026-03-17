from django.apps import apps


class RAGService:
    @staticmethod
    def ask(question: str):
        api_config = apps.get_app_config("api")
        answer = api_config.rag_pipeline.run(question)
        return answer
