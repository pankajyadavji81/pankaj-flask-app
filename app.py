import os
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_mail import Mail, Message

from dotenv import load_dotenv

load_dotenv()

# 1. App Initialization (Sirf ek baar)
app = Flask(__name__)
app.secret_key = 'pankaj_secret_key' 

# 2. Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True


app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', 'pankajy.tech@gmail.com')

mail = Mail(app)

# --- ROUTES ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/work")
def work():
    return render_template("work.html")

    # form  fill

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        sender_email = request.form.get('email')
        subject = request.form.get('subject')
        message_content = request.form.get('message')

        # Basic Validation
        if not name or not sender_email or not message_content:
            flash("All fields are required!", "danger")
            return redirect(url_for('contact'))

        msg = Message(
            subject=f"New Message from {name}: {subject}",
            recipients=['pankajy.tech@gmail.com'],
            reply_to=sender_email,
            body=f"Received a new message from your portfolio:\n\nName: {name}\nEmail: {sender_email}\nSubject: {subject}\n\nMessage:\n{message_content}"
        )

        try:
            mail.send(msg)
            flash("Message sent! I will get back to you soon.", "success")
        except Exception as e:
            print(f"SMTP Error: {e}") 
            flash("Service temporarily unavailable. Please try again later.", "danger")
        
        return redirect(url_for('contact'))

    return render_template("contact.html")

@app.route("/api")
def api():
    data = {
        "name": "Pankaj",
        "course": "B.Tech CSE",
        "skill": "Python Flask"
    }
    return jsonify(data)

# --- RUN SERVER ---

if __name__ == "__main__":
    # host="0.0.0.0" is good for network testing
    app.run(host="0.0.0.0", port=5000, debug=True)