# Python Assessment (Lead Engineer)
We greatly value the time that you put into these assignments.
The technical part of the round-two interview will build upon your submission.

This evaluation is intended to allow you to demonstrate practical Python coding skills, including how you structure your solution.
We value clean code that is easy to understand and extend. We also value appropriate test coverage where applicable.

# Overview
We would like a general object model for running tasks (units of work) in any of the three runtime environments:
1.	Local engineer’s laptop,
2.	In an AWS Batch job container in AWS, and
3.	In an AWS Lambda function.

Each task expects a set of configuration parameters, such as database connection details, that allows it to run regardless of to which runtime environment it is deployed.

For locally running tasks, its parameters are fetched from a JSON file. When running in AWS Batch, we get the parameters from a TinyDB file. Finally, when running as a Lambda the parameters are passed in via the JSON Lambda event.

If needed, bootstrapping of the task configuration is done via environment variables.

# Setup
Create a virtual environment with the required Python libraries by running the following commands:

`python3 -m venv AMA`

`. AMA/bin/activate`

`pip install -r requirements.txt`

