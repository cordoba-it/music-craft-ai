from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int = Field(description="El ID de la tarea", example=1)
    description: str = Field(description="Descripción de la tarea", example="Escoger la progresión de acordes")
    status: str = Field(description="Estado de la tarea", example="pending")


class Narrative(BaseModel):
    title: str = Field(description="Título del segmento narrativo", example="Esclavitud")
    entity: str = Field(description="Entidad temática del segmento", example="El peso de la tecnología")
    musical_representation: str = Field(description="Representación musical", example="Riffs pesados")
    lyrics: str = Field(description="Letra asociada", example="No me puedo concentrar")


class MelodyData(BaseModel):
    progression: str = Field(description="Progresión de acordes", example="I-IV-V")
    key: str = Field(description="Tonalidad", example="E minor")
    bpm: int = Field(description="Beats por minuto", example=120)
    technical_details: str = Field(description="Detalles técnicos", example="Uso de palm muting en riffs")


class Template(BaseModel):
    narrative: List[Narrative] = Field(description="Lista de segmentos narrativos")
    melody_data: MelodyData = Field(description="Datos de la melodía")
    lyrics: List[str] = Field(description="Letras de la canción", example=["I'm searching for a way"])


class UserData(BaseModel):
    genre: str = Field(description="Género musical", example="Metal")
    instruments: List[str] = Field(description="Instrumentos que se utilizarán", example=["Guitarra", "Piano"])
    reason: str = Field(description="Motivo para crear música", example="Explorar mi creatividad")
    goal: str = Field(description="Objetivo final", example="Profesión")
    elements: List[str] = Field(description="Elementos a incluir", example=["Letra", "Melodía", "Ritmo"])
    time_investment: int = Field(description="Tiempo a invertir en horas", example=15)
    inspirations: List[str] = Field(description="Artistas o bandas de inspiración", example=["Metallica", "Beethoven"])
    concept: str = Field(description="Concepto o tema del proyecto", example="Lucha por la libertad")


class Snapshot(BaseModel):
    snapshot_id: str = Field(description="ID del snapshot", example="123456")
    created_at: datetime = Field(description="Fecha de creación", example="2023-08-28T12:34:56Z")
    user_data: UserData = Field(description="Datos del usuario")
    template: Template = Field(description="Plantilla generada")
    tasks: List[Task] = Field(description="Lista de tareas pendientes o completadas")
