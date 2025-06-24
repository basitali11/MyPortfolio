import smtplib
import ssl
import os
from dotenv import load_dotenv
from datetime import datetime
import streamlit as st

load_dotenv()

def send_email(name, sender_email, subject, message):
    """
    Send email using SMTP with environment variables
    """
    try:
        # Email configuration from environment variables
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
        
        RECEIVING_EMAIL = "basitali171480@gmail.com"
        
        # Create email content
        email_subject = f"Portfolio Contact: {subject}"
        email_body = f"""
New message from your portfolio website!

From: {name}
Email: {sender_email}
Subject: {subject}

Message:
{message}

Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        # Create message using proper email format
        full_message = f"Subject: {email_subject}\nFrom: {EMAIL_ADDRESS}\nTo: {RECEIVING_EMAIL}\n\n{email_body}"
        
        # Create secure connection and send email
        context = ssl.create_default_context()
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECEIVING_EMAIL, full_message)
        
        return True
        
    except smtplib.SMTPAuthenticationError:
        st.error("Email authentication failed. Please check your email credentials.")
        return False
    except smtplib.SMTPException as e:
        st.error(f"SMTP error occurred: {str(e)}")
        return False
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False
    
