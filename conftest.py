import pytest

from main import BooksCollector


@pytest.fixture
def dictionary():
    dictionary = BooksCollector()
    dictionary.add_new_book('Три поросенка')
    dictionary.add_new_book('Лисица и журавль')
    dictionary.add_new_book('Маша и медведь')
    dictionary.add_new_book('Шерлок Холмс')
    dictionary.set_book_genre('Три поросенка', 'Ужасы')
    dictionary.set_book_genre('Лисица и журавль', 'Мультфильмы')
    dictionary.set_book_genre('Маша и медведь', 'Мультфильмы')
    dictionary.set_book_genre('Шерлок Холмс', 'Детективы')
    return dictionary
