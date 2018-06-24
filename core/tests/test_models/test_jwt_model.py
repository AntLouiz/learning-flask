from core.models.jwt import RevokedToken
from flask_jwt_extended import create_access_token, get_jti


def test_new_revoked_token(init_db):
    jti = create_access_token(identity='AntLouiz')
    new_revoked_token = RevokedToken(jti=jti)

    assert new_revoked_token.jti == jti


def test_new_revoked_token_on_database(init_db):
    jti = create_access_token(identity='AntLouiz')
    jti = get_jti(jti)
    new_revoked_token = RevokedToken(jti=jti)

    new_revoked_token.add()

    revoked_token = RevokedToken.query.filter_by(jti=jti).first()

    assert revoked_token.jti == jti
