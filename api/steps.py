import json
from typing import List

from fastapi import APIRouter

from models.wizard import Step

router = APIRouter()

with open("resources/mocks/get_steps.json", "r") as f:
    steps_mock = json.load(f)


@router.get("/", response_model=List[Step])
def get(step_id: int = 1):
    # TODO: Take steps from database, maybe MongoDB
    print(f"steps: {steps_mock.get('steps')}")
    return steps_mock.get('steps')


@router.get("/{step_id}", response_model=Step)
def get(step_id: int = 1):
    # TODO: Take steps from database, maybe MongoDB
    print(f"steps: {steps_mock}")
    return steps_mock.get('steps')[step_id]
