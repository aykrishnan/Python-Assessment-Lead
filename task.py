# Your imports
import json


# Task object model implementation
class Task:

    def run(self, parameters):
        return [f'{parameters["first_name"]} {parameters["last_name"]}'.encode()]

    def run_locally(self, filename):
        with open(filename) as file:
            parameters = json.load(file)
        parameters = parameters['Widget']

        return self.run(parameters)

    def run_in_batch(self, filename):
        with open('configuration_db.json') as file:
            parameters = json.load(file)
        parameters = parameters['_default']['1']['parameters']

        return self.run(parameters)

    def run_from_lambda(self, lambda_output):
        return self.run(lambda_output)
