import random
import re
import json

from faker import Faker

from conf import MODEL


def title() -> list:
    """
    Формирует список книг из файла с помощью регулярок и возвращает из него случайный объект
    :return:случайный объект из списка
    """
    filename = "books.txt"
    pattern = re.compile(r'\"(.+?)\"')
    books_list = []

    with open(filename, 'r', encoding="utf-8") as file:
        for word in file.readlines():
            books_list.append((re.findall(pattern, word))[0])
    return random.choice(books_list)


def year() -> int:
    """
    Возвращает рандомный год
    :return:рандомный год
    """
    year_value = random.randint(1940, 2022)
    return year_value


def pages() -> int:
    """
    Формирует рандом номер страницы
    :return:номер страницы
    """
    pages_value = random.randint(50, 200)
    return pages_value


def isbn13() -> str:
    """
    Формирует фэйковый isbn13
    :return:фэйковый isbn13
    """
    fake = Faker()
    return fake.isbn13()


def rating() -> float:
    """
    Формирует число от 0 до 5 с плавающей точкой, округл до 2 знаков
    :return: Формирует число от 0 до 5 с плавающей точкой, округл до 2 знаков
    """
    return round(random.triangular(0, 5), 2)


def price() -> float:
    """
    Формирует число от 100 до 5000 с плавающей точкой, округл до 2 знаков
    :return:
    """
    return round(random.triangular(100, 5000), 2)


def authors() -> list:
    """
    Формирует список от 1 до 3 фейк авторов
    :return: Формирует список от 1 до 3 фейк авторов
    """
    fake = Faker()
    fake_name_list = []  # list comprehension FIXED
    [fake_name_list.append(fake.name()) for _ in range(0, random.randint(1, 3))]
    return fake_name_list


def books_generator(pk=1) -> iter:
    """
    Генератор словарей
    :param pk: с какого номера начинать
    :return:
    """
    while True:
        books_dict = {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": rating(),
                "price": price(),
                "author": authors()
            }
        }
        pk += 1
        yield books_dict


def main(pk) -> list:
    """
    Формирует список словарей книг
    :param pk: с какого номера начинать
    :return:
    """
    b = books_generator(pk)
    filename = "books_json.json"
    books = []  # list comprehension FIXED
    [books.append(next(b)) for _ in range(0, 100)]
    with open(filename, "w") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)
    return books


if __name__ == '__main__':
    print(main(1))
