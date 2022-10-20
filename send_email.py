from email.mime.text import MIMEText
import smtplib

# Sends user a summary of the information they provided 
def send_email(email, height, average_height, count):
    from_email = "********@gmail.com"
    from_password = "***********"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. The average height of all entries is <strong>%s</strong>, which is calculated from the total amount of entries: <strong>%s</strong>" % (height, average_height, count)

    msg = MIMEText(message, 'html') 
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)