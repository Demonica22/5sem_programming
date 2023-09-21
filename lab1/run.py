from api import WikiApi
import webbrowser


class Runner:
    def __init__(self):
        self.wiki_api = WikiApi()

    def run(self):
        user_input = self.get_user_search_input()
        self.wiki_api.get_wiki(user_input)

        results = self.wiki_api.print_results()

        if results:
            self.get_user_choice_input()

    # Считываем пользовательский поиск
    def get_user_search_input(self) -> str:
        """

        :return: string
        """
        user_input = input("Введите запрос, который хотите найти:\n")
        if not user_input.rstrip():
            print("Вы ввели пустой запрос, введите снова: \n")
            return self.get_user_search_input()
        return user_input

    # Считываем количество строк поиска, и открываем страницу
    def get_user_choice_input(self) -> None:
        user_input = input("Введите число: \n")
        while not user_input.isdigit():
            print("Ошибка ввода, вы ввели не число\n")
            user_input = input("Введите число: \n")
        finished = False
        while not finished:
            if 0 < int(user_input) < len(self.wiki_api.response_data.keys()):
                print("Открываем страницу в браузере")
                webbrowser.open(self.wiki_api.get_result_url(int(user_input)))
                finished = True
            elif int(user_input) == len(self.wiki_api.response_data.keys()):
                print('Выход')
                finished = True
            else:
                user_input = input("Ошибка ввода, введите число снова\n")

r = Runner()
r.run()
