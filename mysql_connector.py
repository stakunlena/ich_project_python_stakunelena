"""
Модуль отвечающий за подключение к MySQL и содержащий функции поиска
"""
import pymysql

def connect_to_db():
    '''
    Устанавливает соединение с базой данных sakila с использованием PyMySQL.
    Возвращает объект соединения или None в случае ошибки.
    '''
    config = {
        'host': 'ich-db.edu.itcareerhub.de',
        'user': 'ich1',
        'password': 'password',
        'database': 'sakila',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    try:
        connection = pymysql.connect(**config)
        #print("Подключение к базе данных успешно.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None
        
def search_by_keyword(keyword):
    connection = connect_to_db()
    if connection is None:
        return []

    try:
        with connection.cursor() as cursor:
            sql = '''
                SELECT film_id, title, description, release_year
                FROM film
                WHERE title LIKE CONCAT('%%', %s, '%%')
                ORDER BY title;
            '''
            cursor.execute(sql, (keyword,))
            results = cursor.fetchall()
            return results  # возвращаем список результатов
    except pymysql.MySQLError as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []
    finally:
        connection.close()


"""def search_by_keyword(keyword): # Ищет фильмы по части названия и позволяет просматривать результаты по 10 строк.
   
    connection = connect_to_db()
    if connection is None:
        return

    try:
        with connection.cursor() as cursor:
            sql = '''
                SELECT film_id, title, description, release_year
                FROM film
                WHERE title LIKE CONCAT('%%', %s, '%%')
                ORDER BY title;
            '''
            cursor.execute(sql, (keyword,))
            results = cursor.fetchall()

            if not results:
                print("Фильмы не найдены.")
                return

            index = 0
            page_size = 10

            while index < len(results):
                page = results[index:index + page_size]
                for film in page:
                    print(f"{film['film_id']} | {film['title']} ({film['release_year']})")
                    print(f"Описание: {film['description']}\n")

                index += page_size

                if index >= len(results):
                    print("Это были все результаты.")
                    break

                cont = input("Показать следующие 10? (y/n): ").strip().lower()
                if cont != 'y':
                    print("Просмотр завершён.")
                    break

    except pymysql.MySQLError as e:
        print(f"Ошибка при выполнении запроса: {e}")
    finally:
        connection.close()"""