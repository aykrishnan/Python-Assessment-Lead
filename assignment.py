# Your imports
import task


# Make changes to the Widget class as needed
class Widget:
    def run(self, parameters):
        return [f'{parameters["first_name"]} {parameters["last_name"]}'.encode()]
