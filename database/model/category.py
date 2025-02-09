from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.model import Base


class Category(Base):
    __tablename__ = "categories"

    categoryID: Mapped[int] = mapped_column(primary_key=True)
    categoryName: Mapped[str]
    categoryDesc: Mapped[str]

    questions: Mapped[List["Question"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

    professions: Mapped[List["Profession"]] = relationship(
        back_populates="categories", secondary="professions_categories"
    )
