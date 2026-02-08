from pathlib import Path
from utils import get_cats_info
from pprint import pprint

BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / 'cat.txt'
try:
    cats_info = get_cats_info(FILE_NAME)
    pprint(cats_info)
except Exception as e:
    print(f"Некоректні дані: {e}")
