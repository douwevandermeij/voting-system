

def test_get_votes_0(client):
    response = client.get("/votes")
    assert response.status_code == 200
    assert response.json() == 0


def test_get_votes_1(client):
    client.post("/vote")
    response = client.get("/votes")
    assert response.status_code == 200
    assert response.json() == 1


def test_get_votes_10(client):
    for i in range(1, 10):
        client.post("/vote")
    response = client.get("/votes")
    assert response.status_code == 200
    assert response.json() == 10
