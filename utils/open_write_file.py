from pathlib import Path
import csv


def open_file(path: str | Path, encoding: str = 'utf-8'):
    # Перетворюємо шлях у об'єкт Path
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Файл не знайденно {p}")

    # Відкриваємо файл з указаним кодуванням
    with p.open(encoding=encoding) as file:
        for line in file:
            yield line

def write_file(path: str | Path, contact: list, encoding: str = 'utf-8'):
    p = Path(path)
    p = p.name
    
    if not p.exists():
        woth p.open('w', encoding=encoding) as file:
            csv.writer(file).writerow(contact)
            
    
    with p.open(encoding=encoding) as file:
        pass