from pathlib import Path
from pprint import pprint


def open_file(path: str | Path, encoding: str = 'utf-8'):
    # Перетворюємо шлях у об'єкт Path
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Файл не знайденно {p}")

    # Відкриваємо файл з указаним кодуванням
    with p.open(encoding=encoding) as file:
        for line in file:
            yield line


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


BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / 'files/cat.txt'


def main():
    try:
        cats_info = get_cats_info(FILE_NAME)
        pprint(cats_info)
    except Exception as e:
        print(f"Некоректні дані: {e}")


if __name__ == "__main__":
    main()