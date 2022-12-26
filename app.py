from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from flask_qrcode import QRcode
from dotenv import load_dotenv
from random import randrange
import sqlite3
import os
import re


from helpers import currency_names, convert, usd, caesar_digital, caesar_letters, check_letter_keys, hash_URL, caeser_digital_decoding, check_counter, check_url, check_email, Check_For_Inappropriate_Words

app = Flask(__name__)

# Load environment variables for mail information. 
load_dotenv()

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.filters["usd"] = usd

# Enter mail and server information.
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587 
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_DEBUG"] = True
app.config["MAIL_USERNAME"] = os.getenv('MAIL_DEFAULT_SENDER')
app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')
app.config["MAIL_DEFAULT_SENDER"] = os.getenv('MAIL_DEFAULT_SENDER')
app.config["MAIL_MAX_EMAILS"] = 2

# Open mail connection.
mail = Mail(app)

# Open a connection with the flask_qrcode library.
QRcode(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Open and establish a connection to the database.
with sqlite3.connect("URL.db", check_same_thread=False) as db:
    cr = db.cursor()      

@app.route("/", methods=["GET", "POST"])
def url_shortener():            
    if request.method == "POST":

        long_url = request.form.get("long_url").replace(" ", "")

        if long_url and check_url(long_url):

            cr.execute("SELECT short_url FROM url WHERE long_url = ?", (long_url,))

            found = cr.fetchone()

            if found:
                return render_template("url_shortener.html", short_url=found[0], QR_URL=f"https://multitool-cs50.herokuapp.com/{found[0]}")
                
            cr.execute(" SELECT counter, counter_status FROM counter_manager WHERE id_counter = ?", ('1',) )

            results = cr.fetchall()

            CheckCounter = check_counter(results[0][0], results[0][1]) 

            if CheckCounter:
                cr.execute("BEGIN TRANSACTION")

                short_url = hash_URL(int(results[0][0]) + 1)
                cr.execute("INSERT INTO url (long_url, short_url, counter) values(?, ?, '1')", (long_url, short_url))

                counter = str(int(results[0][0])+1)
                
                cr.execute("UPDATE counter_manager SET counter = ? WHERE id_counter = ?", (counter, '1'))

                cr.execute("COMMIT")

                return render_template("url_shortener.html", short_url=short_url, QR_URL=f"https://multitool-cs50.herokuapp.com/{short_url}")
                
            else:
                return render_template("url_shortener.html", error_counter="1")
        else:
            return render_template("error_page.html", error_url_POST="1")
    else:
        return render_template("url_shortener.html")

@app.route("/<short_url>")
def redirection(short_url):

    cr.execute("SELECT counter, long_url FROM url WHERE short_url = ?", (short_url,))

    found = cr.fetchall()
    
    if found:
        cr.execute("BEGIN TRANSACTION")

        counter = str(int(found[0][0])+(1))
        cr.execute("UPDATE url SET counter = ? WHERE short_url = ?", (counter, short_url))

        cr.execute("COMMIT")
        return redirect(found[0][1])
    else:
        return render_template("error_page.html", error_url_GET="1")

@app.route("/click_counter", methods=["GET", "POST"])
def click_counter():
    if request.method == "POST":

        short_url = request.form.get("short_url")

        if check_url(short_url) and short_url:

            short_re = re.split(r"https://multitool-cs50.herokuapp.com/", short_url)

            # The URL is cut to extract the link code from the database.
            # Returns a first element means that the link is not a valid split.
            if short_re[0]:
                return render_template("click_counter.html", error="Your URL does not exist")

            cr.execute("SELECT counter FROM url WHERE short_url = ?", (short_re[1],))

            found = cr.fetchone()

            if found:
                return render_template("click_counter.html", counter=found[0])
            else:
                return render_template("click_counter.html", error="Your URL does not exist")
        else:
            return render_template("click_counter.html", error="The URL is invalid")
    else:
        return render_template("click_counter.html")

@app.route("/currency_converter", methods=["GET", "POST"])
def currency_converter():
    if request.method == "POST":

        from_ = request.form.get("from")
        To = request.form.get("to")
        amount = request.form.get("amount")

        if not from_ or not To or not amount or amount.isdigit() == False or int(amount) < 1:
            return render_template("currency_converter.html", error="Input error")

        result = convert(from_, To, amount)

        if result == None:
            return render_template("currency_converter.html", error="Invalid currency symbol")

        temporary_variable = 0
        return render_template("currency_converter.html", temporary_variable=temporary_variable, result=result, amount=amount, From=from_, To=To)

    else:
        return render_template("currency_converter.html")

@app.route("/QR", methods=["GET", "POST"])
def QR():
    if request.method == "POST":

        data = request.form.get("data")

        if not data:
            return render_template("QR.html", error="Error: You must enter a text or link")

        return render_template("QR.html", data=data)
    else:
        return render_template("QR.html")

@app.route("/caesar", methods=["GET", "POST"])
def caesar():

    if request.method == "POST":

        cipher_decrypt = request.form.get("cipher")
        text = request.form.get("text")
        key = request.form.get("key")
        Encryption_type = request.form.get("Encryption_type")

        if not Encryption_type:
            return render_template("caesar.html", error="Error: Encryption Type")

        if Encryption_type == "digital":
            try:
                if int(key) and text:
                    return render_template("caesar.html", cipher_text=caesar_digital(key, text))
                    
            except:
                return render_template("caesar.html", error="Error: You must enter a text and a numeric key")

        if Encryption_type == "letters":

            if not text or not cipher_decrypt or check_letter_keys(key):
                return render_template("caesar.html",
                  error="Error: You must enter text, specify the type of operation and enter a character key of at least 26 characters and not more, and the character must not be repeated Example: JTrEKyAVOgDXPSnCUIZLFbMWhQ")

            return render_template("caesar.html", cipher_text=caesar_letters(key, text, cipher_decrypt))
            
        if Encryption_type == "digital_decoding":
            
            if not text:
                return render_template("caesar.html", error="Error: You must enter a Ciphertext")

            return render_template("caesar.html", cipher_text=caesar_digital(caeser_digital_decoding(text), text))

        else:
            return render_template("caesar.html", error="Error: 418 &#128588;")
    else:
        return render_template("caesar.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    answer = 0
    if request.method == "POST":

        country = request.form.get("country")
        name = request.form.get("name")
        email = request.form.get("email")
        sub = request.form.get("subject")
        msg = request.form.get("message")

        if int(request.form.get("answer")) != int(request.form.get("correct_answer")) or not name or not email or not msg or not sub or check_email(email) or Check_For_Inappropriate_Words(msg, name, email, sub ,country):
            return render_template("error_page.html", error_message="1")

        # send email
        message = Message(subject=sub, body=f"Name: {name}\nCountry: {country}\nE-Mail: {email}\n\n {msg}", recipients=['omarps552@gmail.com'])
        mail.send(message)
        return render_template("contact.html", Success="Success")
    else:   
        return render_template("contact.html")

@app.context_processor
def context_processor():
    # global variables
    return dict(names=currency_names(1), country=currency_names("country"), number1=randrange(1, 20), number2=randrange(1, 20)
)
