from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from app_app_app import routes, model

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app_app_app import routes, model
