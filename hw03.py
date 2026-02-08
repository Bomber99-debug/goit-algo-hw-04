from pathlib import Path
from colorama import Fore, Style, init
from sys import argv, exit

init(autoreset=True)

def dir_files(path: Path):
    try:
        directs = [dir for dir in path.iterdir() if dir.is_dir()]
        files = [file for file in path.iterdir() if file.is_file()]
    except PermissionError as err:
        print(f"{Fore.MAGENTA}Немає доступу: {path}") # {Style.RESET_ALL}
        return 
    
    for direct in directs:
        if direct.is_dir():
            print(f"{Fore.RED}{str(direct)}") # {Style.RESET_ALL}
            dir_files(direct)
        
    for file in files:
        if file.is_file():
            print(f"{Fore.YELLOW}{str(file)}") # {Style.RESET_ALL}


if len(argv) != 2:
    print("Будьласка задайте правильну кількись праметрів")
    exit()

relative_path  = Path(argv[1])
abs_dir = relative_path.resolve()

if abs_dir.is_dir():
    dir_files(abs_dir)