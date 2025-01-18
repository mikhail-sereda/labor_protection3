from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base


class ProfessionCategory(Base):
    __tablename__ = "professions_categories"

    categoryID: Mapped[int] = mapped_column(ForeignKey("categories.categoryID", ), primary_key=True)
    professionID: Mapped[int] = mapped_column(ForeignKey("professions.professionID"), primary_key=True)
