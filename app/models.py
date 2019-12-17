from app import db
from flask_login import UserMixin

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __str__(self):
        return str(self.name)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    hash_pass = db.Column(db.String(65))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # def set_password(self, password):
    #    self.password_hash = generate_password_hash(password)
    #    return self.password_hash

    # def check_password(self, password):
    #    return check_password_hash(self.password_hash, password)


Registration = db.Table('registrations',
                        db.Column('code_of_client', db.Integer, db.ForeignKey('clients.code_of_client')),
                        db.Column('code_of_country', db.Integer, db.ForeignKey('countries.code_of_country')))


Proxy = db.Table('proxies',
                 db.Column('code_of_client', db.Integer, db.ForeignKey('clients.code_of_client')),
                 db.Column('num_of_doc', db.BigInteger, db.ForeignKey('trustee.num_of_doc')))
# for nat_per, leg_per and their trustees &&&


Log_to_applic = db.Table('log_to_applic',
                         db.Column('num_of_act', db.Integer, db.ForeignKey('logs.num_of_act')),
                         db.Column('num_of_applic', db.Integer, db.ForeignKey('applications.num_of_applic')))


class Service(db.Model):
    __tablename__ = 'services'
    code_of_service = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, unique=True, nullable=False)
    cost = db.Column(db.Integer)
    addition_docum = db.Column(db.VARCHAR, nullable=True)
    application = db.relationship('Application', backref='Код услуги', lazy='dynamic')
    log = db.relationship('Log', backref='Код услуги', lazy='dynamic')


class Application(db.Model):
    __tablename__ = 'applications'
    num_of_applic = db.Column(db.Integer, primary_key=True)
    code_of_employee = db.Column(db.Integer, db.ForeignKey('employees.code_of_employee'))  # **
    code_of_service = db.Column(db.Integer, db.ForeignKey('services.code_of_service'))  # **
    date_of_record = db.Column(db.DATE, nullable=False)
    num_of_docum = db.Column(db.BigInteger, db.ForeignKey('docums_of_client.num_of_doc'))  # **


class Employee(db.Model):
    __tablename__ = 'employees'
    code_of_employee = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(50), nullable=False)  # фамилия
    first_name = db.Column(db.VARCHAR(50), nullable=False)  # имя
    farther_name = db.Column(db.VARCHAR(50), nullable=True)  # отчество
    address = db.Column(db.VARCHAR, nullable=False)
    sex = db.Column(db.Integer)  # 1-male, 2 - female
    telephone = db.Column(db.VARCHAR(15), nullable=False)
    type_of_employee = db.Column(db.VARCHAR(20), nullable=False)
    number_of_licence = db.Column(db.Integer, nullable=True)
    date_of_lic_issuance = db.Column(db.DATE, nullable=True)
    application = db.relationship('Application', backref='Код сотрудника', lazy='dynamic')
    for_lan_know = db.relationship('ForeignLanKnowledge', backref='Код сотрудника', lazy='dynamic')
    client = db.relationship('Client', backref='Код сотрудника', lazy='dynamic')


class NaturalPerson(db.Model):
    __tablename__ = 'natural_persons'
    code_of_client = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(50), nullable=False)
    first_name = db.Column(db.VARCHAR(50), nullable=False)
    farther_name = db.Column(db.VARCHAR(50), nullable=True)
    sex = db.Column(db.Integer)  # 1-male, 2 - female
    date_of_birth = db.Column(db.DATE, nullable=False)
    data_marriage = db.Column(db.Integer)  # 1 - in marriage, 2 - not


class LegalPerson(db.Model):
    __tablename__ = 'legal_persons'
    code_of_client = db.Column(db.Integer, primary_key=True)
    name_of_client = db.Column(db.VARCHAR(100), nullable=False)


class Country(db.Model):
    __tablename__ = 'countries'
    code_of_country = db.Column(db.Integer, primary_key=True)
    name_of_country = db.Column(db.VARCHAR(70), nullable=False)


class ForeignLanKnowledge(db.Model):
    __tablename__ = 'foreign_lan_knowledge'
    knowled_id = db.Column(db.Integer, primary_key=True)
    code_of_lang = db.Column(db.Integer, db.ForeignKey('codif_of_language.code_of_lang'))
    code_of_empl = db.Column(db.Integer, db.ForeignKey('employees.code_of_employee'))  # **
    code_of_knowl = db.Column(db.Integer, db.ForeignKey('codif_of_proficiency_lang.code_of_profic'))  # **


class CodifOfLanguage(db.Model):
    __tablename__ = 'codif_of_language'
    code_of_lang = db.Column(db.Integer, primary_key=True)
    name_of_lang = db.Column(db.VARCHAR(50), nullable=False)


class CodifOfProficiencyLang(db.Model):
    __tablename__ = 'codif_of_proficiency_lang'
    code_of_profic = db.Column(db.Integer, primary_key=True)
    name_of_profic = db.Column(db.VARCHAR(50), nullable=False)
    for_lan_know = db.relationship('ForeignLanKnowledge', backref='Код знания языка', lazy='dynamic')


class Client(db.Model):
    __tablename__ = 'clients'
    code_of_client = db.Column(db.Integer, primary_key=True)
    code_of_type_of_client = db.Column(db.Integer, nullable=False)  # 1 - legal, 2 - natural
    e_mail = db.Column(db.VARCHAR(70))
    address = db.Column(db.VARCHAR, nullable=False)
    telephone = db.Column(db.VARCHAR(15), nullable=False)
    code_of_emp = db.Column(db.Integer, db.ForeignKey('employees.code_of_employee'))  # **
    doc_of_client = db.relationship('DocumOfClient', backref='Код клиента', lazy='dynamic')
    log = db.relationship('Log', backref='Код клиента', lazy='dynamic')
    registration = db.relationship('Country', secondary=Registration, lazy='dynamic')
    proxy = db.relationship('Trustee', secondary=Proxy, lazy='dynamic')


class DocumOfClient(db.Model):
    __tablename__ = 'docums_of_client'
    num_of_doc = db.Column(db.BigInteger, primary_key=True)
    code_of_client = db.Column(db.Integer, db.ForeignKey('clients.code_of_client'))  # **
    name_of_doc = db.Column(db.VARCHAR, nullable=False)
    applications = db.relationship('Application', backref='Номер документа клиента', lazy='dynamic')


class Log(db.Model):
    __tablename__ = 'logs'
    num_of_act = db.Column(db.Integer, primary_key=True)
    date_of_issuance = db.Column(db.DateTime, nullable=False)
    code_of_client = db.Column(db.Integer, db.ForeignKey('clients.code_of_client'))    # **
    code_of_service = db.Column(db.Integer, db.ForeignKey('services.code_of_service'))  # **
    content = db.Column(db.VARCHAR)
    form = db.relationship('Form', lazy='dynamic')
    participant = db.relationship('Participant', backref='№ нотариального действия', lazy='dynamic')
    registration = db.relationship('Application', secondary=Log_to_applic,  lazy='dynamic')


class Trustee(db.Model):
    __tablename__ = 'trustee'
    num_of_doc = db.Column(db.BigInteger, primary_key=True)
    date_of_regist_of_trust = db.Column(db.DATE, nullable=False)
    place_of_regist = db.Column(db.VARCHAR, nullable=False)


class Form(db.Model):
    __tablename__ = 'forms'
    code_of_form = db.Column(db.Integer, primary_key=True)
    num_of_form = db.Column(db.Integer, nullable=False)
    type_of_form = db.Column(db.VARCHAR, nullable=False)
    num_of_not_act = db.Column(db.Integer, db.ForeignKey('logs.num_of_act'))  # **


class Participant(db.Model):
    __tablename__ = 'participants'
    num_of_doc = db.Column(db.BigInteger, primary_key=True)
    surname = db.Column(db.VARCHAR(50), nullable=False)
    first_name = db.Column(db.VARCHAR(50), nullable=False)
    farther_name = db.Column(db.VARCHAR(50), nullable=True)
    address = db.Column(db.VARCHAR, nullable=False)
    num_of_not_act = db.Column(db.Integer, db.ForeignKey('logs.num_of_act'))  # **
