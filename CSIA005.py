from flask import Flask, render_template
app = Flask(__name__)


@app.route("/more")
def more():
    return render_template("index003.html")

@app.route("/<name>")
def namee(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run(debug = True)
