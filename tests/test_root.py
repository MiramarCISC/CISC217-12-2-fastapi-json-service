def test_root(client):
    r=client.get("/")
    assert r.status_code==200
    assert r.json()=={"message":"CISC 217 Character API"}
