import os
import time


def read_tasks():
    """
    this function reads all tasks and makes it readable
    :return: task list
    """
    task_list = []
    with os.popen('tasklist /fo csv') as command:
        command.readline()
        for line in command:
            new_line = line.split(',')
            task_list.append(new_line[0][1:-1])
    return task_list


def save_list_of_processes_to_kill():
    """
    This function looks for all processes starting with
    "Riot" and "League"
    :return: processes_list to kill
    """
    processes_list = []
    for task in read_tasks():
        if "Riot" in task:
            processes_list.append(task)
        elif "League" in task:
            processes_list.append(task)
    return processes_list


def kill_processes(process_name: str):
    """
    kills process by given name
    :param process_name:
    :return: None
    """
    os.system('taskkill /im "' + process_name + '" /f /t')


def main():
    """check for time if it is before 2pm/14.00"""
    while time.localtime()[3] <= 14:
        time.sleep(9)
        for process in save_list_of_processes_to_kill():
            kill_processes(process)


if __name__ == '__main__':
    main()
