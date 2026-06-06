import os
from dotenv import load_dotenv
import smtplib, ssl

load_dotenv()

def send_email(message):
    host="smtp.gmail.com"
    port=465

    username=os.getenv("EMAIL_SENDER")
    password=os.getenv("EMAIL_PASSWORD")

    receiver=os.getenv("EMAIL_RECEIVER")
    context=ssl.create_default_context()    

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)