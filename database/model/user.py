from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.model import Base


class User(Base):
    __tablename__ = "users"

    userID: Mapped[int] = mapped_column(primary_key=True)
    userFirstName: Mapped[str]
    userLastName: Mapped[str]
    userPatronymic: Mapped[str]

    professionID: Mapped[int] = mapped_column(ForeignKey("professions.professionID"))
    profession: Mapped["Profession"] = relationship(back_populates="users")
