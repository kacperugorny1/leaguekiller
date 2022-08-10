import os
import time


def read_tasks():
    task_list = []
    with os.popen('tasklist /fo csv') as command:
        command.readline()
        for line in command:
            new_line = line.split(',')
            task_list.append(new_line[0][1:-1])
    return task_list


def save_list_of_processes_to_kill():
    processes_list = []
    for task in read_tasks():
        if "Riot" in task:
            processes_list.append(task)
        elif "League" in task:
            processes_list.append(task)
    return processes_list


def kill_processes(process_name: str):
    os.system('taskkill /im "' + process_name + '" /f /t')


def main():
    while time.localtime()[3] <= 14:
        time.sleep(10)
        for process in save_list_of_processes_to_kill():
            kill_processes(process)


if __name__ == '__main__':
    main()
