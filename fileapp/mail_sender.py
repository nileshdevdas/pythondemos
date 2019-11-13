import smtplib

HOST = "mail.vinsys.com"
PORT = 587
SENDER_MAIL = "iot@vinsys.com"
SENDER_PASSWORD = "1QAZxsw@"


def send_confirmation(records, to_mail):
    mail = smtplib.SMTP(host="mail.vinsys.com", port=587)
    mail.starttls()
    print(mail.login(SENDER_MAIL, SENDER_PASSWORD))
    message = "Subject:{} \n\n{}".format(
        "Total File Processing " + '3232323', "File Processing Was")
    print(mail.sendmail('iot@vinsys.com',
                        'apoorva.paranjape.ext@siemens.com', message))
    print(mail.sendmail('iot@vinsys.com',
                        'nilesh.devdas@vinsys.com', message))


send_confirmation('10993993', 'xxx')
