from database.model import db_helper
from database.model import Base

from view.app import App


def create_database():
    # Base.metadata.drop_all(db_helper.engine)
    Base.metadata.create_all(db_helper.engine)


if __name__ == '__main__':
    create_database()
    app = App()
    app.mainloop()
