# qa_python
В файле tests.py содержаться тесты для приложения BooksCollector. 
Это приложение позволяет установить жанр книг и добавить их в избранное.

Класс BooksCollector реализован в файле main.py и содержит:
Словарь books_genre, куда можно добавить пару Название книги: Жанр книги.
Список favorites, который содержит избранные книги.
Список genre, который содержит доступные жанры.
Список genre_age_rating, который содержит жанры с возрастным рейтингом.
Набор методов для работы со словарем books_genre и списком favorites:
add_new_book — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
set_book_genre — устанавливает жанр книги, если книга есть в books_genreи её жанр входит в списокgenre.
get_book_genre— выводит жанр книги по её имени.
get_books_with_specific_genre— выводит список книг с определённым жанром.
get_books_genre— выводит текущий словарь books_genre.
get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
delete_book_from_favorites — удаляет книгу из избранного, если она там есть.
get_list_of_favorites_books — получает список избранных книг.

Список тестов:
1. Проверка, что книга не может быть добавлена в словарь повторно.
2. Проверка, что книга c названием допустимой длины (1-40 символов) добавляется в словарь.
3. Проверка, что книга c названием некорректной длины (0, 41, 42 символа) не может быть добавлена в словарь.
4. Проверка, что книге устанавился жанр, если книга есть в словаре books_genre и её жанр входит в список genre.
5. Проверка, что книге с жанром, которого нет в списке genre, не установился жанр.
6. Проверка вывода списка книг с определенным жанром.
7. Проверка вывода словаря books_genre из словаря фикстуры dictionary.
8. Проверка, что в списке книг, которые подходят детям, 2 книги из словаря фикстуры dictionary.
9. Проверка, что книга добавилась в избранное.
10. Проверка, что книги, которой нет в словаре books_genre, не добавляется в избранное.
11. Проверка удаления книги из избранного.
12. Проверка получения списка избранных книг.

Фикстура для тестов №6 и №7 создана в файле conftest.py