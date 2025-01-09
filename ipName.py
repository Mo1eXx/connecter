import os

def open_text(path):
    with open(path, 'r') as file:
        text = file.read()
        return text.split()


PATH = ('cd c:\\Program Files (x86)\\Radmin viewer 3 && Radmin.exe')

def connect_pc(pc):
    os.system(f'{PATH} /connect:{pc}:4899 /noinput')
