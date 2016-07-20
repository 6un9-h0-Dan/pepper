import flask
import json

from flask import g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask_sslify import SSLify
from flask_redis import Redis
import sendgrid
import settings

DB = SQLAlchemy()
redis_store = Redis()
sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)

import routes
from users.models import User

def configure_login(app):
	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'login'
	login_manager.login_message = ''

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	@app.before_request
	def before_request():
		g.user = current_user


def create_app():
	app = flask.Flask(__name__)
	app.config.from_object(settings)

	DB.init_app(app)
	redis_store.init_app(app)
	routes.configure_routes(app)
	configure_login(app)

	app.jinja_env.filters['json'] = json.dumps
	SSLify(app)
	return app