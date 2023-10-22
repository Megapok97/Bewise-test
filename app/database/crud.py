from sqlalchemy.orm import Session
from app.database.models import QuizQuestion
from typing import Optional, Dict


def check_id_question_exists(db: Session, id_question_to_check: int) -> bool:
    return db.query(QuizQuestion).filter(QuizQuestion.id_question == id_question_to_check).first() is not None


def add_new_question(db: Session, question_data: Optional[Dict]):
    new_question = QuizQuestion(
        id_question=question_data["id"],
        question_text=question_data["question"],
        answer_text=question_data["answer"],
        created_at=question_data["created_at"]
    )
    db.add(new_question)
    db.commit()
    return new_question.question_text
