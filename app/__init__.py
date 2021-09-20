from flask import Flask
from config import Config 


from .blueprints.main import main
from .blueprints.auth import auth
from .blueprints.api import api 

from flask_migrate import Migrate 
from .blueprints.auth.models import db as root_db, login_manager

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(main)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view - 'auth.login'
