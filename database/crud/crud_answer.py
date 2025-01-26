from sqlalchemy import select

from database.model import db_helper, Answer
from sqlalchemy.orm import Session


def db_create_answer(answer_data: dict, q_id):
    """
    Создаёт ответ в БД
    :param answer_data:
    :param q_id:
    :return:
    """
    session = db_helper.get_session()
    answer = Answer(**answer_data, questionID=q_id)
    session.add(answer)
    session.commit()
    return answer


def db_delete_answer(answer_id):
    """
    Удаляет ответ
    :param answer_id:
    :return:
    """
    session: Session = db_helper.get_session()
    question = session.scalar(select(Answer).
                              where(Answer.answerID == answer_id))
    session.delete(question)
    session.commit()
