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
		self.connection_in_use = False
		self.msg_listener_started = False


	def run(self):
	# Initiate the connection to the server
		self.connection.connect((self.host, self.server_port))
		print "Connection received"
		self.connection_in_use = True
		self.msgListener = MessageListener(self, self.connection)
		self.msgListener.start()
		msg_listener_started = True
		time.sleep(0.1)

		while True:
			request_from_user = raw_input("Type request: ")
			if request_from_user == 'login':
				username = raw_input("Enter username: ")
				login_dict = {'request': 'login', 'content': username} 
				json_login = json.dumps(login_dict)
				self.connection.send(json_login)
			elif request_from_user == 'names':
				payload_dict = {'request': 'names', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif request_from_user == 'help':
				payload_dict = {'request': 'help', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif request_from_user == 'logout':
				payload_dict = {'request': 'logout', 'content': None}
				json_payload = json.dumps(payload_dict)
				self.connection.send(json_payload)
				self.msgListener.logged_in = False
				self.connection.close()
				self.connection_in_use = False
			elif request_from_user == 'msg':
				msg_from_user = raw_input("Type message: ")
				payload_dict = {'request': 'msg', 'content': msg_from_user}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			else:
				print 'Invalid input'
			time.sleep(0.5)


if __name__ == '__main__':
	"""
	This is the main method and is executed when you type "python Client.py"
	in your terminal.
	No alterations is necessary
	"""

	client = Client('78.91.66.144', 9998)
	client.run()

