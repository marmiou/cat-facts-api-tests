# cat-facts-api-tests/tests/conftest.py

import logging
import os

import pytest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    # Define the base URL of the API
    return os.getenv("API_BASE_URL", "https://cat-fact.herokuapp.com")


@pytest.fixture(scope="session")
def api_key():
    # Get the API key from environment variables if available
    return os.getenv("API_KEY")


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)


pytest.mark.api = pytest.mark.mark(name='api')
