from app.blueprints.auth.models import User, Character
from app import db, create_app


app = create_app()

app.shell.context_processor
def make_context(): 
    return {
        'User': User,
        'db': db,
        'Character' : Character
    }
