from pathlib import Path


def open_file(path: str | Path, encoding: str = 'utf-8'):
    # Перетворюємо шлях у об'єкт Path
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Файл не знайденно {p}")

    # Відкриваємо файл з указаним кодуванням
    with p.open(encoding=encoding) as file:
        for line in file:
            yield line


def total_salary(path: str | Path, encoding: str = 'utf-8') -> tuple[int, int]:
    salary_list = []

    for line in open_file(path, encoding):
        line = line.strip()
        if not line:
            continue

        try:
            name, salary = line.split(',')
            salary_list.append(int(salary))

        except ValueError:
            print(f'{name} некоректно вказана заробітна платня: {salary}')
            continue

    if not salary_list:
        print("Файл порожній")
        return 0, 0

    total_salary = sum(salary_list)
    avg_salary = round(total_salary / len(salary_list))

    return total_salary, avg_salary


BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / 'files/info.txt'


def main():
    try:
        total, average = total_salary(FILE_NAME)
        print(f"\nЗагальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(f"Некоректні дані: {e}")
        print(f"Загальна сума заробітної плати: 0, Середня заробітна плата: 0")


if __name__ == "__main__":
    main()
