import urllib.parse
import logging
from api import WikiApi

class Runner:
    def __init__(self):
        self.wiki_api = WikiApi()

    def run(self):
        user_input = self.get_user_input()
        encoded_user_input = self.encode_user_input(user_input)

    def get_user_input(self) -> str:
        """

        :return:
        """
        user_input = input("Введите запрос, который хотите найти:\n")
        if not user_input.rstrip():
            print("Вы ввели пустой запрос, введите снова: \n")
            return self.get_user_input()
        return user_input

    def encode_user_input(self, user_input: str) -> str:
        try:
            encoded = urllib.parse.quote(user_input)
        except Exception as x:
            logging.warning(f"Error while encoding user string : {x}")
            return ""
        return encoded


r = Runner()
r.get_user_input()
