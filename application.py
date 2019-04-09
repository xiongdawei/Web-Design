from flask import Flask, render_template
from database_control003 import function


app = Flask(__name__)

a = function()

print(a.complex_search_name('Com'))
@app.route('/')
def index():
    headline = 'Hello, world'
    return render_template('index003.html', headline = headline)


