import os
from RC6 import rc6_ofb_encrypt, rc6_ofb_decrypt
from io_utils import decide_action, ENCRYPT_ACTION, DECRYPT_ACTION, read_filename, print_red

key = b'SuperSecretKey123'
encrypted_file = 'encrypted.bin'
decrypted_file = 'decrypted.txt'


def encrypt_file(symmetric_key, input_file, output_file):
    global iv

    try:
        iv = generate_iv()

        with open(input_file, 'rb') as f:
            plaintext = f.read()

        if not plaintext:
            raise ValueError("Файл пустой.")

        ciphertext = rc6_ofb_encrypt(symmetric_key, iv, plaintext)

        with open(output_file, 'wb') as f:
            f.write(iv + ciphertext)

        print(f"Файл зашифрован и сохранен в: {output_file}")

    except (ValueError) as e:
        print_red(f"Ошибка: {e}")
    except Exception as e:
        print_red(f"Произошла непредвиденная ошибка: {e}")


def decrypt_file(symmetric_key, input_file, output_file):
    global iv

    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Файл {input_file} не найден!")

        if os.path.getsize(input_file) == 0:
            raise ValueError(f"Файл {input_file} пустой.")

        with open(input_file, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()

        decrypted_plaintext = rc6_ofb_decrypt(symmetric_key, iv, ciphertext)

        with open(output_file, 'wb') as f:
            f.write(decrypted_plaintext)

        print(f"Файл расшифрован и сохранен в: {output_file}")

    except (FileNotFoundError, ValueError) as e:
        print_red(f"Ошибка: {e}")
    except Exception as e:
        print_red(f"Произошла непредвиденная ошибка: {e}")


def generate_iv():
    return os.urandom(16)


def main():
    action = decide_action()
    if action == ENCRYPT_ACTION:
        input_file = read_filename()
        if input_file is not None:
            encrypt_file(key, input_file, encrypted_file)

    elif action == DECRYPT_ACTION:
        decrypt_file(key, encrypted_file, decrypted_file)


if __name__ == "__main__":
    main()

iv = None
