from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import current_user, login_user, logout_user, LoginManager, login_required
from . import db
from .models import User, Document
from .forms import RegistrationForm, LoginForm, CreateDocForm

# Blueprint 用来把一组相关路由组织在一起。
# 这里的蓝图名称是 main，因此 url_for 中的端点名需要写成 main.index、main.login 等。
bp = Blueprint('main', __name__, url_prefix='/')

# LoginManager 负责管理用户登录状态，并在需要登录的页面上拦截匿名用户。
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message = 'Please log in to access this page.'

# 用户加载器：Flask-Login 会把 session 中保存的 user_id 交给这个函数。
# 返回 User 对象后，current_user 才能代表当前登录用户。
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@bp.route('/')
def index():
    # 首页展示所有文档。真实项目中可以按创建时间排序，或只展示当前用户的文档。
    documents = Document.query.all()
    return render_template('index.html', documents=documents)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # 已登录用户不应该再次进入注册流程，直接回到首页。
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    # Flask-WTF 会根据请求方法自动处理表单数据和 CSRF 校验。
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
    # 已登录用户重复访问登录页时，直接回到首页。
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)

            # next 参数表示用户登录前原本想访问的页面。
            # 这里只演示基本跳转；生产环境还应该校验 next 是否为站内地址，避免开放重定向。
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    # logout_user 会清理 Flask-Login 写入 session 的用户标识。
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/create_doc', methods=['GET', 'POST'])
@login_required
def create_doc():
    form = CreateDocForm()
    if form.validate_on_submit():
        # current_user 只有在登录后才可靠，因此本视图需要 login_required。
        doc = Document(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(doc)
        db.session.commit()
        flash('Document created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_doc.html', form=form)

@bp.route('/view_doc/<int:doc_id>')
@login_required
def view_doc(doc_id):
    doc = Document.query.get_or_404(doc_id)
    # 简单权限校验：只允许作者查看自己的文档。
    if doc.user_id != current_user.id:
        flash('You do not have permission to view this document.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('view_doc.html', doc=doc)

@bp.route('/edit_doc/<int:doc_id>', methods=['GET', 'POST'])
@login_required
def edit_doc(doc_id):
    doc = Document.query.get_or_404(doc_id)
    # 修改数据前先检查所有权，避免用户通过猜测 ID 修改别人的文档。
    if doc.user_id != current_user.id:
        flash('You do not have permission to edit this document.', 'danger')
        return redirect(url_for('main.index'))

    # obj=doc 会把已有数据填入表单，适合编辑页面复用创建表单。
    form = CreateDocForm(obj=doc)
    if form.validate_on_submit():
        doc.title = form.title.data
        doc.content = form.content.data
        db.session.commit()
        flash('Document updated successfully!', 'success')
        return redirect(url_for('main.view_doc', doc_id=doc.id))
    return render_template('create_doc.html', form=form, doc=doc)
