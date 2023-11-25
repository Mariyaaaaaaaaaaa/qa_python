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

    def test_add_new_book_if_name_is_in_book_genre(self):
        """Книга не может быть добавлена в словарь повторно."""
        collector = BooksCollector()
        collector.add_new_book('Книга для чтения перед сном')
        collector.add_new_book('Книга для чтения перед сном')
        assert len(collector.get_books_genre()) == 1



    books_with_correct_lenth = ['1', '12', 'Тестовая книга c названием 39 символов!', 'Тестовая книга c названием 40 символов!!']
    @pytest.mark.parametrize('correct_lenth', books_with_correct_lenth)
    def test_add_new_book_if_name_lenth_is_correct(self, correct_lenth):
        """Книга с названием допустимой длины (1-40 символов) добавляется в словарь"""
        collector = BooksCollector()
        collector.add_new_book(correct_lenth)
        assert correct_lenth in collector.get_books_genre()


    books_not_correct_lenth = ['', 'Тест-книга, у которой название 41 символ!', 'Тест-книга, у которой название 42 символа!']
    @pytest.mark.parametrize('incorrect_lenth',books_not_correct_lenth)
    def test_add_new_book_if_name_lenth_is_not_correct(self, incorrect_lenth):
        """Книга с названием некорректной длины (0, 41, 42 символа) не может быть добавлена в словарь."""
        collector = BooksCollector()
        collector.add_new_book(incorrect_lenth)
        assert collector.get_book_genre(incorrect_lenth) is None



    def test_set_book_genre_set_genre_success(self):
        """Книге устанавился жанр, если книга есть в словаре books_genre и её жанр входит в список genre."""
        collector = BooksCollector()
        collector.add_new_book('Пигмалион')
        collector.set_book_genre('Пигмалион', 'Комедии')
        assert collector.get_book_genre('Пигмалион') == 'Комедии'
    #
    def test_set_book_genre_if_genre_not_in_genre(self):
        """Книге с жанром, которого нет в списке genre, не установился жанр."""
        collector = BooksCollector()
        collector.add_new_book('Робинзон Крузо')
        collector.set_book_genre('Робинзон Крузо', 'Приключения')
        assert collector.get_book_genre('Робинзон Крузо') == ''

    def test_get_books_with_specific_genre_get_list(self):
        """Вывод списка книг с определенным жанром."""
        collector = BooksCollector()
        collector.add_new_book('Тайная комната')
        collector.set_book_genre('Тайная комната', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Тайная комната']

    def test_get_books_genre_get_dictionary(self, dictionary):
        """Вывод словаря books_genre из словаря фикстуры dictionary."""
        assert dictionary.get_books_genre() == {'Три поросенка': 'Ужасы', 'Лисица и журавль': 'Мультфильмы', 'Маша и медведь': 'Мультфильмы', 'Шерлок Холмс': 'Детективы'}

    def test_get_books_for_children_2_books_in_list(self, dictionary):
        """В списке книг, которые подходят детям, 2 книги из словаря фикстуры dictionary."""
        assert dictionary.get_books_for_children() == ['Лисица и журавль', 'Маша и медведь']

    def test_add_book_in_favorites_add_book_success(self):
        """Книга добавилась в избранное."""
        collector = BooksCollector()
        collector.add_new_book('Орден Феникса')
        collector.add_book_in_favorites('Орден Феникса')
        assert 'Орден Феникса' in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_if_not_in_books_genre_book_not_added(self):
        """Книги, которой нет в словаре books_genre, не добавляется в избранное."""
        collector = BooksCollector()
        collector.add_book_in_favorites('Орден Феникса')
        assert len(collector.get_list_of_favorites_books()) == 0, "Данной книги нет в словаре!"

    def test_delete_book_from_favorites_book_is_deleted(self):
        """Удаление книги из избранного."""
        collector = BooksCollector()
        collector.add_new_book('Орден Феникса')
        collector.add_book_in_favorites('Орден Феникса')
        collector.delete_book_from_favorites('Орден Феникса')
        assert len(collector.get_list_of_favorites_books()) == 0


    def test_get_list_of_favorites_books_get_list(self):
        """Получение списка избранных книг."""
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Асока')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Асока')
        assert 'Дюна' in collector.get_list_of_favorites_books() and 'Асока' in collector.get_list_of_favorites_books()

