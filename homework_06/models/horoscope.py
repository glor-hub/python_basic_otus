from sqlalchemy import Column, Integer, String, DateTime, func

from .database import db


class Horoscope(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    desc = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


    def __repr__(self):
        return f"<{self.name!r}>"
