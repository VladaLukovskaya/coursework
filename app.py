from flask import Flask, render_template, session, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from config import Config
from wtforms import StringField, SubmitField, IntegerField, DateField, PasswordField, validators
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_migrate import Migrate
from forms import NameForm, LoginForm
import hashlib

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __str__(self):
        return 'hello vlada'

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Service(db.Model):
    __tablename__ = 'Services'
    code_of_service = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(30), unique=True)
    cost = db.Column(db.Integer)
    addition_docum = db.Column(db.VARCHAR, nullable=True)

    def __repr__(self):
        return '<Service %r>' % self.name


class Application(db.Model):
    __tablename__ = 'Applications'
    num_of_applic = db.Column(db.Integer, primary_key=True)
    code_of_employee = db.Column(db.Integer, db.ForeignKey('Employees.code_of_employee'))
    code_of_service = db.Column(db.Integer, db.ForeignKey('Services.code_of_service'))
    date_of_record = db.Column(db.DATE)
    series_of_docum = db.Column(db.Integer, db.ForeignKey('Docums_of_client.series_of_doc'))
    number_of_docum = db.Column(db.Integer, db.ForeignKey('Docums_of_client.number_of_doc'))


class Employee(db.Model):
    __tablename__ = 'Employees'
    code_of_employee = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(30))  # фамилия
    first_name = db.Column(db.VARCHAR(20))  # имя
    farther_name = db.Column(db.VARCHAR(30), nullable=True)  # отчество
    address = db.Column(db.VARCHAR(80))
    sex = db.Column(db.Integer)  # 1-male, 2 - female
    telephone = db.Column(db.VARCHAR(15))
    type_of_employee = db.Column(db.VARCHAR)
    number_of_licence = db.Column(db.Integer, nullable=True)
    date_of_lic_issuance = db.Column(db.DATE, nullable=True)


class NaturalPerson(db.Model):
    __tablename__ = 'Natural_Persons'
    code_of_client = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(30))
    first_name = db.Column(db.VARCHAR(20))
    farther_name = db.Column(db.VARCHAR(30), nullable=True)
    date_of_birth = db.Column(db.DATE)
    data_of_marriage = db.Column(db.DATE)  # 1 - in marriage, 2 - not


Proxy = db.Table('proxies',
                 db.Column('code_of_client', db.Integer, db.ForeignKey('Clients.code_of_client')),
                 db.Column('num_of_doc', db.Integer, db.ForeignKey('Trustee.num_of_doc')),
                 db.Column('series_of_doc', db.Integer, db.ForeignKey('Trustee.series_of_doc')))
# for nat_per, leg_per and their trustees &&&


class LegalPerson(db.Model):
    __tablename__ = 'Legal_Persons'
    code_of_client = db.Column(db.Integer, primary_key=True)
    name_of_client = db.Column(db.VARCHAR)


class Country(db.Model):
    __tablename__ = 'Countries'
    code_of_country = db.Column(db.Integer, primary_key=True)
    name_of_country = db.Column(db.VARCHAR(50))


class ForeignLanKnowledge(db.Model):
    __tablename__ = 'Foreign_lan_knowledge'
    code_of_lang = db.Column(db.Integer, primary_key=True)
    code_of_empl = db.Column(db.Integer, primary_key=True)
    code_of_knowl = db.Column(db.Integer, db.ForeignKey('Codif_of_proficiency_lang.code_of_profic'))


class CodifOfLanguage(db.Model):
    __tablename__ = 'Codif_of_language'
    code_of_lang = db.Column(db.Integer, primary_key=True)
    name_of_lang = db.Column(db.VARCHAR(15))


class CodifOfProficiencyLang(db.Model):
    __tablename__ = 'Codif_of_proficiency_lang'
    code_of_profic = db.Column(db.Integer, primary_key=True)
    name_of_profic = db.Column(db.VARCHAR(15))


class Client(db.Model):
    __tablename__ = 'Clients'
    code_of_client = db.Column(db.Integer, primary_key=True)
    code_of_type_of_client = db.Column(db.Integer)  # 1 - legal, 2 - natural
    code_of_country = db.Column(db.Integer)
    e_mail = db.Column(db.VARCHAR(30))
    address = db.Column(db.VARCHAR(80))
    telephone = db.Column(db.VARCHAR(15))
    code_of_emp = db.Column(db.Integer, db.ForeignKey('Employees.code_of_employee'))


Registration = db.Table('registrations',
                 db.Column('code_of_client', db.Integer, db.ForeignKey('Clients.code_of_client')),
                 db.Column('code_of_country', db.Integer, db.ForeignKey('Countries.code_of_country')))


class DocumOfClient(db.Model):
    __tablename__ = 'Docums_of_client'
    number_of_doc = db.Column(db.Integer, primary_key=True)
    series_of_doc = db.Column(db.Integer, primary_key=True)
    code_of_client = db.Column(db.Integer, db.ForeignKey('Clients.code_of_client'))
    name_of_doc = db.Column(db.VARCHAR(30))


class Log(db.Model):
    __tablename__ = 'Logs'
    num_of_act = db.Column(db.Integer, primary_key=True)
    date_of_issuance = db.Column(db.DATE)
    code_of_client = db.Column(db.Integer, db.ForeignKey('Clients.code_of_client'))
    code_of_service = db.Column(db.Integer, db.ForeignKey('Services.code_of_service'))
    content = db.Column(db.VARCHAR)


Registr = db.Table('registrs',
                 db.Column('num_of_act', db.Integer, db.ForeignKey('Logs.num_of_act')),
                 db.Column('num_of_applic', db.Integer, db.ForeignKey('Applications.num_of_applic')))  # &&&


class Trustee(db.Model):
    __tablename__ = 'Trustee'
    num_of_doc = db.Column(db.Integer, primary_key=True)
    series_of_doc = db.Column(db.Integer, primary_key=True)
    date_of_regist_of_trust = db.Column(db.DATE)
    place_of_regist_of_trust = db.Column(db.VARCHAR(30))


class Form(db.Model):
    __tablename__ = 'Forms'
    num_of_form = db.Column(db.Integer, primary_key=True)
    type_of_form = db.Column(db.VARCHAR, primary_key=True)
    num_of_not_act = db.Column(db.Integer, db.ForeignKey('Logs.num_of_act'))


class Participant(db.Model):
    __tablename__ = 'Participants'
    series_of_doc = db.Column(db.Integer, primary_key=True)
    num_of_doc = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.VARCHAR(30))
    first_name = db.Column(db.VARCHAR(20))
    farther_name = db.Column(db.VARCHAR(30), nullable=True)
    address = db.Column(db.VARCHAR)
    num_of_not_act = db.Column(db.Integer, db.ForeignKey('Logs.num_of_act'))


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data  # need encoding
        user = User.query.filter_by(username=username).first()
        if username == User.username:
            return 'Привет,', User.username
    return render_template('index.html', block_title='Логин', form=form)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.errorhandler(404)
def page_not_found(er):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
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

@app.route('/show')
def show():
    user = User()
    return user.id, user.username

if __name__ == '__main__':
    app.run(debug=True)
