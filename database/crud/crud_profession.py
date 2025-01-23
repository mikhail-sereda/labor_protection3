from sqlalchemy import select

from database.model import db_helper, Profession


def check_profession(name: str) -> bool:
    """
    Проверяет наличие профессии в БД
    :param name:
    :return:
    """
    session = db_helper.get_session()
    stmt = select(Profession).where(Profession.professionName == name)
    result_check = session.scalar(stmt)
    return result_check


def db_add_profession(name: str) -> Profession:
    """
    Добавляет профессию в БД если ранее не было.
    :param name:
    :return:
    """
    session = db_helper.get_session()
    profession = check_profession(name)
    if not profession:
        profession = Profession(professionName=name)
        session.add(profession)
        session.commit()

    return profession


def db_get_all_profession():
    session = db_helper.get_session()
    stmt = select(Profession)
    result_check = session.scalars(stmt)
    return result_check


