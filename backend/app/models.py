from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database import Base



class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String(255)
    )

    filepath = Column(
        String(500)
    )

    extracted_text = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class ChatMessage(Base):

    __tablename__ = "chat_messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(Integer)

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
