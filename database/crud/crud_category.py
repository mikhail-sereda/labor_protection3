from sqlalchemy import select

from database.model import db_helper, Profession, Category


def check_category(name: str) -> bool:
    """
    Проверяет наличие категории в БД
    :param name:
    :return:
    """
    session = db_helper.get_session()
    stmt = select(Category).where(Category.categoryName == name)
    result_check = session.scalar(stmt)
    return result_check


def db_add_category(name: str) -> Category:
    """
    Добавляет профессию в БД если ранее не было.
    :param name:
    :return:
    """
    session = db_helper.get_session()
    category = check_category(name)
    if not category:
        category = Category(categoryName=name)
        session.add(category)
        session.commit()

    return category
