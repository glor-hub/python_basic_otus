from sqlalchemy import Column, Integer, String, DateTime, func

from .database import db


class Zodiac(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
