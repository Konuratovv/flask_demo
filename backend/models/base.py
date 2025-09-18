from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import datetime


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    rec_date: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    upd_date: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now, onupdate=datetime.now)
