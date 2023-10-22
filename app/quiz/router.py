from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.crud import check_id_question_exists, add_new_question
from app.database.database import get_db
from app.quiz.jservice import fetch_random_questions
from app.quiz.schemas import QuizRequest

router = APIRouter()


@router.post("/quiz/")
async def get_quiz_questions(request: QuizRequest, db: Session = Depends(get_db)):
    quiz_questions = []

    attempt = 0
    while len(quiz_questions) < request.questions_num or attempt > 9:
        question_data = fetch_random_questions(request.questions_num - len(quiz_questions))

        if not question_data:
            return None

        for question in question_data:
            existing_question = check_id_question_exists(db, question["id"])
            if not existing_question:
                new_question = add_new_question(db, question)
                quiz_questions.append(new_question)

        attempt += 1


    return quiz_questions
