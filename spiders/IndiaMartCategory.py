from bs4 import BeautifulSoup
from bs4.element import Tag
from scrapy import Request, Spider
from scrapy.http import Response
from typing import Dict, Generator, List
from urllib.parse import urljoin

class IndiaMartCategory(Spider):
    """
    Scrapy Spider to extract subcategories from the goods directory of IndiaMART. 

    Reads category URLs from a text file and scrapes `category`, `sub_category`, `sub_category_url` under each category.

    Attributes:
        custom_settings (dict): Custom settings including headers and throttle configuration.
        name (str): Unique spider name used by Scrapy to identify this spider.
        path (str): Path to the file containing target category URLs.
    """

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Referer": "https://www.google.com"
        },
        "DOWNLOAD_DELAY": 2.0,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 1.0,
        "AUTOTHROTTLE_MAX_DELAY": 5.0
    }
    name = "IndiaMartCategory"

    def __init__(self, path: str = "targets.txt"):
        """
        Initialize the spider with a path to the input file.

        Parameters:
            path (str): Path to the file containing category URLs.
        """

        self.path = path

    def start_requests(self):
        """
        Reads target category URLs from text file and sends Scrapy requests.

        Yields:
            Request: Scrapy Request objects with category URLs and associated metadata.
        """

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                urls = [url.strip() for url in file.readlines() if url.strip()]
                for url in urls:
                    yield Request(
                        url=url,
                        callback=self.parse,
                        meta={"category_url": url},
                        dont_filter=True
                    )
        except FileNotFoundError:
            self.logger.error(f"{self.path} file not found.")

    def parse(self, response: Response) -> Generator[Dict[str, str], None, None]:
        """
        Parses subcategory data from the IndiaMART directory.

        Parameters:
            response (Response): The response object.

        Yields:
            dict: A dictionary containing:
                - category (str): Main category name from the <h1> tag.
                - sub_category (str): Subcategory name.
                - sub_category_url (str): Fully resolved URL for the subcategory.
        """

        soup = BeautifulSoup(response.text, "lxml")

        category_tag = soup.find("h1")
        if not category_tag:
            self.logger.warning(f"No <h1> main category found for {response.url}")
            return

        category = category_tag.get_text(strip=True)
        self.logger.info(f"Extracting sub categories from {category} category")

        sub_categories_tag: Tag = soup.find("div", attrs={"class": "mid"})
        if not sub_categories_tag:
            self.logger.warning(f"No <ul> found following <h1> for {response.url}")
            return
        ul_tags: List = sub_categories_tag.find_all("ul")
        self.logger.info(f"Found {len(ul_tags)} <ul> tags in the sub-categories section.")

        for ul_tag in ul_tags:
            li_tags: List = ul_tag.find_all("li")
            self.logger.info(f"Found {len(li_tags)} <li> tags in the <ul> tag of the sub-categories section.")
            for li_tag in li_tags:
                sub_category_link: str = li_tag.find("a")
                if sub_category_link:
                    sub_category: str = sub_category_link.get_text(strip=True)
                    sub_category_url: str = sub_category_link.get("href")
                yield {
                    "category": category,
                    "sub_category": sub_category,
                    "sub_category_url": urljoin(response.meta["category_url"], sub_category_url)
                }