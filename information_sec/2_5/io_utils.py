import yaml


def read_config(input_file):
    """Метод чтения параметров из конфигурационного файла."""
    with open(input_file, 'r') as file:
        file_contents = file.read()

    return yaml.safe_load(file_contents)


def print_green(message: str) -> None:
    """Метод для вывода ключа"""
    print(f"\033[92m{message}\033[0m")


def print_red(message: str) -> None:
    """Метод для вывода расшифрованного текста"""
    print(f"\033[91m{message}\033[0m")


def print_separator():
    """Метод для вывода разграничителя"""
    print_green("-----------------------------------------------------------------")
