from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    names = ["David_D","David_X","James","Cyka_Blyat"]
    return render_template("index002.html", names = names)

if __name__ == "__main__":
    app.run(debug = True)
