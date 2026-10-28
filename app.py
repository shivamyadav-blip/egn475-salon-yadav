
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Salon Management System</h1>
    <h2>Welcome to Yadav Salon</h2>
    <p>Professional Salon Booking and Management</p>
    <p>Developed by Shivam Birat Yadav</p>
    <a href="/about">About Our Salon</a>
    """

@app.route("/about")
def about():
    return """
    <h1>About Yadav Salon</h1>
    <p>Our salon provides professional beauty and grooming services.</p>
    <a href="/">Back to Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
