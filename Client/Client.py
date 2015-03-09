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


		#MessageReceiver(Thread)
		self.login()
		



	# TODO: Finish init process with necessary code

	def login(self):
		print'Trying to connect'
		self.connection.connect((self.host, self.server_port))
		loged_in = False
		while not loged_in:
			username = raw_input("Enter username: ")
			login_dict = {'request': 'login', 'content': username} #Skal man bruke <> eller '' ? 
			print'Sending json msg'
			json_login = json.dumps(login_dict)
			self.connection.send(json_login)

			json_login_response = self.connection.recv(1024)
			login_response = json.loads(json_login_response)
			if login_response['response'] == 'history':
				loged_in = True
				print 'Successful login'



	def run(self):
	# Initiate the connection to the server
		self.msgListener = MessageListener(self, self.connection)
		time.sleep(1)
		self.msgListener.run()

		while True:
			from_user = raw_input("Type message: ")
			from_user_list = from_user.split()
			if from_user_list[0] == 'names':
				payload_dict = {'request': 'name', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif from_user_list[0] == 'help':
				payload_dict = {'request': 'help', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif from_user_list[0] == 'logout':
				payload_dict = {'request': 'logout', 'content': None}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			elif from_user_list[0] == 'msg':
				payload_dict = {'request': 'msg', 'content': from_user_list[1:(length(from_user_list)-1)]}
				json_payload= json.dumps(payload_dict)
				self.connection.send(json_payload)
			else:
				print 'invalid input'




	
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

	client = Client('129.241.187.108', 9996)
	client.run()

