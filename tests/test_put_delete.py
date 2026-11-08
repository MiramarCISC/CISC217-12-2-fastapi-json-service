def test_replace_character(client):
    r=client.put("/characters/1",json={"name":"Aria Prime","health":110,"power":90})
    assert r.status_code==200
    assert r.json()=={"id":1,"name":"Aria Prime","health":110,"power":90}

def test_replace_missing_character_returns_404(client):
    r=client.put("/characters/999",json={"name":"Nobody","health":1,"power":1})
    assert r.status_code==404

def test_delete_character(client):
    r=client.delete("/characters/1")
    assert r.status_code==200
    assert r.json()=={"deleted":True}
    assert client.get("/characters/1").status_code==404

def test_delete_missing_character_returns_404(client):
    assert client.delete("/characters/999").status_code==404
