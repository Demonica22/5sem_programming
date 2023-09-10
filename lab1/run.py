import urllib.parse
import logging
from api import WikiApi
import webbrowser

class Runner:
    def __init__(self):
        self.wiki_api = WikiApi()

    def run(self):
        user_input = self.get_user_input()
        self.wiki_api.get_wiki(user_input)
        print("Выберите нужный вариант")
        self.wiki_api.print_results()

        user_input = input("Введите число: \n")
        if 0 < int(user_input) <= len(self.wiki_api.response_data.keys()):
            webbrowser.open(self.wiki_api.get_result_url(int(user_input)))

    def get_user_input(self) -> str:
        """

        :return:
        """
        user_input = input("Введите запрос, который хотите найти:\n")
        if not user_input.rstrip():
            print("Вы ввели пустой запрос, введите снова: \n")
            return self.get_user_input()
        return user_input




r = Runner()
r.run()
