from pydantic import BaseModel


class QuizRequest(BaseModel):
    questions_num: int
