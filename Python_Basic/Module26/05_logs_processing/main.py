import os.path

input_file_path = os.path.join('data', 'work_logs.txt')
output_file_path = os.path.join('data', 'output.txt')


def error_log_generator(path):
    with open(input_file_path, 'r') as file:
        for line in file:
            if line.startswith('ERROR: '):
                yield line


with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")





