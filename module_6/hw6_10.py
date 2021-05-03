from pathlib import Path
import shutil


def create_archive(path, file_name, employee_residence):

    path_file = f'{path}/{file_name}'
    with open(path_file, 'wb') as file:
        for name, country in employee_residence.items():
            file.write(f'{name} {country}\n'.encode('utf-8'))
    name_archive = shutil.make_archive('backup', 'zip', path)

    return name_archive


# Функция, которая сохраняет архив в папку по пути path, а не в текущую папку, как в первой ф-ции.
'''def create_archive(path, file_name, employee_residence):

    path_file = Path(path) / file_name
    with open(path_file, 'wb') as file:
        for name, country in employee_residence.items():
            file.write(f'{name} {country}\n'.encode('utf-8'))
    path_archive = Path(path) / 'backup'
    name_archive = shutil.make_archive(path_archive, 'zip', path)

    return name_archive'''
