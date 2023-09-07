from typing import Union

from fastapi import APIRouter

from models.snapshot import Snapshot

import json

router = APIRouter()

with open("resources/mocks/post_snapshot.json", "r") as f:
    snapshot_mock = json.load(f)


@router.get("/{snapshot_id}", response_model=Snapshot)
def get(snapshot_id: int = 1):
    # TODO: Take questions from database, maybe MongoDB
    print(f"SNAPSHOT_ID: {snapshot_id}")
    return snapshot_mock


@router.post("/{snapshot_id}", response_model=Snapshot)
def create(snapshot_id: int, q: Union[str, None] = None):
    # TODO: Prompt a ChatGPT
    print(f"SNAPSHOT_ID: {snapshot_id}")
    return snapshot_mock
