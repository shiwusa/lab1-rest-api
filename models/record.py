from db import db
from sqlalchemy.sql import func


class RecordModel(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    user_name = db.Column(
        db.String(64),
        db.ForeignKey("user.name"),
        unique=False,
        nullable=False
    )
    category_title = db.Column(
        db.String(64),
        db.ForeignKey("category.title"),
        unique=False,
        nullable=False
    )
    created = db.Column(db.TIMESTAMP, server_default=func.now())
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")
