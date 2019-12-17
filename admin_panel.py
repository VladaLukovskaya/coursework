from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.server import app
from app.server import Service, Application, Employee, NaturalPerson, LegalPerson, Country, ForeignLanKnowledge, \
    CodifOfLanguage, CodifOfProficiencyLang, Client, DocumOfClient, Log, Trustee, Form, Participant, Role, User, \
    Registration, Proxy, Log_to_applic
from app.server import db


admin = Admin(app, name='Меню для админа', template_mode='bootstrap3')
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(Application, db.session))
admin.add_view(ModelView(Employee, db.session))
admin.add_view(ModelView(NaturalPerson, db.session))
admin.add_view(ModelView(LegalPerson, db.session))
admin.add_view(ModelView(Country, db.session))
admin.add_view(ModelView(ForeignLanKnowledge, db.session))
admin.add_view(ModelView(CodifOfLanguage, db.session))
admin.add_view(ModelView(CodifOfProficiencyLang, db.session))
admin.add_view(ModelView(Client, db.session))
admin.add_view(ModelView(DocumOfClient, db.session))
admin.add_view(ModelView(Log, db.session))
admin.add_view(ModelView(Trustee, db.session))
admin.add_view(ModelView(Form, db.session))
admin.add_view(ModelView(Participant, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Registration, db.session))
admin.add_view(ModelView(Proxy, db.session))
admin.add_view(ModelView(Log_to_applic, db.session))

