from mysql_connector import search_by_keyword

def run_menu():
    while True:
        print("===============================")
        print("     Приложение 'Фильмы'")
        print("===============================")
        print("1. Поиск по ключевому слову")
        print("2. Поиск по жанру и годам")
        print("3. Популярные запросы")
        print("4. Последние запросы")
        print("-------------------------------")
        print("0. Выход")
        print("===============================")

        choice = input("Выберите пункт: ")

        if choice == "1":
            handle_keyword_search()
        elif choice == "2":
            handle_genre_search()
        elif choice == "3":
            show_popular_queries()
        elif choice == "4":
            show_recent_queries()
        elif choice == "0":
            print("Выход из приложения.")
            break
        else:
            print("Неверный ввод. Повторите.\n")


def handle_keyword_search():
    print("\n== ПОИСК ПО КЛЮЧЕВОМУ СЛОВУ ==")
    keyword = input("Введите текстовый запрос или название фильма или 0 для возврата в главное меню: ")
    if keyword == "0":
        return

    results = search_by_keyword(keyword)
    if not results:
        print("Ничего не найдено.\n")
        return

    index = 0
    page_size = 10
    total = len(results)

    while index < total:
        page = results[index:index + page_size]
        for film in page:
            print(f"{film['film_id']}. {film['title']} ({film['release_year']})")
            print(f"Описание: {film['description']}\n")

        index += page_size

        if index < total:
            more = input("Показать следующие 10 результатов? (y/n): ").lower()
            if more != 'y':
                break
        else:
            print("Это были все результаты.")


def handle_genre_search():
    print("\n== ПОИСК ПО ЖАНРУ И ГОДАМ ==")
    genre = input("Введите жанр (или 0 для возврата): ")
    if genre == "0":
        return
    year_range = input("Введите диапазон годов (например, 2005-2010): ")
    print(f"Выполняется поиск по жанру '{genre}' и годам '{year_range}'...\n")
    # Здесь будет вызов реальной функции поиска


def show_popular_queries():
    print("\n== ПОПУЛЯРНЫЕ ЗАПРОСЫ ==")
    # Здесь будет вызов функции статистики
    print("(заглушка) список популярных запросов\n")


def show_recent_queries():
    print("\n== ПОСЛЕДНИЕ ЗАПРОСЫ ==")
    # Здесь будет вызов функции статистики
    print("(заглушка) список последних запросов\n")
