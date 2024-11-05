import os
directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:

        filepath = os.path.join(root, file)


        filetime = os.path.getmtime(filepath)


        filesize = os.path.getsize(filepath)


        parent_dir = os.path.dirname(filepath)


        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} '
              f'байт, Время изменения: {filetime}, Родительская директория: {parent_dir}')
