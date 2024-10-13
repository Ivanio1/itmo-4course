import os
from typing import Optional, Any

ENCRYPT_ACTION = "enc"
DECRYPT_ACTION = "dec"

"""Функция для вывода ошибок"""
def print_red(message: str) -> None:
    print(f"\033[91m{message}\033[0m")


"""Функция для вывода ключа"""
def print_green(message: str) -> None:
    print(f"\033[92m{message}\033[0m")


"""Функция записи в файл"""
def write_to_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print_green(f"Данные успешно записаны в файл: {filename}")
    except IOError as e:
        print_red(f"Ошибка записи в файл {filename}: {e}")
    except Exception as e:
        print_red(f"Произошла ошибка: {e}")


"""Функция чтения из файла"""
def read_from_file(action) -> Optional[str]:
    try:
        if action == 'enc':
            filename = input("Введите названия файла с текстом для шифрования: ")
        else:
            filename = input("Введите названия файла с текстом для дешифрования: ")

        if not filename.strip():
            print_red("Ошибка: имя файла не должно быть пустым.")
            return None

        if not os.path.isfile(filename):
            print_red(f"Ошибка: файл '{filename}' не найден.")
            return None
        with open(filename, "r") as f:
            buf = f.read().split('\n')[0]
            if not buf.strip():
                print_red("Ошибка: файл пуст.")
                return None
            return buf
    except Exception as e:
        print_red(f'Ошибка чтения из файла: {str(e)}')
        return None


"""Функция чтения ключа из консоли"""
def read_key_from_console() -> Optional[str]:
    k = input("Введите ключ шифрования: ")
    if not k.strip():
        print_red("Ошибка: ключ не должен быть пустым.")
        return None
    return k

"""Функция выбора действия"""
def decide_action() -> Any | None:
    print('Выберите действие: \n'
          '1. Зашифровать текст с помощью ключа\n'
          '2. Расшифровать текст с помощью ключа')
    try:
        option = int(input("Введите номер: "))
        if option not in [1, 2]:
            print_red(f'Ошибка: опция {option} недоступна!')
            return None
        if option == 1:
            return ENCRYPT_ACTION
        elif option == 2:
            return DECRYPT_ACTION
        else:
            return None
    except Exception:
        print_red(f'Ошибка: неверный ввод. Необходимо ввести целое число.')
        return None

