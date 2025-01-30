import pytest
import boto3
import json
from . import TEST_ENDPOINT, TEST_REGION, TEST_QUEUE_URL

@pytest.fixture(scope="session", autouse=True)
def ensure_test_queue():
    """Ensure test queue exists before running tests"""
    sqs = boto3.client('sqs',
                      endpoint_url=TEST_ENDPOINT,
                      region_name=TEST_REGION,
                      aws_access_key_id='test',
                      aws_secret_access_key='test')

    try:
        sqs.create_queue(QueueName='default')
        print("\nTest queue created/verified")
    except Exception as e:
        print(f"\nQueue setup note: {e}")

    yield