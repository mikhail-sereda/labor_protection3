# from sqlalchemy import select
#
# from database.model import db_helper, Profession
#
#
# def get_questions_for_profession(name: str) -> bool:
#     """
#     Проверяет наличие профессии в БД
#     :param name:
#     :return:
#     """
#     session = db_helper.get_session()
#     stmt = select(Profession).where(Profession.professionName == name)
#     result_check = session.scalar(stmt)
#     return bool(result_check)