import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    #напиши свои тесты ниже
    #чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_if_name_is_in_book_genre(self):  #1 проверка, что книга которая уже есть в словаре, не добавилась повторно в словарь
        collector = BooksCollector()
        collector.add_new_book('Книга для чтения перед сном')
        collector.add_new_book('Книга для чтения перед сном')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_if_name_lenth_more_tnan_40(self):  #2 проверка, что книга с названием больше 40 символов не добавляется в словарь
        collector = BooksCollector()
        collector.add_new_book('Книга с длинным названием, которое больше сорока символов')
        assert collector.get_book_genre('Книга с длинным названием, которое больше сорока символов') is None

    def test_set_book_genre_set_genre_success(self):  #3 проверка, что книге устанавился жанр, если книга есть в словаре books_genre и её жанр входит в список genre
        collector = BooksCollector()
        collector.add_new_book('Пигмалион')
        collector.set_book_genre('Пигмалион', 'Комедии')
        assert collector.get_book_genre('Пигмалион') == 'Комедии'
    #
    def test_set_book_genre_if_genre_not_in_genre(self):  #4 проверка, что книге с жанром, которого нет в списке genre, не установился жанр
        collector = BooksCollector()
        collector.add_new_book('Робинзон Крузо')
        collector.set_book_genre('Робинзон Крузо', 'Приключения')
        assert collector.get_book_genre('Робинзон Крузо') == ''

    def test_get_books_with_specific_genre_get_list(self):  #5 проверка вывода списка книг с определенным жанром
        collector = BooksCollector()
        collector.add_new_book('Тайная комната')
        collector.set_book_genre('Тайная комната', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Тайная комната']

    def test_get_books_genre_get_dictionary(self, dictionary):  #6 проверка вывода словаря books_genre
        assert len(dictionary.get_books_genre()) == 4

    def test_get_books_for_children_2_books_in_list(self, dictionary):  #7 проверка, что в списке книг, которые подходят детям, 2 книги
        assert len(dictionary.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_book_success(self):    # 8 проверка, что книга добавилась в избранное
        collector = BooksCollector()
        collector.add_new_book('Орден Феникса')
        collector.add_book_in_favorites('Орден Феникса')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_if_not_in_books_genre_book_not_added(self):    # 9 проверка, что книги, которой нет в словаре books_genre, не добавилась в избранное
        collector = BooksCollector()
        collector.add_book_in_favorites('Орден Феникса')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_is_deleted(self):  # 10 проверка удаления книги из избранного
        collector = BooksCollector()
        collector.add_new_book('Орден Феникса')
        collector.add_book_in_favorites('Орден Феникса')
        collector.delete_book_from_favorites('Орден Феникса')
        assert len(collector.get_list_of_favorites_books()) == 0

    favorite_books = ['Дюна', 'Асока', 'Книга Бобы Фетта']  #11  проверка получения списка избранных книг
    @pytest.mark.parametrize('fav_books', favorite_books)
    def test_get_list_of_favorites_books_get_list(self, fav_books):
        collector = BooksCollector()
        collector.add_new_book(fav_books)
        collector.add_book_in_favorites(fav_books)
        assert fav_books in collector.get_list_of_favorites_books()
