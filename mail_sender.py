from smtplib import *
message = input()
conn = SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('mail','password')
conn.sendmail('from-mail','to-mail','Subject: OTP \n\n '+message)
conn.quit()
