import json

# --- ТВОЯ ЗАДАЧА НАПИСАТЬ ФУНКЦИИ ЗДЕСЬ ---
# Тебе нужно создать функции buy_book и sell_book так,
# чтобы код в самом низу этого файла заработал и не выдал ошибок.
# Функций, которые ты напишешь, может быть и больше чем 2. Нам нужно чтобы были написаны и работали buy_book и sell_book
# Предполагаемая струкутра проекта: написать код только в этом файле.
# Данные по сущностям будем хранить в json'ах.


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f)


# ------------------------------------------

# --- ЭТОТ КОД НЕ МЕНЯЙ. ОН ДОЛЖЕН ЗАРАБОТАТЬ ---
if __name__ == "__main__":
    print("Начинаем симуляцию магазина...")

    # 1. Закупаем книги на склад
    buy_book(
        book_name="Python Crash Course",
        count=10,
        buy_price=1000,
        sell_price=1111,
        author_name="author1",
        genre="python",
        language="en",
        year=2001,
    )

    # 2. Продаем пару книг
    sell_book(book_name="Python Crash Course", count=3)
    sell_book(book_name="Python Crash Course", count=2)

    # 3. Пытаемся продать больше, чем есть на складе
    try:
        sell_book(book_name="Python Crash Course", count=100)
        print("ОШИБКА: Твой код позволил продать 100 книг, хотя на складе их всего 5!")
    except ValueError:
        print("ОТЛИЧНО: Твой код правильно заблокировал продажу (выдал ValueError).")

    print("Симуляция завершена. Проверь файлы book.json и transaction.json!")
