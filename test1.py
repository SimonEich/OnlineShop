from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/h")
def hallo():
    return 'hallo willkommen'

app.run(debug=True)
