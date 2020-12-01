

def test_post_vote(client):
    response = client.post("/vote")
    assert response.status_code == 200
