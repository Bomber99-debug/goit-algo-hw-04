from .open_write_file import open_file
from pathlib import Path

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