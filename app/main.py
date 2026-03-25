from app import app
from app.contacts import contacts

app.register_blueprint(contacts)
