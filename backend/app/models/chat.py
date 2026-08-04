from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base


class ChatMessage(Base):

    __tablename__ = "chat_messages"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )


    question = Column(Text)


    answer = Column(Text)


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    user = relationship(
        "User",
        back_populates="chat_messages"
    )