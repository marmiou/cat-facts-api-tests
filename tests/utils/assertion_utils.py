def assert_facts_mandatory_attribute_existence(actual_fact):
    assert "_id" in actual_fact, "Attribute '_id' is missing"
    assert "__v" in actual_fact, "Attribute '__v' is missing"
    assert "user" in actual_fact, "Attribute 'user' is missing"
    assert "updatedAt" in actual_fact, "Attribute 'updatedAt' is missing"
    assert "deleted" in actual_fact, "Attribute 'deleted' is missing"
    assert "source" in actual_fact, "Attribute 'source' is missing"
    assert "status" in actual_fact, "Attribute 'status' is missing"
    assert "text" in actual_fact, "Attribute 'text' is missing"
    assert "type" in actual_fact, "Attribute 'type' is missing"
    assert "createdAt" in actual_fact, "Attribute 'createdAt' is missing"


def assert_facts_mandatory_attribute_type(actual_fact):
    assert isinstance(
        actual_fact["_id"], str
    ), "Attribute '_id' has incorrect type"
    assert isinstance(
        actual_fact["__v"], (int, type(None))
    ), "Attribute '__v' has incorrect type"
    assert isinstance(
        actual_fact["user"], str
    ), "Attribute 'user' has incorrect type"
    assert isinstance(
        actual_fact["updatedAt"], str
    ), "Attribute 'updatedAt' has incorrect type"
    assert isinstance(
        actual_fact["deleted"], bool
    ), "Attribute 'deleted' has incorrect type"
    assert isinstance(
        actual_fact["source"], str
    ), "Attribute 'source' has incorrect type"
    assert isinstance(
        actual_fact["status"], dict
    ), "Attribute 'status' has incorrect type"
    assert isinstance(
        actual_fact["text"], str
    ), "Attribute 'text' has incorrect type"
    assert isinstance(
        actual_fact["type"], str
    ), "Attribute 'type' has incorrect type"
    assert isinstance(
        actual_fact["createdAt"], str
    ), "Attribute 'createdAt' has incorrect type"


def assert_facts_equal_values(actual_fact_data, expected_fact):
    assert (
        expected_fact._id == actual_fact_data["_id"]
    ), "Attribute '_id' values do not match"
    assert (
        expected_fact.user == actual_fact_data["user"]["_id"]
    ), "Attribute 'user' values do not match"
    assert (
        expected_fact.text == actual_fact_data["text"]
    ), "Attribute 'text' values do not match"
    assert (
        expected_fact.updatedAt == actual_fact_data["updatedAt"]
    ), "Attribute 'updatedAt' values do not match"
    assert (
        expected_fact.createdAt == actual_fact_data["createdAt"]
    ), "Attribute 'createdAt' values do not match"
    assert (
        expected_fact.deleted == actual_fact_data["deleted"]
    ), "Attribute 'deleted' values do not match"
    assert (
        expected_fact.type == actual_fact_data["type"]
    ), "Attribute 'type' values do not match"
    assert (
        expected_fact.status == actual_fact_data["status"]
    ), "Attribute 'status' values do not match"
