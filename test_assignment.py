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
    return {
      'Records': [
        {
          'EventSource': 'aws:sns',
          'EventVersion': '1.0',
          'EventSubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:Foo:a7d72f53-e07f-44bd-aeae-db4787ab5c69',
          'Sns': {
            'Type': 'Notification',
            'MessageId': '807e8cdb-71aa-5bd5-a96c-d5835a102fb4',
            'TopicArn': 'arn:aws:sns:us-east-1:123456789012:Bar',
            'Subject': None,
            'Message': '{"first_name": "Miles", "last_name": "Morales"}',
            'Timestamp': '2021-07-01T20:45:46.090Z',
            'SignatureVersion': '1',
            'Signature': 'ZUwXyamt6MCEpZ3t5CwTU4FAEf1J9XXWLryq7PeLWQLz0tvIA5LvGdeB422XAo5qMUFXI7rhVJCZ+QWEB+OecVQ7w/9CCz/5Bf+VJhWWeW1Ip4UglHoG/kLHQeIxFdKX+GciNLsC0/gFc4uUdps2nl2U0fW2IkI4aKekyfXiFqm5MLpuropI0ss3pek6Qoyqb7zhLbMgVjdQgKJPhMaiAN4+sj9Y7trNOQX6z/WaE05c4JwgQc29zU8pKGXznrN90kHbDnwtspvHOACZf7FKH/kD6k6vjLJgF3b/BMTNAcU1NxTQte2lk1n2DMKnjFXyo6OxWj6ibETgtdq4zpWKkA==',
            'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-12345678901234567890.pem',
            'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:Foo:a7d72f53-e07f-44bd-aeae-db4787ab5c69',
            'MessageAttributes': {}
          }
        }
      ]
    }
