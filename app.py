
from flask import Flask, render_template

app = Flask(__name__)

SAMPLE_SERVICES = [
    {
        "id": 1,
        "name": "Haircut",
        "category": "Cutting",
        "duration_minutes": 30,
        "price_cents": 3000,
    },
    {
        "id": 2,
        "name": "Hair Coloring",
        "category": "Color",
        "duration_minutes": 90,
        "price_cents": 8000,
    },
    {
        "id": 3,
        "name": "Hair Styling",
        "category": "Styling",
        "duration_minutes": 45,
        "price_cents": 4500,
    },
    {
        "id": 4,
        "name": "Blowout",
        "category": "Styling",
        "duration_minutes": 40,
        "price_cents": 4000,
    },
    {
        "id": 5,
        "name": "Deep Conditioning",
        "category": "Treatment",
        "duration_minutes": 30,
        "price_cents": 2500,
    },
    {
        "id": 6,
        "name": "Highlights",
        "category": "Color",
        "duration_minutes": 120,
        "price_cents": 9500,
    },
]


@app.context_processor
def inject_registered_endpoints():
    return {"registered_endpoints": set(app.view_functions)}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SAMPLE_SERVICES)


if __name__ == "__main__":
    app.run(debug=True)
