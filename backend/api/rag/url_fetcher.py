import requests


class URLFetcher:
    def fetch(self, url: str):
        response = requests.get(url)
        return response.content
