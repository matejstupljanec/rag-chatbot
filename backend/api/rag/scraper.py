from bs4 import BeautifulSoup


class Scraper:
    def scrape(self, html: str):
        soup = BeautifulSoup(html, "html.parser")

        soup = self.clean_soup(soup)
        
        text = self.text_soup(soup)
        return text

    def clean_soup(self, soup: BeautifulSoup):
        irrelevant_tags = [
            "header",
            "footer",
            "nav",
            "script",
            "style",
            "meta",
            "link",
            "title",
        ]

        for tag in soup(irrelevant_tags):
            tag.decompose()

        cookies = soup.find(id="container_admin_bar")
        if cookies:
            cookies.decompose()

        header = soup.find("div", class_="fixed_header")
        if header:
            header.decompose()

        path = soup.find("ol", class_="breadcrumb")
        if path:
            path.decompose()

        old_accessibility = soup.find("div", class_="row breadcrumbs")
        if old_accessibility:
            old_accessibility.decompose()

        return soup

    def text_soup(self, soup: BeautifulSoup):
        text = soup.get_text(separator=" ", strip=True)
        text = text.replace("\xa0", " ")
        return text

    def title(self, soup: BeautifulSoup):
        return soup.title.string
