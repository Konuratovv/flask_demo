from models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Users(BaseModel):
    __tablename__ = 'users'
    
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))