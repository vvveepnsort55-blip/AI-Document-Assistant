from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from .base import Base


class Document(Base):

    __tablename__ = "documents"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user = relationship(
            "User",
             back_populates="documents"
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
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

