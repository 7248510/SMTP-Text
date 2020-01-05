import smtplib
email = ""
password = ""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(email, password) 
def message1():
    msg = "" #Watch the 160 character sms limit.
    server.sendmail(email, "number@designatedcarrier.com", msg)
message1()


