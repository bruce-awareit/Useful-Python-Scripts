import smtplib
from email.mime.text import MIMEText


sender_email = "your_email@example.com"
recipient_email = "recipient_email@example.com"

subject = "Automated Email"
message = "This is an automated email sent using Python."

# SMTP server configuration (example: Gmail)

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"


msg = MIMEText(message)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email
try:

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
       server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")
    
except Exception as e:
    print("Error sending email:", str(e))
    
finally:

    server.quit()

