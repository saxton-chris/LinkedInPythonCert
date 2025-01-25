import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASS = os.getenv("SENDER_PASS")

def send_email(recipient_email, subject, email_message):
    """
    Sends an email using the Gmail SMTP server.
    
    Parameters:
    recipient_email (str): The recipient's email address.
    subject (str): The subject of the email.
    email_message (str): The body/content of the email.
    """
    try:
        # Create a MIMEText object for the email body
        msg = MIMEText(email_message)
        msg['Subject'] = subject
        msg['To'] = recipient_email
        msg['From'] = SENDER_EMAIL

        # Establish a secure connection to the Gmail SMTP server using SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASS)  # Login to the SMTP server
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())  # Send the email

        print(f"Email sent successfully to {recipient_email}")

    except smtplib.SMTPAuthenticationError:
        print("Failed to login: Check your email or app-specific password.")
    except smtplib.SMTPConnectError:
        print("Failed to connect to the SMTP server. Check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    send_email("surfde22@gmail.com", "Test Email", "This is a test email from Python.")
