# db_setup.py
from server import app
from server.models import db

with app.app_context():
    db.create_all()
