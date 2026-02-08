from .open_write_file import open_file, write_file

def add_contact():
    pass

def change_contact():
    pass

def show_phone():
    pass

def show_all():
    pass


def parse_input(comands: str, *args):
    COMMANDS = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all
        }
    
    hendler = COMMANDS.get(comands)
        
    if hendler:
        result = hendler(args)