from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base


class Category(Base):
    __tablename__ = "categories"

    categoryID: Mapped[int] = mapped_column(primary_key=True)
    categoryName: Mapped[str]
    questions_id: Mapped[int] = mapped_column(ForeignKey("questions.questionsID"))
    questions: Mapped[List["Question"]] = relationship(
        back_populates="category", cascade="all, delete-orphan")
