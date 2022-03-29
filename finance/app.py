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

    current_user = session["user_id"]
    total = 0
    i = 0

    wallet_list = db.execute("SELECT * FROM wallets WHERE idName = ?", current_user)
    row2 = db.execute("SELECT cash FROM users WHERE id = ?", current_user)
    current_cash_float = row2[0]["cash"]
    current_cash = round(current_cash_float, 2)

    total_row = db.execute("SELECT total FROM wallets WHERE idName = ?", current_user)
    for row in total_row:
        tmp = total_row[i]["total"]
        total += tmp
        i += 1

    totaltotal_f = total + current_cash
    totaltotal = round(totaltotal_f, 2)

    return render_template("index.html", wallet=wallet_list, cash=current_cash, total=total, totaltotal=totaltotal)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        var_lookup = lookup(symbol)
        price = var_lookup["price"]
        corp_name = var_lookup["name"]
        current_user = session["user_id"]
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%Y")



        row = db.execute("SELECT cash FROM users WHERE id = ?", current_user)
        current_cash = row[0]["cash"]
        total_price_float = (price * shares)
        total_price = round(total_price_float, 2)

        if var_lookup == None:
            return apology("Symbol not found", 403)

        elif shares <= 0:
            return apology("You must provide a positive number of shares")

        elif total_price > current_cash:
            return apology("You do not have enough cash", 403)

        else:
            update_cash = current_cash - total_price
            db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, current_user)
            db.execute("INSERT INTO transactions(symbol, shares, value, total, date, time, idName) VALUES (?, ?, ?, ?, ?, ?, ?)", symbol, shares, price, total_price, date, time, current_user)

            # check if the symbol already exist. If not, create it.
            check_empty = db.execute("SELECT ownID FROM wallets WHERE idName = ? AND symbol = ?", current_user, symbol)
            if check_empty:
                row2 = db.execute("SELECT shares FROM wallets WHERE idName = ? AND symbol = ?", current_user, symbol)
                current_shares = row2[0]["shares"]
                row3 = db.execute("SELECT total FROM wallets WHERE idName = ? AND symbol = ?", current_user, symbol)
                current_total = row3[0]["total"]
                new_shares = current_shares + shares
                new_total = total_price + current_total
                print(new_total)
                db.execute("UPDATE wallets SET shares = ?, value = ?, total = ? WHERE idName = ? AND symbol = ?", new_shares, price, new_total, current_user, symbol)

            else:
                print(total_price)
                db.execute("INSERT INTO wallets (symbol, shares, value, total, name, idName) VALUES (?, ?, ?, ?, ?, ?)", symbol, shares, price, total_price, corp_name, current_user)

            # update the TOTAL cash (total shares + cash)
            total_total_f = 0
            row4 = db.execute("SELECT total FROM wallets WHERE idName = ?", current_user)
            print(row4)

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
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_str = request.form.get("shares")
        shares = int(shares_str)
        var_lookup = lookup(symbol)
        if var_lookup == None:
            return apology("Invalid symbol", 403)

        if symbol == "empty":
            return apology("Invalid symbol", 403)
        elif shares < 0:
            return apology("You cannot sell negative numbers of shares", 403)
        elif shares == 0:
            return apology("You cannot sell 0 shares",403)

        # Liste des symbole que possède l'utilisateur
        current_user = session["user_id"]
        i = 0
        list_symbol = []
        row = db.execute("SELECT symbol FROM wallets WHERE idName = ?", current_user)
        for cell in row:
            list_symbol.append(row[i]["symbol"])
            i += 1

        if symbol not in list_symbol:
            return apology("You do not own this shares", 403)

        # Action que possède l'utilisateur
        row = db.execute("SELECT shares FROM wallets WHERE idName = ? AND symbol = ?", current_user, symbol)
        current_shares = row[0]["shares"]

        if shares > current_shares:
            return apology("You do not have enough action", 403)
        else:
            # Valider la vente et mettre à jour le wallets
            current_price = var_lookup["price"]
            total_price_float = current_price * shares
            total_price = round(total_price_float, 2)
            row2 = db.execute("SELECT cash FROM users WHERE id = ?", current_user)
            current_cash = row2[0]["cash"]
            new_cash_float = current_cash + total_price
            new_cash = round(new_cash_float, 2)

            new_shares = current_shares - shares

            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, current_user)
            db.execute("UPDATE wallets SET shares = ? WHERE idName = ?", new_shares, current_user)
            return redirect("/")


    else:
        current_user = session["user_id"]
        list_symbol = db.execute("SELECT symbol FROM wallets WHERE idName = ?", current_user)
        return render_template("sell.html", symbol=list_symbol)

