import logging
import urllib.parse

import requests
import logging
import json
from pprint import pprint


class WikiApi:
    URL = 'https://ru.wikipedia.org/w/api.php'
    RESULT_PAGE_URL = 'https://ru.wikipedia.org/w/index.php'

    def __init__(self):
        pass

    def get_wiki(self, user_input: str) -> dict:
        params = {"action": "query",
                  "list": "search",
                  "format": "json",
                  "srsearch": user_input}

        try:
            request = requests.get(self.URL, params=params)
            request.raise_for_status()

            json_data = request.json()
            self.response_data = {i + 1: {'page_id': elem['pageid'], 'title': urllib.parse.unquote(elem['title'])} for
                                  i, elem
                                  in
                                  enumerate(json_data['query']['search'])}

            return self.response_data
        except Exception as x:
            logging.warning(f"Ошибка запроса к wiki: {x}")
            return {}

    def get_result_url(self, index: int) -> str:
        id = self.response_data.get(index, {}).get('page_id')
        if not id:
            print("No such page")
        url = requests.request(method='get', url=self.RESULT_PAGE_URL, params={'curid': id}).url
        return url

    def print_results(self):
        print("Выберите нужный вариант")
        i = 0
        for i in self.response_data:
            title = self.response_data[i]['title']
            print(f"{i}) {title}")
        print(f"{i + 1}) Выйти")
        self.response_data[i + 1] = {'title': "Выйти"}
