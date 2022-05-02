
def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/home' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/home')
    assert response.status_code == 200
    assert b"HERD 1.0" in response.data
    assert b"A well-annotated database of putative and validated human enhancers." in response.data
    
def test_home_page_post(test_client):
    """
    GIVEN a Flask application
    WHEN the '/home' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/home')
    assert response.status_code == 405
    assert b"HERD 1.0" not in response.data
    assert b"A well-annotated database of putative and validated human enhancers." not in response.data

def test_help_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/help' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/help')
    assert response.status_code == 200
    assert b"HERD App Documentation" in response.data
    assert b"What is the HERD Database?" in response.data

def test_help_page_post(test_client):
    """
    GIVEN a Flask application
    WHEN the '/help' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/help')
    assert response.status_code == 405
    assert b"HERD App Documentation" not in response.data
    assert b"What is the HERD Database?" not in response.data

def test_about_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/help' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/about')
    assert response.status_code == 200
    assert b"About" in response.data

def test_about_page_post(test_client):
    """
    GIVEN a Flask application
    WHEN the '/help' page is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/about')
    assert response.status_code == 405
    assert b"About" not in response.data