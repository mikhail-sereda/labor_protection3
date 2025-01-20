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
    session = db_helper.get_session()
    dsp = db_add_profession("ДСП")
    prsd = db_add_profession("ПРСД")
    dsc = db_add_profession("ДСЦ")
    C = db_add_category(name="C")
    B = db_add_category(name="B")
    OGG = db_add_category(name="ОПП")
    dsp = session.scalar(select(Profession)
                         .where(Profession.professionID == dsp.professionID)
                         .options(selectinload(Profession.categories),))
    prsd = session.scalar(select(Profession)
                          .where(Profession.professionID == prsd.professionID)
                          .options(selectinload(Profession.categories),))
    dsc = session.scalar(select(Profession)
                         .where(Profession.professionID == dsc.professionID)
                         .options(selectinload(Profession.categories),))
    dsp.categories.append(B)
    dsp.categories.append(C)
    dsp.categories.append(OGG)
    dsp.categories.append(C)
    dsp.categories.append(OGG)
    dsc.categories.append(C)
    dsc.categories.append(OGG)
    prsd.categories.append(OGG)
    session.commit()


    app = App()
    app.mainloop()
