import logging
import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("API_BASE_URL", "https://cat-fact.herokuapp.com")


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)


pytest.mark.api = pytest.mark.mark(name="api")
