from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2: Hello World
@app.route('/')
def hello_world():
    return """
    <h1>Hello World!</h1>
    <p>John D. : afk</p>
    <p>Jane S. : brb</p>
    <p>Richard Roe. : lol</p>
    """

# Task 3: Add template
@app.route('/alberto')
def alberto():
    return render_template('index.html')

# Task 5: GitHub Repo
# https://github.com/alberto93927/CST_205_lab_15