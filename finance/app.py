import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        var_lookup = lookup(symbol)
        price = var_lookup["price"]
        current_user = session["user_id"]
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%Y")



        row = db.execute("SELECT cash FROM users WHERE id = ?", current_user)
        current_cash = row[0]["cash"]
        total_price = (price * shares)

        if var_lookup == None:
            return apology("Symbol not found", 403)

        elif total_price > current_cash:
            return apology("You do not have enough cash", 403)

        else:
            update_cash = current_cash - total_price
            db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, current_user)
            db.execute("INSERT INTO transactions(symbol, shares, value, total, date, time, idName) VALUES (?, ?, ?, ?, ?, ?, ?)", symbol, shares, price, total_price, date, time, current_user)

            test = db.execute("SELECT ? FROM wallets", symbol)
            print(test)
            if test == None:
                print("caca")


        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        symbol = request.form.get("quote")
        var_lookup = lookup(symbol)

        if var_lookup == None:
            return apology("Symbol not found", 403)

        else:
            name = var_lookup["name"]
            price = var_lookup["price"]
            symbol = var_lookup["symbol"]
            return render_template("quoted.html", name=name, price=price, symbol=symbol)

    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        list_of_name = db.execute("SELECT username FROM users")
        z = 0
        for i in list_of_name:
            if request.form.get("regUser") in list_of_name[z]["username"]:
                return apology("Username already taken", 403)
            z += 1


        if not request.form.get("regUser"):
            return apology("Must provide username", 403)

        elif not request.form.get("regPassword"):
            return apology("Must provide password", 403)

        elif request.form.get("regPassword") != request.form.get("regConfirm"):
            return apology("The confirmation is incorrect", 403)

        password = generate_password_hash(request.form.get("regPassword"))
        id = request.form.get("regUser")

        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", id, password)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
