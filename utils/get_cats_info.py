from .open_write_file import open_file
from pathlib import Path


def get_cats_info(path: str | Path, encoding: str = 'utf-8') -> list[dict[str, str | int]]:
    cats = []
    for line in open_file(path, encoding):
        line = line.strip()
        if not line:
            continue

        try:
            id, name, age = line.split(',')
            cats.append({'id': id, 'name': name, 'age': int(age)})
        except ValueError as e:
            print(f"Вік кота {name} вказаний некоректно")
            continue

    return cats
