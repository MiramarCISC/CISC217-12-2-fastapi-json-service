def test_list_characters(client):
    r=client.get("/characters")
    assert r.status_code==200
    assert [c["name"] for c in r.json()]==["Aria","Borin"]

def test_list_characters_filters_by_minimum_power(client):
    r=client.get("/characters?minimum_power=80")
    assert [c["name"] for c in r.json()]==["Aria"]

def test_list_characters_respects_limit(client):
    r=client.get("/characters?limit=1")
    assert len(r.json())==1

def test_get_character(client):
    r=client.get("/characters/1")
    assert r.status_code==200
    assert r.json()["name"]=="Aria"

def test_get_character_missing_returns_404(client):
    r=client.get("/characters/999")
    assert r.status_code==404
    assert r.json()["detail"]=="Character not found"
