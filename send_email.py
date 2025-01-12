import smtplib
import ssl
import certifi

host = "smtp.gmail.com"  #specific for gmail
port = 465


username = 'govolzgo@gmail.com'
password = 'efeqwnmcvesqnmjn'

receiver = 'govolzgo@gmail.com'
#context = ssl.create_default_context()
#context = ssl._create_unverified_context()
#context = ssl.create_default_context(cafile=certifi.where())
#context = ssl.create_default_context(cafile="proxy-ca.pem")
context = ssl.create_default_context(cafile="cacert.pem")

#addin the '\' and the 'Subject:' attributes will populate the subject field in your email
message = """\
Subject: Hi!
How are you?
Bye!
"""

try:
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("Email sent successfully!")
except ssl.SSLCertVerificationError as e:
    print("SSL verification failed:", e)
except Exception as e:
    print("An error occurred:", e)
