from sqlalchemy import func
from app import db

class Announcement(db.Model):
    __tablename__ = "announcement"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def __init__(self,title,content):
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Announcement(id={self.id!r}, title={self.title!r}, content={self.content!r})"