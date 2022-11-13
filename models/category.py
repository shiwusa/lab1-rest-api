from db import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")
