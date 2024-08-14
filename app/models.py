from app import db


class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    link = db.Column(db.String(200), nullable=True)
    note = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<WishlistItem {self.name}>"
