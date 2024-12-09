from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # Inisialisasi Flask
app.config.from_object(Config)  # Memuat konfigurasi dari objek Config

db = SQLAlchemy(app)  # Inisialisasi SQLAlchemy
migrate = Migrate(app, db)  # Inisialisasi Flask-Migrate
from app import routes
from app.model import user, todo
