from encrypt import encrypt_message, decrypt_message
from io_utils import read_from_file, read_key_from_console, decide_action, write_to_file, DECRYPT_ACTION, ENCRYPT_ACTION

if __name__ == '__main__':
    action = decide_action()
    if action == ENCRYPT_ACTION:
        s = read_from_file(action)
        if s is not None:
            encrypted, key = encrypt_message(s)
            write_to_file('encrypted.txt', encrypted)
            print(f'Результат: "{encrypted}"')
            print(f'Ключ: "{key}"')
    elif action == DECRYPT_ACTION:
        s = read_from_file(action)
        if s is not None:
            k = read_key_from_console()
            if k is not None:
                decrypted = decrypt_message(s, k)
                print(f'Результат: "{decrypted}"')
