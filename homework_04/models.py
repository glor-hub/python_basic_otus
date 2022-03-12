"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    DateTime,
    func,
    String,
    Integer,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    relationship,
    sessionmaker,
)

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/homework_04"
PG_ECHO = True


class Base:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    def __repr__(self):
        return str(self)


engine = create_async_engine(PG_CONN_URI, echo=PG_ECHO)

Session = sessionmaker(engine, expire_on_commit=False,class_=AsyncSession)

Base = declarative_base(bind=engine, cls=Base)


class TimestampMixin:
    created_at = Column(
        DateTime,
        server_default=func.now(),
    )


class User(TimestampMixin, Base):
    username = Column(
        String(32),
        unique=True,
    )

    name = Column(
        String(64),
        unique=False,
        nullable=False,
        default="",
        server_default="",
    )

    email = Column(
        String(64),
        unique=False,
        nullable=False,
        default="",
        server_default="",
    )

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id},\n " \
               f"user_name={self.username!r},\n " \
               f"name={self.name},\n " \
               f"email={self.email},\n " \
               f"created_at={self.created_at!r})\n"


class Post(TimestampMixin, Base):
    title = Column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    user_id = Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=False,
    )

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id},\n " \
               f"title={self.title!r},\n " \
               f"user_id={self.user_id},\n " \
               f"created_at={self.created_at!r})\n"
