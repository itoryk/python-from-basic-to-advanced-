class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Hello')
