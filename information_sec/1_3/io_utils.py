import os
from typing import Optional


def print_red(message: str) -> None:
    """Метод для вывода ошибок"""
    print(f"\033[91m{message}\033[0m")


def read_filename() -> str:
    filename = input("Введите названия входного файла: ")
    if not filename.strip():
        print_red("Ошибка: имя файла не должно быть пустым.")
        return None
    return filename


def read_from_file(filename) -> Optional[bytes]:
    try:
        if not os.path.isfile(filename):
            print_red(f"Ошибка: файл '{filename}' не найден.")
            return None
        with open(filename, "rb") as f:
            buf = f.read()
            if not buf.strip():
                print_red("Ошибка: файл пуст.")
                return None
            return buf
    except Exception as e:
        print_red(f'Ошибка чтения из файла: {str(e)}')
        return None
