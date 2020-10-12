from . import db


class PhotoCoordinates(db.Model):
    id = db.Column("id", db.INTEGER, primary_key=True)
    name = db.Column(db.String(), unique = True)
    lan = db.Column(db.String(), unique = True)
    lon = db.Column(db.String(), unique = True)


def __repr__(self):
        return '<PhotoCoordinates {}>'.format(self.name)