from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
from app import db
from datetime import datetime
from app.forms import EditProfileForm
from app.forms import AddForm
from app.models import fileTable


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    articles = fileTable.query.paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('index', page=articles.prev_num) \
        if articles.has_prev else None
    return render_template('index.html', title='Home', articles=articles.items, next_url=next_url,
                           prev_url=prev_url)


#Inactive Table
@app.route('/inActive')
@login_required
def deactivate():
    articles = fileTable.query.filter_by(isActive = 0)
    return render_template('inActive.html', articles = articles)


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    articles = fileTable.query.filter_by(isActive=1).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('explore', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('explore', page=articles.prev_num) \
        if articles.has_prev else None
    return render_template("index.html", title='Explore', articles=articles.items,
                          next_url=next_url, prev_url=prev_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')

        return redirect(url_for('edit_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template('edit_profile.html', title='Edit Profile', form=form)


# Add File
@app.route('/add_files', methods=['GET', 'POST'])
def add_files():
    form = AddForm()
    if form.validate_on_submit():
        new_file = fileTable(Station_Code=form.Station_Code.data,
                             Station_Name=form.Station_Name.data,
                             Location = form.Location.data,
                             Month = form.Month.data,
                             Day = form.Day.data,
                             Year = form.Year.data,
                             Weather = form.Weather.data,
                             PC = form.PC.data,
                             Client = form.Client.data,
                             Type = form.Type.data,
                             Longitude = form.Longitude.data,
                             Latitude = form.Latitude.data)
        db.session.add(new_file)
        db.session.commit()
        flash('New File Created!', 'success')
        return redirect(url_for('index'))
    return render_template('add_files.html', form=form)


#Edit File
@app.route('/edit_files/<int:ID>', methods=['GET', 'POST'])
def edit_files(ID):
    articles = fileTable.query.filter_by(ID=ID).one()

    #Get form
    form = AddForm(obj=articles)

    if form.validate_on_submit():
        form.populate_obj(articles)
        articles.Station_Code = form.Station_Code.data
        articles.Station_Name = form.Station_Name.data
        articles.Location = form.Location.data
        articles.Month = form.Month.data
        articles.Day = form.Day.data
        articles.Year = form.Year.data
        articles.Weather = form.Weather.data
        articles.PC = form.PC.data
        articles.Client = form.Client.data
        articles.Type = form.Type.data
        articles.Longitude = form.Longitude.data
        articles.Latitude = form.Latitude.data
        db.session.commit()
        flash('File Updated!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_files.html', form=form, articles=articles)