from app.adapter.inmemory_vote_repository import InMemoryVoteRepository
from app.domain.vote import Vote

from fastapi import FastAPI

app = FastAPI()

vote_repository = InMemoryVoteRepository()


@app.post("/vote")
def vote() -> Vote:
    return Vote().save(vote_repository)


@app.get("/votes")
def votes() -> int:
    return vote_repository.total()
