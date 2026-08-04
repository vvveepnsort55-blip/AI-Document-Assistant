from models.base import Base
from database import engine

# مهم: مدل‌ها باید قبل از create_all لود شوند
from models.user import User
from models.document import Document
from models.chat import ChatMessage


print("USER:", User)
print("DOCUMENT:", Document)
print("CHAT:", ChatMessage)

print("TABLES:")
print(Base.metadata.tables.keys())


Base.metadata.create_all(bind=engine)

print("DONE")