import getpass
import smtplib
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender=input("Enter sender email id ")
reciever=input("Enter reciever email id ")
msg=input("Enter message to be sent ")
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,reciever,msg)
print("Message sent successfully")
s.quit()