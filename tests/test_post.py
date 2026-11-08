def test_create_character(client):
    r=client.post("/characters",json={"name":"Cyra","health":90,"power":95})
    assert r.status_code==201
    body=r.json()
    assert body=={"id":3,"name":"Cyra","health":90,"power":95}

def test_created_character_can_be_retrieved(client):
    c=client.post("/characters",json={"name":"Cyra","health":90,"power":95}).json()
    r=client.get(f"/characters/{c['id']}")
    assert r.status_code==200
    assert r.json()["name"]=="Cyra"
