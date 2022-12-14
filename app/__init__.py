from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from app.routes.login_bp import login_bp
from app import models, topRoutes

app.register_blueprint(login_bp, url_prefix='/login')
db.create_all()