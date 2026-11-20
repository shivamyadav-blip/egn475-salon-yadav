import os
import re
from decimal import Decimal

from flask import Flask, abort, redirect, render_template, request, url_for

import db
from db import get_db

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(app.instance_path, "salon.sqlite")
os.makedirs(app.instance_path, exist_ok=True)
db.init_app(app)


def active_services():
    return get_db().execute(
        """
        SELECT id, name, category, duration_minutes, price_cents
        FROM services
        WHERE active = 1
        ORDER BY name COLLATE NOCASE, id
        """
    ).fetchall()


def salon_appointments():
    return get_db().execute(
        """
        SELECT a.id, a.date, a.time, a.client_name AS client, a.stylist,
               a.status, s.name AS service, s.price_cents
        FROM appointments AS a
        JOIN services AS s ON s.id = a.service_id
        ORDER BY a.date, a.id
        """
    ).fetchall()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book")
def book():
    return render_template("book.html", services=active_services())


@app.route("/services")
def services():
    return render_template("services.html", services=active_services())


@app.route("/services/<int:service_id>")
def service_detail(service_id):
    service = get_db().execute(
        """
        SELECT id, name, category, duration_minutes, price_cents
        FROM services
        WHERE id = ? AND active = 1
        """,
        (service_id,),
    ).fetchone()
    if service is None:
        abort(404, description="The requested salon service was not found.")
    return render_template("service_detail.html", service=service)


@app.route("/admin/services/new", methods=["GET", "POST"])
def new_service():
    if request.method == "GET":
        return render_template("new_service.html", form={})

    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip() or "General"
    duration = request.form.get("duration_minutes", "").strip()
    price = request.form.get("price", "").strip()

    if not name:
        error = "Enter a service name."
    elif not re.fullmatch(r"[0-9]{1,9}", duration) or int(duration) < 1:
        error = "Enter a positive whole number of minutes."
    elif not re.fullmatch(r"[0-9]{1,9}(\.[0-9]{1,2})?", price):
        error = "Enter a nonnegative price with up to two decimal places."
    else:
        price_cents = int(Decimal(price) * 100)
        connection = get_db()
        connection.execute(
            """
            INSERT INTO services (name, category, duration_minutes, price_cents)
            VALUES (?, ?, ?, ?)
            """,
            (name, category, int(duration), price_cents),
        )
        connection.commit()
        return redirect(url_for("services"))

    return render_template("new_service.html", form=request.form, error=error), 400


@app.route("/calendar")
def calendar():
    return render_template("calendar.html", appointments=salon_appointments())


@app.route("/appointments")
def appointments():
    return render_template("appointments.html", appointments=salon_appointments())


if __name__ == "__main__":
    app.run(debug=True)
