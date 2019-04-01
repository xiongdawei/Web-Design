from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route("/")
def index():
    return '<h1>Hello World</h1>'
"""

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    message = "Hello " + str(name)
    return message
"""
@app.route("/")
def table():
    return render_template("table.html")

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, %s!</h1>' % name


@app.route("/")
def index():
    headline = "ICC Building"
    return render_template("index.html", headline = headline)
"""

if __name__ == '__main__':
    app.run(debug = True)
    


