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
            return redirect('/show', 302)

    return render_template('login.html', name=session.get('name'), form=form, known=session.get('known', False))


@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    form = EmployeeForm()
    # user_id = session['user_id']
    # if load_user(user_id) == 1:
        #print('adm')
    # if form.validate_on_submit():
    # session['name'] = form.name.data
    print('boom')
    return render_template('for_all.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))


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
    form = ClientForm()
    # if load_user():
    #    print('wuhuu')
    user_id = session['user_id']
    # return 'Wow, it is you, ' + user_id + '! Hello'
    return render_template('for_all.html', form=form)