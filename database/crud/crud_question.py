from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database.crud.crud_answer import db_create_answer
from database.model import db_helper, Profession
from database.model import Question

quest = {"categoryID": 1, "questionsText": "текст вопроса"}
answ = [
    {"answersText": "техт ответа неправильный1", "answerCorrect": False},
    {"answersText": "техт ответа неправильный2", "answerCorrect": False},
    {"answersText": "техт ответа неправильный3", "answerCorrect": False},
    {"answersText": "техт ответа правильный1", "answerCorrect": True}]


def db_create_question(question: dict):
    """
    Создаёт вопрос без ответов и записывает его в БД
    :param question:
    :return:
    """
    session = db_helper.get_session()
    question = Question(**question)
    session.add(question)
    session.commit()
    return question


def db_add_question(question_data: dict, answer_data: list[dict]):
    """
    Добавляет вопрос с ответами в БД
    :param question_data:
    :param answer_data: список ответов
    :return:
    """
    session: Session = db_helper.get_session()
    question_id = db_create_question(question_data)
    for one_answer in answer_data:
        db_create_answer(one_answer, q_id=question_id.questionsID)
    session.commit()


def db_delete_question(question_id):
    """
    Удаляет вопрос и все его ответы
    :param question_id:
    :return:
    """
    session: Session = db_helper.get_session()
    question = session.scalar(select(Question).
                              where(Question.questionsID == question_id))
    session.delete(question)
    session.commit()


# db_add_question(quest, answ)
#
# db_delete_question(12)
