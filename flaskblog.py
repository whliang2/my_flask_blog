from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisttrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0a0f7201aa53977e832eeab846cac2e3'



posts =[
    {
      'author':'Henry',
      'title':'Blog Post 1',
      'content':'Hello world!',
      'date_posted':'April 20, 2018'
    },
        {
      'author':'Andy',
      'title':'Blog Post 2',
      'content':'Hello HIIII!',
      'date_posted':'April 23, 2018'
    }
]





@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisttrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You Have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password!','danger')
    return render_template('login.html', title='Login', form=form)





if __name__ == '__main__':
    app.run(debug=True)