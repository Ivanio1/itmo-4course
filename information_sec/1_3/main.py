from encoder import encode
from io_utils import read_from_file, read_filename, write_to_file, print_red


def main():
    try:
        input_file = read_filename(True)
        output_file = read_filename(False)
        if input_file is not None and output_file is not None:
            data = read_from_file(input_file)
            encoded = encode(data)
            write_to_file(output_file, encoded)
    except Exception as e:
        print_red(f'Ошибка чтения из файла: {str(e)}')


if __name__ == "__main__":
    main()
