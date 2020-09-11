from flask import Flask, render_template, url_for
app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)