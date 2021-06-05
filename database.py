from app import db





class Zhabrcom(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    title = db.Column(db.String())
    created = db.Column(db.String())
    author = db.Column(db.String())
    image = db.Column(db.String())
    descrypt = db.Column(db.String())
    descrypt_text=db.Column(db.String())