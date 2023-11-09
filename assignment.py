# Your imports
from task import Task


class Widget(Task):
    """
    Widget task that subclasses Task. Ideally, I would use composition over inheritance. However, for simplicity's sake,
    I am using inheritance here.

    Alternatives:

    1. Task is a delegate called by the encompassing Widget class (and similar classes) that receives parameters from
    enveloping functions and executes them.

    2. Task is a parent class that simply defines a run() function with no body. Any subclass of Task (e.g., Widget)
    must implement a run() function; there could be a TaskRunner class with an execute() facade method that calls the
    run() function of whatever Task instance it contains.
    """
    def run(self, parameters):
        return super().run(parameters)
