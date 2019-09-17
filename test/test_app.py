import unittest
import requests


class TestApp(unittest.TestCase):
    def test_execute(self):
        proxies = {
            "http": None,
            "https": None,
        }
        for i in range(10):
            res = requests.get('http://127.0.0.1:5000/send_task', proxies=proxies)
            print(i, res.text)

        res = requests.get('http://127.0.0.1:5000/task_list', proxies=proxies)
        print('task_list:')
        task_list = res.text.split('<br>')
        for task_row in task_list:
            print(task_row)
