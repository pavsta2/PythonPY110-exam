import random
import re
import json

from faker import Faker

from conf import MODEL


def title():
    filename = "books.txt"
    pattern = re.compile(r'\"(.+?)\"')
    books_list = []

    with open(filename, 'r', encoding="utf-8") as file:
        # books_list = file.readlines()
        # return random.choice(books_list)
        for word in file.readlines():
            books_list.append((re.findall(pattern, word))[0])
    return random.choice(books_list)


def year():
    year_value = random.randint(1940, 2022)
    return year_value


def pages():
    pages_value = random.randint(50, 200)
    return pages_value


def isbn13():
    fake = Faker()
    return fake.isbn13()


def rating():
    return round(random.triangular(0, 5), 2)


def price():
    return round(random.triangular(100, 5000), 2)


def authors():
    fake = Faker()
    fake_name_list = []
    for _ in range(0, random.randint(1, 3)):
        fake_name_list.append(fake.name())
    return fake_name_list


def books_generator(pk):
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
    return books_dict


def book_list(pk):
    filename = "books_json.json"
    books = []
    for _ in range(0, 100):
        books.append(books_generator(pk))
        pk += 1
    with open(filename, "w") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)
    return books


if __name__ == '__main__':
    print(book_list(1))
