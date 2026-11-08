def test_path_parameter_must_be_integer(client):
    assert client.get("/characters/not-an-integer").status_code==422

def test_query_parameter_must_be_integer(client):
    assert client.get("/characters?minimum_power=strong").status_code==422

def test_request_body_requires_health(client):
    assert client.post("/characters",json={"name":"Cyra","power":95}).status_code==422

def test_request_body_requires_integer_power(client):
    assert client.post("/characters",json={"name":"Cyra","health":90,"power":"very strong"}).status_code==422
