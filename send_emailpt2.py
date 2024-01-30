''' Using MIME (Multipurpose Internet Mail Extensions). Its is a standard that 
 extends the format of email messages to support text in character sets other than ASCII
  as well as attachements of audio, video,images and app programs.'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import msvcrt

def get_hidden_input(prompt="Enter password: "):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            print()
            break
        elif char == '\b':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    return password

def send_email(subject, body, receiver_email, smtp_server, smtp_port, sender_email, sender_password):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

# Replace these variables with your own values
subject = "Test Email"
body = "This is a test email sent from a Python script."
receiver_email = "trvrmwangi@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "willfrazier715@gmail.com"

# Ask for the password securely with asterisks
sender_password = get_hidden_input("Enter your Gmail password: ")
print("Sending your email now!")

# Call the function to send the email
send_email(subject, body, receiver_email, smtp_server, smtp_port, sender_email, sender_password)
