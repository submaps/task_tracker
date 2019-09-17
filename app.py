import threading

from flask import Flask
from collections import deque
from multiprocessing import Pool
from Task import Task

app = Flask(__name__)
task_queue = deque()
task_dict = {}


@app.route('/')
def main():
    return 'Welcome to <b>task_tracker</b>!'


@app.route('/send_task')
def send_task():
    task = Task()
    task_dict[task.task_id] = task
    task_queue.append(task.task_id)
    return str(task.task_id)


@app.route('/task_list')
def task_list():
    return '<br>'.join(str(task) for task_id, task in task_dict.items())


def execute_task(task):
    task.start()


@app.route('/execute')
def execute_all_task():
    num_workers = 2
    p = Pool(num_workers)
    while task_queue:
        task_id_list = [task_queue.popleft() for _ in range(num_workers)]
        task_list = [task_dict[task_id] for task_id in task_id_list]
        print(p.map(execute_task, task_list))
        return 'task executed {}'.format(task_id_list)
    return 'empty queue'


if __name__ == '__main__':
    app.run()
