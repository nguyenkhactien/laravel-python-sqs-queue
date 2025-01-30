"""
Test configuration for Laravel Python Queue package.
"""
import os
import sys
from pathlib import Path

# Add the src directory to Python path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Test constants
TEST_QUEUE_URL = "http://localhost:4566/000000000000/default"
TEST_REGION = "ap-northeast-1"
TEST_ENDPOINT = "http://localhost:4566"

# Common test data
TEST_JOB_CLASS = "App\\Jobs\\TestJob"
TEST_JOB_DATA = {
    "message": "Test message",
    "user_id": 123
}