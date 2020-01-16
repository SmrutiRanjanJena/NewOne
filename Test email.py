import smtplib


class email:

    def __init__(self, receiverEmail="smrutiranjan_jena@bmc.com", receiverName="Smruti Ranjan"):
        self.sub = "Status Update Notification: Test email"
        self.senderEmail = "smrutiranjan_jena@bmc.com"
        self.receiverEmail = receiverEmail
        self.receiverName = receiverName

    def send(self, body):
        message = (f"From: <" + self.senderEmail + ">"
                   f"\nTo: <" + self.receiverEmail + ">"
                   f"\nSubject:" + self.sub +
                   f"\nDear " + self.receiverName + "," +
                   f"\n\n" + body)
        try:
            smtpObj = smtplib.SMTP('phx-relayprd-01.adprod.bmc.com')
            smtpObj.sendmail(self.senderEmail, self.receiverEmail, message)
            print("Successfully sent email...")
        except smtplib.SMTPException:
            print("Error: unable to send email.")

Email = email()
Email.send("Body builder")
