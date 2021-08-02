from flask import Flask

from config import Config
from models import db
from views import blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()
