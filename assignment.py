# Your imports
from task import Task


class Widget(Task):
    """
    Widget task that subclasses Task. Ideally, I would use composition over inheritance (i.e., have Task be a delegate
    used by the encompassing Widget class). However, for simplicity's sake, I am using inheritance here.
    """
    def run(self, parameters):
        return super().run(parameters)
