from typing import List, Optional

from pydantic import BaseModel, Field


class Question(BaseModel):
    id: int = Field(examples=[1])
    type: str = Field(examples=["type"])
    question: str = Field(examples=["¿Cuál es tu género musical favorito?"])


class Step(BaseModel):
    step_id: int = Field(examples=[1])
    group: str = Field(examples=["Contexto General"])
    questions: List[Question]
