import logging

import pytest
import requests

from tests.models.fact import Fact
from tests.utils.assertion_utils import (
    assert_facts_equal_values,
    assert_facts_mandatory_attribute_existence,
    assert_facts_mandatory_attribute_type,
)

RANDOM_ENDPOINT = "/facts/random"
FACTS_ENDPOINT = "/facts/"


class TestCatfactsAPI:

    @pytest.mark.api
    def test_get_facts_attributes_should_exist(self, base_url):
        get_facts_response = requests.get(base_url + FACTS_ENDPOINT)
        assert get_facts_response.status_code == 200
        facts_json = get_facts_response.json()
        logging.info(f"Facts json: {facts_json}")

        for actual_fact in facts_json:
            logging.info(f"Actual fact attributes: {actual_fact}")
            assert_facts_mandatory_attribute_existence(actual_fact)

    @pytest.mark.api
    def test_get_facts_attributes_should_have_expected_type(self, base_url):
        get_facts_response = requests.get(base_url + FACTS_ENDPOINT)
        assert get_facts_response.status_code == 200
        facts_json = get_facts_response.json()
        logging.info(f"Facts json: {facts_json}")

        for actual_fact in facts_json:
            logging.info(f"Actual fact: {actual_fact}")
            assert_facts_mandatory_attribute_type(actual_fact)

    @pytest.mark.api
    def test_fact_ids_should_be_unique(self, base_url):
        get_facts_response = requests.get(base_url + FACTS_ENDPOINT)
        assert get_facts_response.status_code == 200
        facts_json = get_facts_response.json()
        logging.info(f"Facts json: {facts_json}")

        facts_list = [Fact(**fact_data) for fact_data in facts_json]

        fact_ids = [fact._id for fact in facts_list]
        assert len(fact_ids) == len(set(fact_ids)), "Fact IDs are not unique"

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

        fact_by_id_response = requests.get(
            base_url + FACTS_ENDPOINT + expected_fact._id
        )
        assert fact_by_id_response.status_code == 200
        actual_fact_by_id_data = fact_by_id_response.json()
        logging.info(f"Fact by ID Response: {fact_by_id_response.text}")

        assert_facts_equal_values(actual_fact_by_id_data, expected_fact)
