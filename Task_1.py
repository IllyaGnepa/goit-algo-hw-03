import os
import shutil
import argparse

# Функція для копіювання файлів у нову директорію та сортування за розширенням
def copy_files(src_dir, dest_dir):
    try:
        for root, dirs, files in os.walk(src_dir):  # Проходимо по всіх директоріях та файлах
            for file in files:
                # Отримуємо розширення файлу, якщо його немає, присвоюємо 'no_extension'
                file_ext = os.path.splitext(file)[1][1:] or 'no_extension'
                new_dir = os.path.join(dest_dir, file_ext)  # Створюємо нову піддиректорію за розширенням
                os.makedirs(new_dir, exist_ok=True)  # Створюємо піддиректорію, якщо вона не існує
                shutil.move(os.path.join(root, file), os.path.join(new_dir, file))  # Переміщуємо файл у нову директорію
    except (OSError, shutil.Error) as e:
        print(f"Виникла помилка: {e}")

# Основна функція
def main():
    # Запитуємо у користувача, чи хоче він використовувати поточну директорію
    use_current_dir = input("Використати поточну директорію? (y/n): ").strip().lower()

    if use_current_dir == 'y':
        src_dir = os.getcwd()
    else:
        src_dir = input("Введіть шлях до вихідної директорії: ").strip()

    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Копіювання та сортування файлів за розширенням.')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Директорія призначення (за замовчуванням: dist)')
    
    args = parser.parse_args()

    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує.")
        return
    
    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)  # Створюємо директорію призначення, якщо вона не існує
    
    copy_files(src_dir, args.dest_dir)  # Викликаємо функцію копіювання файлів

# Запуск програми
if __name__ == '__main__':
    main()