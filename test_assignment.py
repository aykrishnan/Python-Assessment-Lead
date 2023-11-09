import os
import pytest

from assignment import Widget


def test_widget(widget_parameters):
    task = Widget()
    output = task.run(widget_parameters)

    assert len(output) == 1

    text = output[0].decode()

    assert text == "Peter Parker"


def test_widget_runs_locally(local_environment):
    filename = local_environment.get('PARAMETER_FILE')
    task = Widget()
    output = task.run_locally(filename)
    text = output[0].decode()

    assert text == "Penny Parker"


def test_widget_runs_in_batch(batch_environment):
    filename = batch_environment.get('PARAMETER_DATABASE')
    task = Widget()
    output = task.run_in_batch(filename)
    text = output[0].decode()

    assert text == "Peter Porker"


def test_widget_runs_in_lambda(lambda_event):
    task = Widget()
    output = task.run_from_lambda(lambda_event)
    text = output[0].decode()

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
