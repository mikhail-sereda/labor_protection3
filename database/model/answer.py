from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.model import Base


class Answer(Base):
    __tablename__ = "answers"

    answerID: Mapped[int] = mapped_column(primary_key=True)
    answersText: Mapped[str]
    answerCorrect: Mapped[bool]

    questionID: Mapped[int] = mapped_column(ForeignKey("questions.questionsID"))
    question: Mapped["Question"] = relationship(back_populates="answers")

    def __repr__(self) -> str:
        return f"answerID={self.answerID!r}, answersText={self.answersText!r}, answerCorrect={self.answerCorrect!r})"
