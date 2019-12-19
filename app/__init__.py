from flask_admin import Admin, AdminIndexView, expose, BaseView
from flask_admin.menu import MenuLink
from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from config import Config
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from app import routes, models


class Controller(ModelView):
    def is_accessible(self):
        if current_user.role_id != 1:
            return False
        return current_user.is_authenticated

    def not_aut(self):
        return "Пожалуйста, войдите в систему"


admin = Admin(app,
              name='Меню для админа',
              template_mode='bootstrap3',
              url='/admin')
# admin.add_view(FirstView())
admin.add_view(Controller(models.Service, db.session, name='Услуги'))
admin.add_view(Controller(models.Application, db.session, name='Заявление'))
admin.add_view(Controller(models.Employee, db.session, name='Сотрудники'))
admin.add_view(Controller(models.NaturalPerson, db.session, name='Физические лица'))
admin.add_view(Controller(models.LegalPerson, db.session, name='Юридические лица'))
admin.add_view(Controller(models.Country, db.session, name='Страны'))
admin.add_view(Controller(models.ForeignLanKnowledge, db.session, name='Знание иностранного языка'))
admin.add_view(Controller(models.CodifOfLanguage, db.session, name='Кодификатор знания языка'))
admin.add_view(Controller(models.CodifOfProficiencyLang, db.session, name='Кодификатор степени знания языка'))
admin.add_view(Controller(models.Client, db.session, name='Клиент'))
admin.add_view(Controller(models.DocumOfClient, db.session, name='Документы клиента'))
admin.add_view(Controller(models.Log, db.session, name='Журнал'))
admin.add_view(Controller(models.Trustee, db.session, name='Доверенное лицо клиента'))
admin.add_view(Controller(models.Form, db.session, name='Бланки'))
admin.add_view(Controller(models.Participant, db.session, name='Участники нот. действия'))
admin.add_view(Controller(models.Role, db.session, name='Роли'))
admin.add_view(Controller(models.User, db.session, name='Пользователи'))
admin.add_link(MenuLink(name='Выход', url='/logout'))
