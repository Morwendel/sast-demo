from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/search")
def search():
    q = request.args.get("q", "")
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + q + "'"
    cur.execute(query)
    return {"result": cur.fetchall()}

@app.route("/")
def index():
    return "Hello, insecure world!"
