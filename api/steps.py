import json
from typing import List

from fastapi import APIRouter

from models.wizard import Step

from db.mongo import database

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
    return get_step_from_db(step_id)


def get_step_from_db(step_id: int = 1):
    steps_collection = database.steps
    step_data = steps_collection.find_one({"step_id": step_id})

    if step_data:
        return step_data
    else:
        return {"error": "Step not found"}
