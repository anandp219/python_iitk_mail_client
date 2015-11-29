#!/usr/bin/python
import smtplib
from Tkinter import *
from threading import Thread
from time import sleep
import tkMessageBox

def threaded_function(msg):
	if msg == 1:
		msg = "Mail has been Sent"
	else:
		msg = "Mail has not been Sent"
	print msg
	tkMessageBox.showinfo("Notice",msg)

	# for i in range(100):
	# 	print msg
	# 	sleep(1)

class SampleApp(Tk):
	def __init__(self):
		Tk.__init__(self)
        # self.entry = Entry(self)
        # self.button = Button(self, text="Get", command=self.on_button)
        # self.button.pack()
        # self.entry.pack()
		self.resizable(width=FALSE, height=FALSE)
		self.geometry('{}x{}'.format(500, 550))
		self.title("Python IITK mail client")
		self.user = Entry(self)
		self.user.pack(padx=5, pady=5)
		self.password = Entry(self, show="*")
		self.password.pack(padx=5, pady=5)
		self.send = Entry(self)
		self.send.pack(padx=5, pady=5)
		self.text = Text(self,wrap= WORD)
		self.text.pack(padx=20, pady=20)
		self.blackbutton = Button(self, text="Send", fg="black",command = self.send_mail)
		self.blackbutton.pack( side = BOTTOM)
		self.var = StringVar()
		self.label = Message( self, textvariable=self.var, relief=RAISED )

    # def on_button(self):
    #     print(self.entry.get())

	def send_mail(self):
		msg = self.text.get("1.0", "end-1c")
		username = self.user.get()
		password = self.password.get()
		recv = self.send.get()
		try:
			server = smtplib.SMTP('smtp.cc.iitk.ac.in',25) #port 465 or 587
			server.login(username,password)
			send = username+"@iitk.ac.in"
			server.sendmail(send,recv,msg)
			server.close()
			# self.Message("Mail has been sent")
			thread = Thread(target = threaded_function, args = (1,))
			thread.start()
		except:
			msg = "Mail has not been Sent"
			thread = Thread(target = threaded_function, args = (2,))
			thread.start()
	

app = SampleApp()
app.mainloop() 