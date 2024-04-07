import logging

import pytest
import requests

from tests.models.fact import Fact
from tests.utils.assertion_utils import assert_fact_equal

RANDOM_ENDPOINT = "/facts/random"
FACT_ENDPOINT = "/facts/"


class TestCatfactsAPI:

    @pytest.mark.api
    def test_get_facts_should_follow_schema(self, base_url):
        get_facts_response = requests.get(base_url + FACT_ENDPOINT)
        assert get_facts_response.status_code == 200
        facts_json = get_facts_response.json()
        logging.info(f"Facts json: {facts_json}")

        facts_list = [Fact(**fact_data) for fact_data in facts_json]

        logging.info("Content of facts_list:")
        for actual_fact in facts_list:
            expected_schema = Fact.get_default_schema()
            logging.info(f"Facts json: {expected_schema}")
            actual_schema = actual_fact.get_instance_schema()
            logging.info(f"Facts json: {actual_schema}")
            assert Fact._compare_schema(expected_schema, actual_schema)

    @pytest.mark.api
    def test_random_fact_should_be_equal_with_fact_by_id(self, base_url):
        random_response = requests.get(
            base_url + RANDOM_ENDPOINT, params={"animal_type": "cat", "amount": 2}
        )
        assert random_response.status_code == 200
        random_fact_data_list = random_response.json()
        logging.info(f"Random facts Response: {random_response.text}")

        random_fact_data = random_fact_data_list[0]
        logging.info(f"Random fact Data: {random_fact_data}")
        expected_fact = Fact(**random_fact_data)

        fact_by_id_response = requests.get(base_url + FACT_ENDPOINT + expected_fact._id)
        assert fact_by_id_response.status_code == 200
        actual_fact_by_id_data = fact_by_id_response.json()
        logging.info(f"fact by object_a_id has Response: {fact_by_id_response.text}")

        assert_fact_equal(actual_fact_by_id_data, expected_fact)
