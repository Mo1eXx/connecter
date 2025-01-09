

def open_text(path):
    with open(path, 'r') as file:
        text = file.read()
        return text.split()


open_text('test.txt')
