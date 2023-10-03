from typing import List, Optional

from pydantic import BaseModel, Field


class Question(BaseModel):
    id: int = Field(examples=[1])
    type: str = Field(examples=["text"])
    question: str = Field(examples=["¿Cuál es tu género musical favorito?"])


class Answer(BaseModel):
    question_id: int = Field(examples=[1])
    type: str = Field(examples=["text"])
    answer: str = Field(examples=["HipHop, LoFi"])


class Step(BaseModel):
    step_id: int = Field(examples=[1])
    step_name: str = Field(examples=["Contexto General"])
    questions: List[Question]


class StepData(BaseModel):
    step_id: int = Field(examples=[1])
    answers: List[Answer]
