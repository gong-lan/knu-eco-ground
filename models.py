from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Quiz(Base):
    __tablename__ = "quiz"

    idx = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    choice1 = Column(Text, nullable=False)
    choice2 = Column(Text, nullable=False)
    choice3 = Column(Text, nullable=True)
    answer = Column(Text, nullable=False)
    reference = Column(Text, nullable=True)
    create_date = Column(DateTime, nullable=False)
