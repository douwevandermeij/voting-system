import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.vote_repository import VoteRepository


@dataclass
class Vote:
    vote_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, vote_repository: 'VoteRepository'):
        return vote_repository.add(self)

    def __hash__(self):
        return hash(self.vote_id)
