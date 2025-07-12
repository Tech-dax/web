from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# Utiliser DATABASE_URL ou erreur si pas définie
database_url = os.environ.get('DATABASE_URL')
if not database_url:
    raise RuntimeError("La variable d'environnement DATABASE_URL doit être définie dans le fichier .env")

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Exemple modèle
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Créer les tables au lancement (Flask 3.x compatible)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Serveur Flask local connecté à PostgreSQL Render!"

@app.route('/add/<name>')
def add_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f"Utilisateur {name} ajouté."

@app.route('/users')
def list_users():
    users = User.query.all()
    return ', '.join(u.name for u in users) or "Aucun utilisateur."

if __name__ == "__main__":
    app.run(debug=True)
