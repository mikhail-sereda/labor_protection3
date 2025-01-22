from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.crud.crud_category import db_add_category
from database.crud.crud_profession import db_add_profession
from database.model import db_helper, Profession
from database.model import Base

from view.app import App


def create_database():
    # Base.metadata.drop_all(db_helper.engine)
    Base.metadata.create_all(db_helper.engine)


if __name__ == '__main__':
    create_database()
    # dsp = session.scalar(select(Profession)
    #                      .where(Profession.professionID == dsp.professionID)
    #                      .options(selectinload(Profession.categories),))
    app = App()
    app.mainloop()
