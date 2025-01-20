from sqlalchemy import select

from database.model import db_helper

# def db_add_user(user_id: dict) -> None:
#     """
#     Добавляет пользователя в БД если ранее не было, иначе активирует.
#     :param user_id:
#     :return:
#     """
#     session = db_helper.get_session()
#     stmt = select(UsersORM).where(UsersORM.user_tg_id == user_id['user_tg_id'])
#     result_user = session.scalars(stmt)
#     result_user = result_user.first()
#     if not result_user:
#         stmt = insert(UsersORM).values(user_id)
#         await session.execute(stmt)
#     elif not result_user.activity:
#         await db_activates_user(user_id['user_tg_id'])
#     await session.commit()
#
#
# async def db_get_user_id(user_tg_id: int) -> int:
#     """
#     Отдаёт id user по telegram id.
#     :param user_tg_id:
#     :return: id_user: int
#     """
#     session = await get_async_session()
#     stmt = select(UsersORM).where(UsersORM.user_tg_id == user_tg_id).limit(1)
#     result_user = await session.scalar(stmt)
#     if result_user:
#         await session.commit()
#         return result_user.user_id
#     await session.commit()