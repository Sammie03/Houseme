from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_migrate import Migrate

#Instantiate an object of Flask
app = Flask(__name__, instance_relative_config=True)
csrf=CSRFProtect(app)

#Local imports starts here
from Housemeapp import config 
app.config.from_object(config.ProductionConfig)
app.config.from_pyfile('config.py',silent=False)

db = SQLAlchemy(app)
mail =Mail(app) #instantiate after loading the config
migrate= Migrate(app,db)

#Load your routes here
from Housemeapp.routes import adminroutes, userroutes
from Housemeapp import forms 
from Housemeapp import mymodels

