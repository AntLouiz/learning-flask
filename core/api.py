from flask_heroku import Heroku
from core.base import db
from core.resources import app


heroku = Heroku(app)
db.create_all(app=app)

if __name__ == '__main__':
    app.run(debug=True)
