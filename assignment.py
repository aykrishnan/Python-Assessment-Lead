# Your imports
import task


class Widget:
    def run(self, parameters):
        return [f'{parameters["first_name"]} {parameters["last_name"]}'.encode()]
