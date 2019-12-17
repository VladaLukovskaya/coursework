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
        email = form.email.data
        salt = username.encode()
        hashed_password = hashlib.md5(password + salt).hexdigest()
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
    emp = Employee.query.filter_by()
    form = EmployeeForm(request.form)
    if request.method == 'POST' and form.validate():
        employee = EmployeeForm(
            code_of_employee=form.code_of_employee.data,
            surname = form.surname.data,
            first_name = form.first_name.data,
            farther_name = form.farther_name.data,
            address = form.address.data,
            sex =form.sex.data,
            telephone = form.telephone.data,
            type_of_employee = form.type_of_employee.data,
            number_of_licence = form.number_of_licence.data,
            date_of_lic_issuance = form.date_of_lic_issuance.data,
        )
        db.session.add(employee)
        db.session.commit()
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

