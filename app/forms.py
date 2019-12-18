from wtforms import StringField, SubmitField, IntegerField, DateField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('Логин', [Length(min=2, max=20), validators.DataRequired()])
    password = PasswordField('Пароль', [Length(min=6, max=30), validators.DataRequired()])
    remember = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')


class ServiceForm(FlaskForm):
    name = StringField('Название')
    cost = IntegerField('Стоимость')
    addition_doc = StringField('Дополнительные документы')
    submit = SubmitField('Ввести')


class ApplicationForm(FlaskForm):
    num_of_applic = IntegerField('Номер заявки')
    code_of_employee = IntegerField('Код сотрудника')
    code_of_service = IntegerField('Код услуги')
    date_of_record = DateField('Дата составления')
    num_of_doc = IntegerField('Номер и серия документа')
    submit = SubmitField('Ввести')


class EmployeeForm(FlaskForm):
    surname = StringField('Фамилия')
    first_name = StringField('Имя')
    farther_name = StringField('Отчество')
    address = StringField('Адрес')
    sex = IntegerField('Пол')
    telephone = StringField('Телефон')
    type_of_employee = StringField('Должность')
    number_of_licence = IntegerField('Номер лицензии (при наличии)')
    date_of_lic_issuance = DateField('Дата выдачи лицензии (при наличии)')
    submit = SubmitField('Ввести')


class NatPersonForm(FlaskForm):
    cl_code = IntegerField('Код клиента')
    surname = StringField('Фамилия')
    first_name = StringField('Имя')
    farther_name = StringField('Отчество')
    sex = IntegerField('Пол')
    date_of_birth = DateField('Дата рождения')
    data_of_marriage = DateField('Дата заключения брака')
    submit = SubmitField('Ввести')


class LegPersonForm(FlaskForm):
    cl_code = IntegerField('Код клиента')
    name_of_client = StringField('Название')
    submit = SubmitField('Ввести')


class CountryForm(FlaskForm):
    code_of_country = IntegerField('Код языка')
    name_of_country = StringField('Название языка')
    submit = SubmitField('Ввести')


class ForLanKnowForm(FlaskForm):
    code_of_lang = IntegerField('Код языка')
    code_of_empl = IntegerField('Код сотрудника')
    code_of_knowl = IntegerField('Код знания')
    submit = SubmitField('Ввести')


class CodOfLanForm(FlaskForm):
    code_of_lang = IntegerField('Код языка')
    name_of_lang = IntegerField('Название языка')
    submit = SubmitField('Ввести')


class CodOfProfLanForm(FlaskForm):
    code_of_profic = IntegerField('Код степени знания языка')
    name_of_profic = StringField('Наименование степени')
    submit = SubmitField('Ввести')


class ClientForm(FlaskForm):
    code_of_type_of_client = IntegerField('Код типа лица')
    code_of_country = IntegerField('Код страны клиента')
    e_mail = StringField('Почта')
    address = StringField('Адрес')
    telephone = StringField('Телефон')
    code_of_emp = IntegerField('Код сотрудника, работающего с клиентом')
    submit = SubmitField('Ввести')


class DocOfClientForm(FlaskForm):
    name_of_doc = StringField('Наименование документа')
    num_of_doc = IntegerField('Номер и серия документа')
    code_of_client = IntegerField('Код клиента')
    submit = SubmitField('Ввести')


class LogForm(FlaskForm):
    num_of_act = IntegerField('Номер нотариального действия')
    date_of_issuance = DateField('Дата регистрации')
    code_of_client = IntegerField('Код клиента')
    code_of_service = IntegerField('Код услуги')
    content = StringField('Содержание')
    submit = SubmitField('Ввести')


class TrusteeForm(FlaskForm):
    num_of_doc = IntegerField('Номер и серия документа')
    date_of_regist_of_trust = DateField('Дата регистрации доверенности')
    place_of_regist_of_trust = StringField('Место регистрации')
    submit = SubmitField('Ввести')


class BlankForm(FlaskForm):
    num_of_form = IntegerField('Номер бланка')
    type_of_form = StringField('Тип бланка')
    num_of_not_act = IntegerField('Номер нотариального действия')
    submit = SubmitField('Ввести')


class ParticipantFrom(FlaskForm):
    num_of_doc = IntegerField('Номер и серия документа')
    surname = StringField('Фамилия')
    first_name = StringField('Имя')
    farther_name = StringField('Отчество')
    address = StringField('Адрес')
    num_of_not_act = IntegerField('Номер нотариального действия')
    submit = SubmitField('Ввести')


class LogAppForm(FlaskForm):
    num_of_act = IntegerField('№ нот. действия')
    num_of_app = IntegerField('№ заявки')
    submit = SubmitField('Ввести')


class ProxyForm(FlaskForm):
    cl_code = IntegerField('Код клиента')
    trustee_doc = IntegerField('Номер документа доверенного лица')
    submit = SubmitField('Ввести')


class RegistForm(FlaskForm):
    cl_code = IntegerField('Код клиента')
    country_code = IntegerField('Код страны')
    submit = SubmitField('Ввести')


class RegForm(FlaskForm):
    username = StringField('Username or email', [validators.Length(min=4, max=25),
                                                 validators.DataRequired()])
    email = StringField('E-mail', [validators.DataRequired("Enter a valid email address"),
                                   validators.Email("Enter a valid email address")])
    password = PasswordField('Password', [Length(min=3, max=25),
                                          validators.DataRequired(),
                                          # check_password,
                                          validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Submit")
