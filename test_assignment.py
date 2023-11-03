''' Unit tests for the assignment module. '''
import os

import pytest
from   tinydb import TinyDB, Query

from   assignment import Widget


def test_widget(widget_parameters):
    task = Widget()

    output = task.run(widget_parameters)

    assert len(output) == 1

    text = output[0].decode()

    assert text == "Peter Parker"


def test_widget_runs_locally(local_environment):
    text = None

    # Run the task as if running locally and retrieve the task output

    assert text == "Penny Parker"


def test_widget_runs_in_batch(batch_environment):
    text = None

    # Run the task as if running in AWS Batch and retrieve the task output

    assert text == "Peter Porker"


def test_widget_runs_in_lambda(lambda_event):
    text = None

    # Run the task as if running in a Lambda function and retrieve the task output

    assert text == "Miles Morales"


@pytest.fixture
def widget_parameters():
    return {
        "first_name": "Peter",
        "last_name": "Parker"
    }


@pytest.fixture
def local_environment():
    current_environment = os.environ.copy()

    os.environ["PARAMETER_FILE"] = 'parameters.json'

    yield os.environ

    os.environ.clear()
    os.environ.update(current_environment)


@pytest.fixture
def batch_environment():
    current_environment = os.environ.copy()

    os.environ["PARAMETER_DATABASE"] = 'configuration_db.json'

    yield os.environ

    os.environ.clear()
    os.environ.update(current_environment)


@pytest.fixture
def lambda_event():
    return {"first_name": "Miles", "last_name": "Morales"}
