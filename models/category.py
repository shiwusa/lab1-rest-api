from db import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    private = db.Column(db.Integer, default=0)
    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        unique=False,
        nullable=True
    )

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")
    user = db.relationship("UserModel", back_populates="category")
