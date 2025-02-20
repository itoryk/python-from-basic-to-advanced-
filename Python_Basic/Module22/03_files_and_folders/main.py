import os

size = 0
path = r'C:\Users'
path, dirs, files = next(os.walk(path))
for file in files:
    file_name = os.path.join(path, file)
    size += os.path.getsize(file_name)

print('Размер каталога (в Кб): ', size / 1024)
print('Количество подкаталогов: ', len(dirs))
print('Количество файлов: ', len(files))

