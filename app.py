from flask import Flask, render_template, session, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from forms import NameForm, LoginForm, ServiceForm, ApplicationForm, EmployeeForm, NatPersonForm, LegPersonForm, \
    CountryForm, ForLanKnowForm, CodOfLanForm, CodOfProfLanForm, ClientForm, DocOfClientForm, LogForm, TrusteeForm, \
    BlankForm, ParticipantFrom
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, UserMixin, LoginManager
import hashlib

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    hash_pass = db.Column(db.String(128))
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
                 db.Column('num_and_ser_of_doc', db.Integer, db.ForeignKey('trustee.num_and_ser_of_doc')))
# for nat_per, leg_per and their trustees &&&


Log_to_applic = db.Table('log_to_applic',
                         db.Column('num_of_act', db.Integer, db.ForeignKey('logs.num_of_act')),
                         db.Column('num_of_applic', db.Integer, db.ForeignKey('applications.num_of_applic')))


class Service(db.Model):
    __tablename__ = 'services'
    code_of_service = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(30), unique=True, nullable=False)
    cost = db.Column(db.Integer)
    addition_docum = db.Column(db.VARCHAR, nullable=True)
    application = db.relationship('Application', lazy='dynamic')
    log = db.relationship('Log', lazy='dynamic')


class Application(db.Model):
    __tablename__ = 'applications'
    num_of_applic = db.Column(db.Integer, primary_key=True)
    code_of_employee = db.Column(db.Integer, db.ForeignKey('employees.code_of_employee'))  # **
    code_of_service = db.Column(db.Integer, db.ForeignKey('services.code_of_service'))  # **
    date_of_record = db.Column(db.DATE, nullable=False)
    num_and_ser_of_docum = db.Column(db.Integer, db.ForeignKey('docums_of_client.num_and_ser_of_doc'))  # **
    registrarion = db.relationship('Log', secondary=Log_to_applic, lazy='dynamic')  # ???


class Employee(db.Model):
    __tablename__ = 'employees'
    code_of_employee = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(30), nullable=False)  # фамилия
    first_name = db.Column(db.VARCHAR(20), nullable=False)  # имя
    farther_name = db.Column(db.VARCHAR(30), nullable=True)  # отчество
    address = db.Column(db.VARCHAR(80), nullable=False)
    sex = db.Column(db.Integer)  # 1-male, 2 - female
    telephone = db.Column(db.VARCHAR(15), nullable=False)
    type_of_employee = db.Column(db.VARCHAR(20), nullable=False)
    number_of_licence = db.Column(db.Integer, nullable=True)
    date_of_lic_issuance = db.Column(db.DATE, nullable=True)
    application = db.relationship('Application', lazy='dynamic')
    for_lan_know = db.relationship('ForeignLanKnowledge', lazy='dynamic')
    client = db.relationship('Client', lazy='dynamic')


class NaturalPerson(db.Model):
    __tablename__ = 'natural_persons'
    code_of_client = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(30), nullable=False)
    first_name = db.Column(db.VARCHAR(20), nullable=False)
    farther_name = db.Column(db.VARCHAR(30), nullable=True)
    sex = db.Column(db.Integer)  # 1-male, 2 - female
    date_of_birth = db.Column(db.DATE, nullable=False)
    data_of_marriage = db.Column(db.DATE)  # 1 - in marriage, 2 - not


class LegalPerson(db.Model):
    __tablename__ = 'legal_persons'
    code_of_client = db.Column(db.Integer, primary_key=True)
    name_of_client = db.Column(db.VARCHAR(50), nullable=False)


class Country(db.Model):
    __tablename__ = 'countries'
    code_of_country = db.Column(db.Integer, primary_key=True)
    name_of_country = db.Column(db.VARCHAR(50), nullable=False)


class ForeignLanKnowledge(db.Model):
    __tablename__ = 'foreign_lan_knowledge'
    code_of_lang = db.Column(db.Integer, primary_key=True)
    code_of_empl = db.Column(db.Integer, db.ForeignKey('employees.code_of_employee'))  # **
    code_of_knowl = db.Column(db.Integer, db.ForeignKey('codif_of_proficiency_lang.code_of_profic'))  # **


class CodifOfLanguage(db.Model):
    __tablename__ = 'codif_of_language'
    code_of_lang = db.Column(db.Integer, primary_key=True)
    name_of_lang = db.Column(db.VARCHAR(15), nullable=False)


class CodifOfProficiencyLang(db.Model):
    __tablename__ = 'codif_of_proficiency_lang'
    code_of_profic = db.Column(db.Integer, primary_key=True)
    name_of_profic = db.Column(db.VARCHAR(15), nullable=False)
    for_lan_know = db.relationship('ForeignLanKnowledge', lazy='dynamic')


class Client(db.Model):
    __tablename__ = 'clients'
    code_of_client = db.Column(db.Integer, primary_key=True)
    code_of_type_of_client = db.Column(db.Integer, nullable=False)  # 1 - legal, 2 - natural
    e_mail = db.Column(db.VARCHAR(30))
    address = db.Column(db.VARCHAR(80), nullable=False)
    telephone = db.Column(db.VARCHAR(15), nullable=False)
    code_of_emp = db.Column(db.Integer, db.ForeignKey('employees.code_of_employee'))  # **
    doc_of_client = db.relationship('DocumOfClient', lazy='dynamic')
    log = db.relationship('Log', lazy='dynamic')


class DocumOfClient(db.Model):
    __tablename__ = 'docums_of_client'
    num_and_ser_of_doc = db.Column(db.Integer, primary_key=True)
    code_of_client = db.Column(db.Integer, db.ForeignKey('clients.code_of_client'))  # **
    name_of_doc = db.Column(db.VARCHAR(30), nullable=False)
    application = db.relationship('Application', lazy='dynamic')


class Log(db.Model):
    __tablename__ = 'logs'
    num_of_act = db.Column(db.Integer, primary_key=True)
    date_of_issuance = db.Column(db.DateTime, nullable=False)
    code_of_client = db.Column(db.Integer, db.ForeignKey('clients.code_of_client'))    # **
    code_of_service = db.Column(db.Integer, db.ForeignKey('services.code_of_service'))  # **
    content = db.Column(db.VARCHAR)
    form = db.relationship('Form', lazy='dynamic')
    participant = db.relationship('Participant', lazy='dynamic')
    dbregistration = db.relationship('Application', secondary=Log_to_applic,  lazy='dynamic')


class Trustee(db.Model):
    __tablename__ = 'trustee'
    num_and_ser_of_doc = db.Column(db.Integer, primary_key=True)
    date_of_regist_of_trust = db.Column(db.DATE, nullable=False)
    place_of_regist_of_trust = db.Column(db.VARCHAR(30), nullable=False)


class Form(db.Model):
    __tablename__ = 'forms'
    code_of_form = db.Column(db.Integer, primary_key=True)
    num_of_form = db.Column(db.Integer, nullable=False)
    type_of_form = db.Column(db.VARCHAR(40), nullable=False)
    num_of_not_act = db.Column(db.Integer, db.ForeignKey('logs.num_of_act'))  # **


class Participant(db.Model):
    __tablename__ = 'participants'
    num_and_ser_of_doc = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(30), nullable=False)
    first_name = db.Column(db.VARCHAR(20), nullable=False)
    farther_name = db.Column(db.VARCHAR(30), nullable=True)
    address = db.Column(db.VARCHAR(80), nullable=False)
    num_of_not_act = db.Column(db.Integer, db.ForeignKey('logs.num_of_act'))  # **


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data.encode()
        hash_passw = hashlib.md5(password)
        user = User.query.filter(User.username == username).first()
        passw = User.query.filter(User.hash_pass == hash_passw)
        if user and passw:
            print('Ouu')
            login_user(user, remember=form.remember.data)
            session['username'] = form.username.data
            # return redirect('/show', 302)

    return render_template('index.html', name=session.get('name'), form=form, known=session.get('known', False))


@app.route('/main', methods=['GET', 'POST'])
@login_required
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    form = ServiceForm(request.form)


@app.route('/service', methods=['GET', 'POST'])
@login_required
def service():
    form = ServiceForm(request.form)


@app.route('/application', methods=['GET', 'POST'])
@login_required
def application():
    form = ApplicationForm(request.form)


@app.route('/employee', methods=['GET', 'POST'])
@login_required
def employee():
    form = EmployeeForm(request.form)


@app.route('/natperson', methods=['GET', 'POST'])
def natperson():
    form = NatPersonForm(request.form)


@app.route('/legperson', methods=['GET', 'POST'])
def legperson():
    form = LegPersonForm(request.form)


@app.route('/country', methods=['GET', 'POST'])
def country():
    form = CountryForm(request.form)


@app.route('/lanknow', methods=['GET', 'POST'])
def lanknow():
    form = ForLanKnowForm(request.form)


@app.route('/codeoflan', methods=['GET', 'POST'])
def codeoflan():
    form = CodOfLanForm(request.form)


@app.route('/codeofprof', methods=['GET', 'POST'])
def codeofprof():
    form = CodOfProfLanForm(request.form)


@app.route('/client', methods=['GET', 'POST'])
def client():
    form = ClientForm(request.form)


@app.route('/docofclient', methods=['GET', 'POST'])
def docofclient():
    form = DocOfClientForm(request.form)


@app.route('/log', methods=['GET', 'POST'])
def log():
    form = LogForm(request.form)


@app.route('/trustee', methods=['GET', 'POST'])
def trustee():
    form = TrusteeForm(request.form)


@app.route('/blank', methods=['GET', 'POST'])
def blank():
    form = BlankForm(request.form)


@app.route('/partic', methods=['GET', 'POST'])
def partic():
    form = ParticipantFrom(request.form)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.errorhandler(404)
def page_not_found(er):
    return render_template('404.html'), 404


@app.route('/show', methods=['GET', 'POST'])
@login_required
def show():
    form = NameForm
    user_name = session['user_id']
    return 'Wow, it is you, ' + user_name + '! Hello'


if __name__ == '__main__':
    app.run(debug=True)
