import enum


class TaskStatus(enum.Enum):
    IN_QUEUE = 'In Queue'
    RUN = 'Run'
    COMPLETED = 'Completed'
