import subprocess

def process_count(username: str) -> int:
    commands = ['ps', '-u', username]
    process = subprocess.run(commands, capture_output=True)
    count_process = process.stdout.decode().splitlines()[1:]
    return len(count_process)

def total_memory_usage(root_pid: int) -> float:
    commands1 = ['ps', '--ppid', str(root_pid), '-o', '%mem=']
    process = subprocess.run(commands1, capture_output=True)
    list_process = process.stdout.decode().splitlines()
    new_list = [float(i) for i in list_process]
    return sum(new_list)


if __name__ == '__main__':
    count = process_count('root')
    print(f'output: {count}')
    memory = total_memory_usage(1)
    print(f'output: {memory}%')
