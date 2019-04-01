from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, World"
    return render_template("table.html", headline = headline)


 @app.route("/hello")
def indexx():
    names = ["David_D","David_X","James"]
    return render_template("table.html", names = names)

if __name__ == "__main__":
    app.run(debug = True)
