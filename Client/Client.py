# -*- coding: utf-8 -*-
import socket
import json
import time
from MessageReceiver import MessageListener


class Client:
	"""
	This is the chat client class
	"""

	def __init__(self, host, server_port):
		"""
		This method is run when creating a new Client object
		"""
		self.host = host
		self.server_port = server_port
		# Set up the socket connection to the server
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.loged_in = False

		#MessageReceiver(Thread)
		#self.login()
		



	# TODO: Finish init process with necessary code

	def login(self):
		self.connection.connect((self.host, self.server_port))
		print "Connection received"
		loged_in = False
		while not loged_in:
			username = raw_input("Enter username: ")
			login_dict = {'request': 'login', 'content': username} 
			json_login = json.dumps(login_dict)
			self.connection.send(json_login)

			json_login_response = self.connection.recv(1024)
			login_response = json.loads(json_login_response)
			if login_response['response'] == 'history':
				loged_in = True
				print "Successful login"
				print login_response['content']
		self.msgListener = MessageListener(self, self.connection)
		self.msgListener.start()
		time.sleep(0.1)



	def run(self):
	# Initiate the connection to the server

		while True:
			request_from_user = raw_input("Type request: ")
			# from_user_list = from_user.split()
			loggedIn = False
			if request_from_user == 'names' and loggedIn:
				payload_dict = {'request': 'names', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif request_from_user == 'help':
				print "Inne i help"
				payload_dict = {'request': 'help', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif request_from_user == 'logout' and loggedIn:
				payload_dict = {'request': 'logout', 'content': None}
				json_payload = json.dumps(payload_dict)
				self.connection.send(json_payload)
				self.msgListener.logged_in = False
				self.connection.close()
			elif request_from_user == 'msg':
				msg_from_user = raw_input("Type message: ")
				payload_dict = {'request': 'msg', 'content': msg_from_user}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif request_from_user == 'login':
				self.login()
				loggedIn = True
			else:
				print 'invalid input'
			time.sleep(0.5)




	
	# def disconnect(self):
	# # TODO: Handle disconnection
	# loged_in = False
	# pass

	# def receive_message(self, message):
	# # TODO: Handle incoming message
	# pass

	# def send_payload(self, data):
	# # TODO: Handle sending of a payload
	# pass


if __name__ == '__main__':
	"""
	This is the main method and is executed when you type "python Client.py"
	in your terminal.
	No alterations is necessary
	"""

	client = Client('78.91.71.70', 9981)
	client.run()

