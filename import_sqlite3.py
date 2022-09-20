import sqlite3

try:
    # add name your base here
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    # use SQL here
    sql_query = """INSERT INTO reviews_categories VALUES (5, 'shiran', 'музыка');"""
    cursor.execute(sql_query)
    sqlite_connection.commit()
    print("Действие прошло успешно")
    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
