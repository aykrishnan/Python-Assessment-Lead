# Python Assessment (Lead Engineer)
We greatly value the time that you put into these assignments.
The technical part of the round-two interview will build upon your submission.

This evaluation is intended to allow you to demonstrate practical Python coding skills, including how you structure your solution.
We value clean code that is easy to understand and extend. We also value appropriate test coverage where applicable.

When you have completed the challenge, please send an email to your recruiter with the link to your fork of the repository containing the completed assessment.
They will ensure that it makes it back to us.

# Overview
We would like a general object model for running tasks (units of work) in any of the three runtime environments:
1.	Local engineer’s laptop,
2.	In an AWS Batch job container in AWS, and
3.	In an AWS Lambda function.

Each task expects a set of configuration parameters, such as database connection details, that allows it to run regardless of to which runtime environment it is deployed.

For locally running tasks, its parameters are fetched from a JSON file. When running in AWS Batch, we get the parameters from a TinyDB file. Finally, when running as a Lambda the parameters are passed in via the JSON Lambda event. If needed, bootstrapping of the task configuration is done via environment variables.

Instructions for each task can be found in this README. Please use best practices when solving these tasks.

This assessment should take around a couple of hours or so to complete, so please timebox your efforts. You should complete at least task #1 and two of the other tasks to demonstrate the generality of the object model. That said, if the object model is well thought out it should be straight forward by design to accomodate additional runtime use cases.

# Setup
Create a virtual environment with the required Python libraries by running the following commands:

`python3 -m venv AMA`

`. AMA/bin/activate`

`pip install -r requirements.txt`

# Testing
Run the unit tests as follows:

pytest -vv

# Task 1
Implement the base object model classes in _task.py_. Update the _assignment.py_ module as needed to tie it in with the object model.

# Task 2
Implement any specific code for running the `Widget` task locally. This includes completing the associated unit test case in _test_assignment.py_.

# Task 3
Implement any specific code for running the `Widget` task as if from AWS Batch.  This includes completing the associated unit test case in _test_assignment.py_.

# Task 4
Implement any specific code for running the `Widget` task as if from AWS Lambda.  This includes completing the associated unit test case in _test_assignment.py_.
