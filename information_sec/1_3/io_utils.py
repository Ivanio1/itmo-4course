import os
from typing import Optional


def print_red(message: str) -> None:
    """Функция для вывода ошибок"""
    print(f"\033[91m{message}\033[0m")


def print_green(message: str) -> None:
    """Функция для вывода ответов сервиса"""
    print(f"\033[92m{message}\033[0m")


def read_filename(is_input) -> str:
    """Функция чтения имени файла"""
    if is_input:
        filename = input("Введите названия входного файла: ")
    else:
        filename = input("Введите названия выходного файла: ")
    if not filename.strip():
        print_red("Ошибка: имя файла не должно быть пустым.")
        return None
    return filename


def read_from_file(filename) -> Optional[bytes]:
    """Функция чтения из файла"""
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


def write_to_file(filename, content):
    """Функция записи в файл"""
    try:
        with open(filename, 'wb') as file:
            file.write(content)
        print_green(f"Данные успешно записаны в файл: {filename}")
    except IOError as e:
        print_red(f"Ошибка записи в файл {filename}: {e}")
    except Exception as e:
        print_red(f"Произошла ошибка: {e}")
