import os
from dotenv import load_dotenv  
import smtplib, ssl

load_dotenv()

def send_email(message):
    host ="smtp.gmail.com"
    port=465

    sender=os.getenv("EMAIL_SENDER")
    password=os.getenv("EMAIL_PASSWORD")

    receiver=os.getenv("EMAIL_RECEIVER")
    context=ssl.create_default_context() 
    # the above line is for security, it creates a secure connection to the email server. 

    with smtplib.SMTP_SSL(host, port, context=context) as server:
    # the above line is for connecting to the email server using SSL (Secure Sockets Layer) encryption.

        server.login(sender,password)
        # the above line is for logging into the email server using the sender's email address and password.
        server.sendmail(sender,receiver,message)
        # the above line is for sending the email from the sender to the receiver with the specified message.

send_email("Hi how are you")