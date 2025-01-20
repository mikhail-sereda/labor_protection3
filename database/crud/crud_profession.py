from sqlalchemy import select

from database.model import db_helper, Profession


def check_profession(name: str) -> bool:
    session = db_helper.get_session()
    stmt = select(Profession).where(Profession.professionName == name)
    result_check = session.scalar(stmt)
    print(11, result_check)
    return bool(result_check)


def db_add_profession(name: str) -> Profession:
    """
    Добавляет пользователя в БД если ранее не было, иначе активирует.
    :param name:
    :return:
    """
    session = db_helper.get_session()
    if not check_profession(name):
        profession = Profession(professionName=name)
        session.add(profession)
        session.commit()
        return profession



