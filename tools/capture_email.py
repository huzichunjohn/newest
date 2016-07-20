from smtpd import *
import asyncore

class SMTPDaemon(SMTPServer):
    def __init__(self, localaddr, remoteaddr):
	SMTPServer.__init__(self, localaddr, remoteaddr)

    def process_message(self, peer, mailfrom, rcpttos, data):
	print ""
	print "===== " + "New Email Received" + " ====="
	print data
	print ""

    @staticmethod
    def run(port):
	daemon = SMTPDaemon(("127.0.0.1", port), (None, None))
	try:
	    asyncore.loop(timeout=2)
	except KeyboardInterrupt:
	    daemon.close()

if __name__ == "__main__":
    SMTPDaemon.run(25)
