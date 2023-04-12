from flask import Flask, url_for, redirect, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.htm")


@app.route("/newcust")
def new_customer():
    return render_template("customer.htm")


@app.route("/addrec", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        name = request.form["customer_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        zip = request.form["zip"]

        cmd = "INSERT INTO customers (name, email, phone, zip) VALUES ('{0}', '{1}', '{2}', '{3}')".format(name, email, phone, zip)

        with sql.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()
            msg = "Customer data successfully saved."
            return render_template("output.htm", msg = msg)
        

@app.route("/report")
def report():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cmd = "SELECT * FROM customers"
    cur = conn.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.close()
    return render_template("report.htm", rows = rows)

if __name__ == "__main__":
    app.run(debug = True)