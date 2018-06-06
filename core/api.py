from core.base import db
from core.resources import app

db.create_all(app=app)

if __name__ == '__main__':
    app.run(debug=True)
