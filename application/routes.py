from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Events, Users, Event_Details
from application.forms import EventForm, RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')

@app.route('/home')
def home():
    eventData = Events.query.all()
    return render_template('home.html', title='Home',events=eventData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data, 
                password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('event'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/event', methods=['GET', 'POST'])
@login_required
def event():
    form = EventForm()
    if form.validate_on_submit():
        eventData = Events(
            event_name = form.event_name.data,
            event_date = form.event_date.data,
            location = form.location.data,
            description = form.description.data
        )

        db.session.add(eventData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('event.html', title='Event', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    deets = Event_Details.query.filter_by(event_id = event.id).all()
    #events = Events.query.details.filter_by(user_id=user)
    for deet in deets:
       db.session.delete(deet)

    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))

