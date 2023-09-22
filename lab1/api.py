import urllib.parse

import requests
import logging


# Класс взаимодействия с Api Википедии
class WikiApi:
    URL = 'https://ru.wikipedia.org/w/api.php'
    RESULT_PAGE_URL = 'https://ru.wikipedia.org/w/index.php'

    def get_wiki(self, user_input: str) -> dict:
        """
        Отправляет запрос к вики-апи с пользовательским запросом user_input
        :param user_input:
        :return: dict
        """
        params = {"action": "query",
                  "list": "search",
                  "format": "json",
                  "srsearch": user_input}

        try:
            # Делаем Get запрос по URL
            request = requests.get(self.URL, params=params)
            # Проверка status_code, и возврат ошибки, если она есть
            request.raise_for_status()

            # получаем ответ в виде JSON
            json_data = request.json()
            # Парсим JSON, и записываем его search в ответ
            self.response_data = {i + 1: {'page_id': elem['pageid'], 'title': urllib.parse.unquote(elem['title'])} for
                                  i, elem
                                  in
                                  enumerate(json_data['query']['search'])}

        except Exception as x:
            # Обрабатываем ошибку
            logging.warning(f"Ошибка запроса к wiki: {x}")
            self.response_data = {}

        return self.response_data

    def get_result_url(self, index: int) -> str:
        """

        :return: string
        """

        # получаем по индексу значение из словаря, и достаем оттуда page_id
        id = self.response_data.get(index, {}).get('page_id')
        if not id:
            print("No such page")
        # собираем url для данного значения, которое достали по индексу
        url = requests.request(method='get', url=self.RESULT_PAGE_URL, params={'curid': id}).url
        return url

    def print_results(self) :
        """

        :return: bool
        """

        if not self.response_data:
            print("По вашему запросу ничего не найдено. Выход \n")
            return False
        print("Выберите нужный вариант")
        i = 0
        for i in self.response_data:
            title = self.response_data[i]['title']
            print(f"{i}) {title}")
        print(f"{i + 1}) Выйти")
        self.response_data[i + 1] = {'title': "Выйти"}

        return True
