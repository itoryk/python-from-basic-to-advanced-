import os

folder = os.path.abspath(os.path.join('..'))

gen_files_path = [links + '\\' + file for links, dirs, files in list(os.walk(folder)) for file in files ]

for file in gen_files_path:
    print(file)