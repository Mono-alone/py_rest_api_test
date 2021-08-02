from flask.blueprints import Blueprint

from models import User

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
def index():
    return 'Hello, world!'


@blueprint.route('/user/<username>')
def user(username):
    return User.query.filter_by(username=username).first().to_dict()
