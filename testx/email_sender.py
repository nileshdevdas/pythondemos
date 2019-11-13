import smtplib

mail = smtplib.SMTP()
mail.starttls()
mail.login()
mail.sendmail()