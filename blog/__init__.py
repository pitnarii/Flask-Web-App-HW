from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate 

#app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e298337a4489b6a598882fa6a6c7fd2045b9702e7d100914'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c21100955:Yamesaki1994@csmysql.cs.cf.ac.uk:3306/c21100955_flask_lab_db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes


