from flask import Blueprint, render_template, request, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


views = Blueprint("views", __name__)

def send_email(title, email,  message):
  # Set up SMTP connection
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()

    # Compose your message
  sender_email = "wouldrathernotsaywho@gmail.com"
  receiver_email = email
  subject = title
  body = message
  
  # Login to your Gmail account
  
  password = "klwm olkw mnqk wzev"
  s.login(sender_email, password)
  


  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = receiver_email
  message['Subject'] = subject

  message.attach(MIMEText(body, 'plain'))

  # Send the email
  s.sendmail(sender_email, receiver_email, message.as_string())
  
  # Terminate the session
  s.quit()


@views.route('/', methods=['GET', 'POST'])
def home():
  is_sent = False
  title = request.form.get("title")
  email = request.form.get("email")
  message = request.form.get("message")
  if email is not None:
    send_email(title, email, message)
    flash("Email sent successfully!", "success")

  print(is_sent)
  return render_template("index.html", variable=is_sent)
