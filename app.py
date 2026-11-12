
from flask import Flask, render_template

app = Flask(__name__)


@app.context_processor
def inject_registered_endpoints():
    return {"registered_endpoints": set(app.view_functions)}


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
