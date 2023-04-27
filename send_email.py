import smtplib
import ssl
import os


def send_email(msg):
    host = "smtp.gmail.com"
    # Default SMTP-over-SSL port!
    port = 465

    context = ssl.create_default_context()

    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, msg.encode("utf-8"))
