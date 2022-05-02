import json

def test_documentation_table_data(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the /api/documentation_table route is requested (GET)
    THEN check response is a valid json object
    """
    response = test_client.get('/api/documentation_table')
    assert response.status_code == 200
    res = json.loads(response.data.decode('utf-8')).get("data")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['System'] == 'Circulatory'
    assert type(res) is list
