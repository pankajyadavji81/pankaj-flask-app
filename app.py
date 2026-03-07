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


# CONTACT PAGE + EMAIL SENDING
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        sender_email = "pankajy.tech@gmail.com"
        password = "zcxz ftzg pedr dxah"

        text = f"""
        New Contact Message

        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, password)

        server.sendmail(sender_email, sender_email, text)

        server.quit()

        return "Message Sent Successfully!"

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