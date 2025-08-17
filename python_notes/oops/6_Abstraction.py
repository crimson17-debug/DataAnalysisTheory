# reduce complexity by hiding unesseary details

class EmailServices:

    def _connect(self):
        print("connecting to the email server")

    def _authenticate(self):
        print("Authenticating....")

    def _disconnect(self):
        print("Disconnecting from the email server...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()





sender = EmailServices()
sender.send_email()


#encapuslation -------- bundling data attribute or methods and it stricts the attributes
#abstraction ============ we can hide the underhood implementation



