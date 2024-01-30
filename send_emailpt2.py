import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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

def send_email(subject, body, receiver_email, smtp_server, smtp_port, sender_email, sender_password, attachment_path=None):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Attach the text file if provided
    if attachment_path:
        attach_file(message, attachment_path)

    # Connect to the SMTP server
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

def attach_file(message, file_path):
    # Open and attach the file
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file_path.split('/')[-1]}"
        )
        message.attach(part)

# Replace these variables with your own values
subject = "Test Email with Attachment"
body = "This is a test email sent from a Python script with an attachment."
receiver_email = "trvrmwangi@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "willfrazier715@gmail.com"

# Ask for the password securely with asterisks
sender_password = get_hidden_input("Enter your Gmail password: ")
print("Sending your email now!")

# Specify the path to the text file you want to attach
attachment_path = r"C:\Users\TREVOR\Documents\GitHub\Python-Automation\CortexDiagnoseReport.txt" 
# Call the function to send the email with attachment
send_email(subject, body, receiver_email, smtp_server, smtp_port, sender_email, sender_password, attachment_path)
