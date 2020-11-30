import uuid

from app.domain.vote import Vote


def test_vote_existing_vote_id():
    vote_id = str(uuid.uuid4())

    assert Vote(vote_id).vote_id == vote_id


def test_vote_defaults():
    assert uuid.UUID(Vote().vote_id)
