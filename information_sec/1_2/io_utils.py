import os
from typing import Optional, Any

ENCRYPT_ACTION = "enc"
DECRYPT_ACTION = "dec"

"""Функция для вывода ошибок"""
def print_red(message: str) -> None:
    print(f"\033[91m{message}\033[0m")


"""Функция чтения имени файла с открытым текстом из консоли"""
def read_filename() -> Optional[str]:
    try:
        filename = input("Введите названия файла с текстом для шифрования: ")
        if not filename.strip():
            print_red("Ошибка: имя файла не должно быть пустым.")
            return None

        if not os.path.isfile(filename):
            print_red(f"Ошибка: файл '{filename}' не найден.")
            return None
        return filename
    except Exception as e:
        print_red(f'Ошибка чтения из файла: {str(e)}')
        return None


"""Функция выбора действия"""
def decide_action() -> Any | None:
    print('Выберите действие: \n'
          '1. Зашифровать файл\n'
          '2. Расшифровать файл')
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
