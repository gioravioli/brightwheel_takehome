from utils import clean_fields
import requests
from bs4 import BeautifulSoup


class ChildcarePage():
    def __init__(self, db, url):
        self.db = db
        self.url = url

    def add_all(self, num_pages=None):
        if num_pages is None:
            num_pages = self._get_num_pages()
        for i in range(1, num_pages + 1):
            self._parse_page(i)
        return self

    def _parse_page(self, page_num):
        url = f"{self.url}&pagenum={page_num}"
        soup = BeautifulSoup(requests.get(url).content, features="lxml")
        num_cols = len([x.text for x in soup.find('table').find_all('th')])
        values = [x.text for x in soup.find('table').find_all('td')]
        for i in range(0, len(values), num_cols):
            fields = clean_fields({
                'name': values[i],
                'type': values[i + 1],
                'address': values[i + 2],
                'city': values[i + 3],
                'state': values[i + 4],
                'zip': values[i + 5],
                'phone': values[i + 6],
                'email': values[i + 7]
            })
            self.db.add_provider(fields=fields)

    def _get_num_pages(self):
        soup = BeautifulSoup(requests.get(self.url).content, features="lxml")
        tbl = soup.find_all('table')[-1]
        return int(tbl.find_all('a')[-1]['href'].split('=')[-1])
