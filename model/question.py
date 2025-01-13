from typing import List


from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base


class Question(Base):
    __tablename__ = "questions"

    questionsID: Mapped[int] = mapped_column(primary_key=True)
    questionsText: Mapped[str]
    category: Mapped[List["Category"]] = relationship(
        back_populates="questions", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Question(id={self.questionsID!r}, questionsText={self.questionsText!r}, category={self.category!r})"
