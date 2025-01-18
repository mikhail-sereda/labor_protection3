from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base


class Profession(Base):
    __tablename__ = "professions"

    professionID: Mapped[int] = mapped_column(primary_key=True)
    professionName: Mapped[str]

    categories: Mapped[List["Category"]] = relationship(
        back_populates="professions", secondary="professions_categories")
