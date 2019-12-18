from . import app, login_manager
from app.models import *
from flask import render_template, session, request, redirect, flash, url_for
from flask_login import logout_user, login_required, login_user
from app.forms import *
import hashlib


@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    return User.query.filter(User.id == user_id).first()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data.encode()
        hash_passw = hashlib.sha256(password)
        user = User.query.filter(User.username == username).first()
        passw = User.query.filter(User.hash_pass == hash_passw)
        if user and passw:
            print('Ouu')
            login_user(user, remember=form.remember.data)
            session['username'] = form.username.data
            return redirect('/main', 302)

    return render_template('login.html', name=session.get('name'), form=form, known=session.get('known', False))



@app.route('/registry', methods=['GET', 'POST'])
def registry():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate():

        username = form.username.data
        password = form.password.data.encode()
        hashed_password = hashlib.sha256(password)
        print(username, password, hashed_password)
        user = User()
        user.username = username
        user.hash_pass = hashed_password
        db.session.add(user)
        db.session.commit()
    return render_template('form.html', block_title='Register', form=form)


@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    return render_template('index.html')


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))


@app.route('/add_form_employee/')
@login_required
def add_form_employee():
    form = EmployeeForm(request.form)
    if request.method == 'POST' and form.validate():
        employee = Employee()
        employee.surname = form.surname.data
        employee.first_name = form.first_name.data
        employee.farther_name = form.farther_name.data
        employee.address = form.address.data
        employee.sex = form.sex.data
        employee.telephone = form.telephone.data
        employee.type_of_employee = form.type_of_employee.data
        employee.number_of_licence = form.number_of_licence.data
        employee.date_of_lic_issuance = form.date_of_lic_issuance.data
        db.session.add(employee)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_applic/')
@login_required
def add_form_applic():
    form = ApplicationForm(request.form)
    if request.method == 'POST' and form.validate():
        application = Application()
        application.num_of_applic = form.num_of_applic
        application.code_of_employee = form.code_of_employee.data
        application.code_of_service = form.code_of_service.data
        application.date_of_record = form.date_of_record.data
        application.num_of_doc = form.num_of_doc.data
        db.session.add(application)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_client/')
@login_required
def add_form_client():
    form = ClientForm(request.form)
    if request.method == 'POST' and form.validate():
        client = Client()
        client.code_of_type_of_client = form.code_of_type_of_client.data
        client.e_mail = form.e_mail.data
        client.address = form.address.data
        client.telephone = form.telephone.data
        client.code_of_emp = form.code_of_emp.data
        db.session.add(client)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_lang_cod/')
@login_required
def add_form_lang_cod():
    form = CodOfLanForm()
    if request.method == 'POST' and form.validate():
        lang_cod = CodifOfLanguage()
        lang_cod.code_of_lang = form.code_of_lang.data
        lang_cod.name_of_lang = form.code_of_lang.data
        db.session.add(lang_cod)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_country')
@login_required
def add_form_country():
    form = CountryForm()
    if request.method == 'POST' and form.validate():
        country = Country()
        country.code_of_country = form.code_of_country.data
        country.name_of_country = form.name_of_country.data
        db.session.add(country)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_cl_doc/')
@login_required
def add_form_cl_doc():
    form = DocOfClientForm()
    if request.method == 'POST' and form.validate():
        client_doc = DocOfClientForm()
        client_doc.num_of_doc = form.code_of_client.data
        client_doc.code_of_client = form.code_of_client.data
        client_doc.name_of_doc = form.name_of_doc.data
        db.session.add(client_doc)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_lan_know/')
@login_required
def add_form_lan_know():
    form = ForLanKnowForm()
    if request.method == 'POST' and form.validate():
        lan_know = ForeignLanKnowledge()
        lan_know.code_of_empl = form.code_of_empl.data
        lan_know.code_of_lang = form.code_of_lang.data
        lan_know.code_of_knowl = form.code_of_knowl.data
        db.session.add(lan_know)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_forms/')
@login_required
def add_form_forms():
    form = BlankForm()
    if request.method == 'POST' and form.validate():
        forms = Form()
        forms.num_of_form = form.num_of_form.data
        forms.type_of_form = form.type_of_form.data
        forms.num_of_not_act = form.num_of_not_act.data
        db.session.add(forms)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_legal/')
@login_required
def add_form_legal():
    form = LegPersonForm()
    if request.method == 'POST' and form.validate():
        legal = LegalPerson()
        legal.code_of_client = form.cl_code.data
        legal.name_of_client = form.name_of_client.data
        db.session.add(legal)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_log_to_app/')
@login_required
def add_form_log_to_app():
    form = LogAppForm()
    if request.method == 'POST' and form.validate():
        log_app = Log_to_applic()
        log_app.num_of_act = form.num_of_act.data
        log_app.num_of_applic = form.num_of_app.data
        db.session.add(log_app)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_logs/')
@login_required
def add_form_logs():
    form = LogForm()
    if request.method == 'POST' and form.validate():
        log = Log()
        log.date_of_issuance = form.date_of_issuance.data
        log.code_of_client = form.code_of_client.data
        log.code_of_service = form.code_of_service.data
        db.session.add(log)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_nat/')
@login_required
def add_form_nat():
    form = NatPersonForm()
    if request.method == 'POST' and form.validate():
        natural = NaturalPerson()
        natural.code_of_client = form.cl_code.data
        natural.surname = form.surname.data
        natural.first_name = form.first_name.data
        natural.farther_name = form.farther_name.data
        natural.sex = form.sex.data
        natural.date_of_birth = form.date_of_birth.data
        natural.data_marriage = form.data_of_marriage.data
        db.session.add(natural)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_partic/')
@login_required
def add_form_partic():
    form = ParticipantFrom()
    if request.method == 'POST' and form.validate():
        partic = Participant()
        partic.num_of_doc = form.num_of_doc.data
        partic.surname = form.surname.data
        partic.first_name = form.first_name.data
        partic.farther_name = form.farther_name.data
        partic.address = form.address.data
        partic.num_of_not_act = form.num_of_not_act.data
        db.session.add(partic)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_proxy/')
@login_required
def add_form_proxy():
    form = ProxyForm()
    if request.method == 'POST' and form.validate():
        proxy = Proxy()
        proxy.code_of_client = form.cl_code.data
        proxy.code_of_country = form.trustee_doc.data
        db.session.add(proxy)
        db.session.commit()
    return render_template('for_all.html', form=form)



@app.route('/add_form_regist/')
@login_required
def add_form_regist():
    form = RegistForm()
    if request.method == 'POST' and form.validate():
        regist = Registration()
        regist.code_of_client = form.cl_code.data
        regist.code_of_country = form.country_code.data
        db.session.add(regist)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_service/')
@login_required
def add_form_service():
    form = ServiceForm()
    if request.method == 'POST' and form.validate():
        service = Service()
        service.name = form.name.data
        service.cost = form.cost.data
        service.addition_docum = form.addition_doc.data
        db.session.add(service)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/add_form_trustee/')
@login_required
def add_form_trustee():
    form = TrusteeForm()
    if request.method == 'POST' and form.validate():
        trustee = Trustee()
        trustee.num_of_doc = form.num_of_doc.data
        trustee.date_of_regist_of_trust = form.date_of_regist_of_trust.data
        trustee.place_of_regist = form.place_of_regist_of_trust.data
        db.session.add(trustee)
        db.session.commit()
    return render_template('for_all.html', form=form)


@app.route('/show_applic/')
@login_required
def show_applic():
    applic = Application.query.all()
    return render_template('show_applic.html', info=applic)


@app.route('/show_client/')
@login_required
def show_client():
    client = Client.query.all()
    return render_template('show_client.html', info=client)


@app.route('/show_lan_cod/')
@login_required
def show_lan_cod():
    lan_cod = CodifOfLanguage.query.all()
    return render_template('show_lan_code.html', info=lan_cod)


@app.route('/show_prof_cod/')
@login_required
def show_prof_cod():
    prof_cod = CodifOfProficiencyLang.query.all()
    return render_template('show_prof_cod.html', info=prof_cod)


@app.route('/show_country/')
@login_required
def show_country():
    country = Country.query.all()
    return render_template('show_country.html', info=country)


@app.route('/show_client_doc/')
@login_required
def show_client_doc():
    client_doc = DocumOfClient.query.all()
    return render_template('show_client_doc.html', info=client_doc)


@app.route('/show_employee/')
@login_required
def show_employee():
    employee = Employee.query.all()
    return render_template('show_employee.html', info=employee)


@app.route('/show_lan_know/')
@login_required
def show_lan_know():
    lan_know = ForeignLanKnowledge.query.all()
    return render_template('show_lan_know.html', info=lan_know)


@app.route('/show_blank/')
@login_required
def show_blank():
    blank = Form.query.all()
    return render_template('show_blank.html', info=blank)


@app.route('/show_legal/')
@login_required
def show_legal():
    legal = LegalPerson.query.all()
    return render_template('show_legal.html', info=legal)


@app.route('/show_app_log/')
@login_required
def show_app_log():
    app_log = Log_to_applic.query.all()
    return render_template('show_app_log.html', info=app_log)


@app.route('/show_log/')
@login_required
def show_log():
    log = Log.query.all()
    return render_template('show_log.html', info=log)


@app.route('/show_natural/')
@login_required
def show_natural():
    natural = NaturalPerson.query.all()
    return render_template('show_natural.html', info=natural)


@app.route('/show_partic/')
@login_required
def show_partic():
    partic = Participant.query.all()
    return render_template('show_partic.html', info=partic)


@app.route('/show_proxy/')
@login_required
def show_proxy():
    proxy = Proxy.query.all()
    return render_template('show_proxy.html', info=proxy)


@app.route('/show_regist/')
@login_required
def show_regist():
    registration = Registration.query.all()
    return render_template('show_regist.html', info=registration)


@app.route('/show_service/')
@login_required
def show_service():
    service = Service.query.all()
    return render_template('show_service.html', info=service)


@app.route('/show_trustee/')
@login_required
def show_trustee():
    trustee = Trustee.query.all()
    return render_template('show_trustee.html', info=trustee)
