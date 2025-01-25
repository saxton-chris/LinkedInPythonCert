# Importing necessary libraries
import smtplib  # Library to handle sending emails via Simple Mail Transfer Protocol (SMTP)
from email.mime.text import MIMEText  # MIMEText is used to create plain text email messages

# The sender's email address and the corresponding app-specific password
SENDER_EMAIL = 'csaxt0015@gmail.com'
SENDER_PASS = 'sfbo txws airp ojdm'  # Ensure this is an app-specific password, not your actual Gmail password, for security

# Function to send an email
def send_email(recipient_email, subject, email_message):
    """
    Sends an email using the Gmail SMTP server.
    
    Parameters:
    recipient_email (str): The recipient's email address.
    subject (str): The subject of the email.
    email_message (str): The body/content of the email.
    """
    
    # Create a MIMEText object for the email body
    msg = MIMEText(email_message)
    msg['Subject'] = subject  # Set the subject of the email
    msg['To'] = recipient_email  # Set the recipient's email address
    msg['From'] = SENDER_EMAIL  # Set the sender's email address
    
    # Establish a secure connection to the Gmail SMTP server using SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASS)  # Login to the SMTP server with sender credentials
        # Send the email using the sendmail method
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())

# Sending a test email
send_email('surfde22@gmail.com', 'Test Email', 'This is a test email from python')
