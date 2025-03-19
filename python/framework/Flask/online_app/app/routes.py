from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import current_user, login_user, logout_user, LoginManager
from . import db
from .models import User, Document
from .forms import RegistrationForm, LoginForm, CreateDocForm
bp = Blueprint('main', __name__, url_prefix='/')
login_manager = LoginManager()

# 用户加载器
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/')
def index():
    documents = Document.query.all()
    return render_template('index.html', documents=documents)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@bp.route('/create_doc', methods=['GET', 'POST'])
def create_doc():
    form = CreateDocForm()
    if form.validate_on_submit():
        doc = Document(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(doc)
        db.session.commit()
        flash('Document created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_doc.html', form=form)

@bp.route('/view_doc/<int:doc_id>')
def view_doc(doc_id):
    doc = Document.query.get_or_404(doc_id)
    if doc.user_id != current_user.id:
        flash('You do not have permission to view this document.', 'danger')
        return redirect(url_for('index'))
    return render_template('view_doc.html', doc=doc)

@bp.route('/edit_doc/<int:doc_id>', methods=['GET', 'POST'])
def edit_doc(doc_id):
    doc = Document.query.get_or_404(doc_id)
    if doc.user_id != current_user.id:
        flash('You do not have permission to edit this document.', 'danger')
        return redirect(url_for('index'))
    form = CreateDocForm(obj=doc)
    if form.validate_on_submit():
        doc.title = form.title.data
        doc.content = form.content.data
        db.session.commit()
        flash('Document updated successfully!', 'success')
        return redirect(url_for('view_doc', doc_id=doc.id))
    return render_template('create_doc.html', form=form, doc=doc)