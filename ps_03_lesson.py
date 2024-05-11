import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
        result = translater.translate(f"{word_definition}", dest="ru")

        print(result.text)


        user = input("Что это за слово ?")
        if user == word:

            print("Ответ верный")
        else:
            print(f"Ответ не верный,правильный - ")
            result2 = translater.translate(f"{word}", dest="ru")
            print(result2.text)


        play_again = input("Сыграть ещё?  y/n")
        if play_again != "y":
            print("Спасибо за игру")


            break

translater = Translator()

word_game()