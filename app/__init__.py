from flask_admin import Admin
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

admin = Admin(app, name='Меню для админа', template_mode='bootstrap3')
admin.add_view(ModelView(models.Service, db.session, name='Услуги'))
admin.add_view(ModelView(models.Application, db.session, name=''))
admin.add_view(ModelView(models.Employee, db.session, name='Сотрудники'))
admin.add_view(ModelView(models.NaturalPerson, db.session, name='Физические лица'))
admin.add_view(ModelView(models.LegalPerson, db.session, name='Юридические лица'))
admin.add_view(ModelView(models.Country, db.session, name='Страны'))
admin.add_view(ModelView(models.ForeignLanKnowledge, db.session, name='Знание иностранного языка'))
admin.add_view(ModelView(models.CodifOfLanguage, db.session, name='Кодификатор знания языка'))
admin.add_view(ModelView(models.CodifOfProficiencyLang, db.session, name='Кодификатор степени знания языка'))
admin.add_view(ModelView(models.Client, db.session, name='Клиент'))
admin.add_view(ModelView(models.DocumOfClient, db.session, name=''))
admin.add_view(ModelView(models.Log, db.session, name=''))
admin.add_view(ModelView(models.Trustee, db.session, name=''))
admin.add_view(ModelView(models.Form, db.session, name=''))
admin.add_view(ModelView(models.Participant, db.session, name=''))
admin.add_view(ModelView(models.Role, db.session, name=''))
admin.add_view(ModelView(models.User, db.session, name=''))
