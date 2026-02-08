from pathlib import Path
from utils import total_salary

BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / 'info.txt'

try:
    total, average  = total_salary(FILE_NAME)
    print(f"\nЗагальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as e:
    print(f"Некоректні дані: {e}")
    print(f"Загальна сума заробітної плати: 0, Середня заробітна плата: 0")
