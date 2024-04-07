def assert_fact_equal(response_data, expected_fact):
    assert expected_fact._id == response_data['_id']
    assert expected_fact.user == response_data['user']['_id']
    assert expected_fact.text == response_data['text']
    assert expected_fact.updatedAt == response_data['updatedAt']
    assert expected_fact.createdAt == response_data['createdAt']
    assert expected_fact.deleted == response_data['deleted']
    assert expected_fact.type == response_data['type']
    assert expected_fact.status == response_data['status']

