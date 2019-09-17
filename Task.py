from datetime import datetime
import uuid

from TaskStatus import TaskStatus


def run_default_task():
    try:
        import test
        return True
    except:
        pass


class Task:
    def __init__(self):
        self.task_id = uuid.uuid1()
        self.create_time = datetime.now()
        self.start_time = None
        self.time_to_execute = None
        self.status = None

    def start(self):
        self.start_time = datetime.now()
        self.status = TaskStatus.RUN
        run_default_task()
        self.time_to_execute = datetime.now() - self.start_time
        self.status = TaskStatus.COMPLETED
        self.save_to_db()

    def save_to_db(self):
        pass

    def __repr__(self):
        return ' '.join(
            map(str,
                [self.task_id,
                self.start_time.strftime("%Y-%m-%d, %H:%M:%S") if self.start_time else None,
                self.create_time.strftime("%Y-%m-%d, %H:%M:%S"),
                self.time_to_execute if self.start_time else None,
                self.status])
        )
