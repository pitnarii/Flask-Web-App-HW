from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post, Comment
from blog.forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home():
  posts= Post.query.all()
  posts = Post.query.order_by(Post.date) 
  return render_template('home.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html', title='About Me')

#Add post page
@app.route('/add-post', methods=['GET','POST'])
def add_post():
  form = PostForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, content=form.content.data, author=form.author.data, slug=form.slug.data)
    #clear the form
    form.title.data = ''
    form.content.data = ''
    form.author.data = ''
    form.slug.data = ''
    #add post data to db
    db.session.add(post)
    db.session.commit()

    flash("Blog Post submitted successfully")
  return render_template("add_post.html", form=form)

@app.route('/posts')
def posts():
  #all the post from db
  posts = Post.query.order_by(Post.date)
  return render_template('posts.html', posts=posts)

@app.route('/posts/<int:id>')
def post(id):
  post = Post.query.get_or_404(id)
  return render_template('post.html', post=post)

@app.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('registered'))
  flash('Sorry, there is a problem with your registration')
  return render_template('register.html', title='Register',form=form)
    
@app.route('/registered')
def registered():
  return render_template('registered.html', title='thanks!')

@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if request.method=='POST':
    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)
    flash('You\'ve successfully logged in.')
    return redirect(url_for('home'))
  flash('Invalid email or password supplied.')
  return render_template('login.html',title='Login',form=form)

@app.route('/logout')
def logout():
  logout_user()
  flash('You have been logged out')
  return redirect(url_for('home'))

@app.route('/create-comment/<post_id>', methods=['POST'])
@login_required
def create_comment(post_id):
  text = request.form.get('text')
  if not text:
    flash('Comment cannot be empty.', category='error')
  else:
    post = Post.query.filter_by(id=post_id)
    if post:
      comment = Comment(text=text, author=current_user.id, post_id=post_id)
      db.session.add(comment)
      db.session.commit()
    else:
      flash('Post does not exist.', category='error')

  return redirect(url_for('home'))
