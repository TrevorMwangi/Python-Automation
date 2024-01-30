import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

    print("Email sent successfully!")

# Replace these variables with your own values
subject = "Test Email"
body = "This is a test email sent from a Python script."
to_email = "trvrmwangi@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "willfrazier715@gmail.com"
sender_password = "sppj hjhk owki lwld "

# Call the function to send the email
send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password)
