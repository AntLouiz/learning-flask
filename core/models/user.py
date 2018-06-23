from core.base import db, ma
from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self


class UserSchema(ma.Schema):

    class Meta:
        fields = ('username',)


user_schema = UserSchema()
