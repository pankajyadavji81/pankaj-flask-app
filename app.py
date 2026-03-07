import smtplib

from flask import Flask, render_template, request, jsonify
import smtplib

app = Flask(__name__)

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


# CONTACT PAGE + EMAIL SENDING
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        try:
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            message = request.form["message"]

            sender_email = "pankajy.tech@gmail.com"
             password = "abcd efgh ijkl mnop"

            text = f"""
Subject: New Contact Form Message

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(sender_email, password)

            server.sendmail(sender_email, sender_email, text)

            server.quit()

            return "Message Sent Successfully!"

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("contact.html")


@app.route("/api")
def api():
    data = {
        "name": "Pankaj",
        "course": "B.Tech CSE",
        "skill": "Python Flask"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)