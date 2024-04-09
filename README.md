# Cat Facts API tests
<h1 align="center">API automation with pytest & requests</h1>

## Links

- [Repo](https://github.com/marmiou/cat-facts-api-tests "API automation with pytest & requests")

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.8 or higher on your machine. You can check by using 
```bash
python3 -V
```
- You have installed Poetry for dependency management. If you haven't, follow the installation instructions below.

## Installation

### Installing Poetry

Poetry is a tool for dependency management and packaging in Python. To install Poetry, run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
For other installation methods, visit the [official Poetry documentation](https://python-poetry.org/docs/).

## Installation

After installing Poetry, clone the project repository and navigate to the project directory:

```bash
git clone git@github.com:marmiou/cat-facts-api-tests.git
cd cat-facts-api-tests
```
Install the project dependencies by running:
```bash
poetry install
```

## Available Commands
To activate the project's virtual environment and run the tests:
```bash
poetry shell
pytest
```

Alternatively, you can run commands within the virtual environment without activating it by using poetry run. 
For example, to run a specific test:
```bash
poetry run pytest tests/api/test_cat_facts_api.py
```

Or, to run all e2e tests:
```bash
poetry run pytest
```

Reports of the run can be found under the directory:
```bash
allure/reports
```

To open reports execute:

```bash
allure serve reports/allure-results
```

## Test Table

| Test Case Description                                                     | Test Method                                                      |
|---------------------------------------------------------------------------|------------------------------------------------------------------|
| Check if all mandatory attributes exist in the API response               | `test_get_facts_attributes_should_exist`                        |
| Check if all mandatory attributes have expected types                     | `test_get_facts_attributes_should_have_expected_type`            |
| Check if fact IDs are unique                                              | `test_fact_ids_should_be_unique`                                 |
| Equality of a random fact attributes with those of a fact retrieved by ID | `test_random_fact_should_be_equal_with_fact_by_id`               |


## What validations have been used and why?

### test_get_facts_attributes_should_exist:

This test aims to ensure that when getting facts from the endpoint, each fact object in the response JSON contains all 
the mandatory attributes.

Validation: The test iterates over each fact in the response JSON and checks if it contains all the mandatory attributes 
using the assert_facts_mandatory_attribute_existence function.

Purpose: Ensures that the API response contains the necessary data for each fact object, guaranteeing that no mandatory 
attributes are missing

### test_get_facts_attributes_should_have_expected_type:

This test verifies that the data types of the attributes in each fact object returned by the endpoint are as expected.

Validation: Test iterates over each fact in the response JSON and checks if the data types of all attributes are as 
expected using the assert_facts_mandatory_attribute_type function.

Purpose: Ensures data integrity and consistency by confirming that the attributes have the correct data types. This 
helps prevent unexpected errors due to type mismatches during data processing.


### test_fact_ids_should_be_unique:

This test ensures that the IDs assigned to each fact in the response JSON are unique.

Validation: It constructs a list of fact IDs from the JSON response and checks if the length of this list matches the 
length of a set of unique IDs. If they are not equal, it means there are duplicate IDs.

Purpose: Guarantees the uniqueness of fact IDs, which is crucial for data integrity and prevents potential issues such 
as overwriting or confusion between different facts with the same ID.

### test_random_fact_should_be_equal_with_fact_by_id:

This test verifies the consistency between fetching a random fact and fetching the same fact by its ID.

Validation: It first fetches a random fact, then retrieves the same fact by its ID and compares the retrieved facts' data.

Purpose: Ensures that the random fact retrieved matches the same fact obtained by its ID, validating the consistency 
and accuracy of data retrieval from the API.


Also, all the above tests verify the status code of the response JSON by equality.
In general, other methods of validation can also be validating headers, schema, handling errors, authorisation etc, but
we didn't use them here.

## Built With

- Pytest
- Requests
- Allure reporter
- Poetry
- iSort

## Author

**Markella Efthymiou**
- [GitHub Profile](https://github.com/marmiou/ "Markella Efthymiou")
- [Email](mailto:efthymioumarkella@gmail.com?subject=Hi "Hi!")

## 🤝 Support

Contributions and issues are welcome!

Give a ⭐️ if you like this project!
