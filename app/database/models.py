from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import engine

Base = declarative_base()


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)
    id_question = Column(Integer, index=True)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime())


Base.metadata.create_all(bind=engine)
