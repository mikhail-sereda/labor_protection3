from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


database_url = "sqlite:///data.db"

class DataHelper:
    def __init__(self, db_url: str, db_echo: bool = True):
        self.engine = create_engine(url=db_url, echo=db_echo)
        self.__session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_session(self):
        with self.__session_factory() as session:
            return session

db_helper = DataHelper(database_url)



