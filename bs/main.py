import os
import time
from ftplib import FTP
import subprocess

address = "192.168.0.8"
command = ["ping", "-c", "10", address]


def ping():
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output = result.stdout
        errors = result.stderr

        print("Выходные данные команды ping:")
        print(output)

        if errors:
            print("Ошибки:")
            print(errors)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def create_large_file(filename, size_in_gb):
    """Создает файл заданного размера в Гб."""
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_in_gb * 1024 * 1024))


def upload_file_ftp(ftp, filename):
    """Загружает файл на FTP-сервер и замеряет время передачи."""
    ftp.set_pasv(True)
    start_time = time.time()
    with open(filename, 'rb') as f:
        ftp.storbinary(f'STOR {os.path.basename(filename)}', f)
    end_time = time.time()

    elapsed_time = end_time - start_time
    file_size = os.path.getsize(filename)
    speed_mbps = (file_size * 8) / (1024 * 1024 * elapsed_time)  # Биты в Мегабиты/сек

    return elapsed_time, speed_mbps


def main():
    filename = 'large_file_2.bin'
    size_in_mb = 300
    ftp_host = '192.168.0.8'
    ftp_user = 'Asus'
    ftp_pass = 'root'

    # print("Создание большого файла...")
    # create_large_file(filename, size_in_mb)
    # print(f"Файл {filename} успешно создан.")

    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    print("Начало загрузки на FTP...")
    elapsed_time, speed_mbps = upload_file_ftp(ftp, filename)
    ftp.quit()

    print(f"Загрузка завершена.")
    print(f"Время передачи: {elapsed_time:.2f} секунд.")
    print(f"Скорость передачи: {speed_mbps:.2f} Мбит/с.")

    ping()


if __name__ == "__main__":
    main()
