from email.mime.multipart import MIMEMultipart
import smtplib


def emailIP(emailListFile):


    emailfrom = "navigatorSeniorDesign@gmail.com"
    password = "navigator18"


    emailto = "navigatorSeniorDesign@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = emailfrom
    msg['To'] = emailto
    msg['Subject'] = 'IP HERE'

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(emailfrom, password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()