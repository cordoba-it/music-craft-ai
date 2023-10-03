import json

from fastapi import APIRouter, HTTPException

from db.mongo import database
from models.snapshot import Snapshot
from models.wizard import StepData

router = APIRouter()

with open("resources/mocks/post_snapshot.json", "r") as f:
    snapshot_mock = json.load(f)


@router.get("/{snapshot_id}", response_model=Snapshot)
def get(snapshot_id: int = 1):
    # TODO: Take questions from database, maybe MongoDB
    print(f"SNAPSHOT_ID: {snapshot_id}")
    return snapshot_mock


@router.post("/{snapshot_id}", response_model=Snapshot,
             summary="Process responses and updates the model",
             description="- Store answers from the specific step\n"
                         "- Process information with ChatGPT\n"
                         "- Populate the corresponding JSON model")
async def create(snapshot_id: int, step_data: StepData):
    # Obtener la colección de steps y snapshots
    steps_collection = database.steps
    snapshots_collection = database.snapshots

    # Buscar el step correspondiente
    step = steps_collection.find_one({"step_id": step_data.step_id})

    if not step:
        raise HTTPException(status_code=404, detail="Step not found")

    # Update step info con las respuestas
    step["answers"] = step_data.answers

    # Aquí podrías interactuar con ChatGPT si lo necesitas
    # Por ejemplo, para generar el siguiente step basado en las respuestas
    # next_step = chatGPT_process(step)

    # Actualizar el step en la base de datos con las respuestas
    steps_collection.update_one({"step_id": step_data.step_id}, {"$set": step})

    # Buscar el snapshot correspondiente para actualizarlo o devolverlo al final
    snapshot = snapshots_collection.find_one({"snapshot_id": snapshot_id})

    if not snapshot:
        raise HTTPException(status_code=404, detail="Snapshot not found")

    # Suponiendo que tu snapshot tiene un campo de "steps", puedes añadir o actualizar el step
    if "steps" in snapshot:
        # Buscar si el step ya está en los steps del snapshot y actualizarlo
        for s in snapshot["steps"]:
            if s["step_id"] == step_data.step_id:
                s.update(step)
                break
        else:
            # Si no se encuentra el step en los steps del snapshot, añadirlo
            snapshot["steps"].append(step)
    else:
        # Si el snapshot no tiene el campo "steps", lo crea y añade el step
        snapshot["steps"] = [step]

    # Actualizar el snapshot en la base de datos
    snapshots_collection.update_one({"snapshot_id": snapshot_id}, {"$set": snapshot})

    return snapshot
