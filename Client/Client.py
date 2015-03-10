# -*- coding: utf-8 -*-
import socket
import json


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

        self.run()



    # TODO: Finish init process with necessary code

    def login(self, connection):
        username = 'ola'
        login_dict = {'request': 'login', 'content': username} #Skal man bruke <> eller '' ? 
        json_login = json.dumps(login_dict)

        self.connection.send(json_login)


    def run(self):
    # Initiate the connection to the server
        print'Trying to connect'
        self.connection.connect((self.host, self.server_port))

        username = 'Kjetil3'
        login_dict = {'request': 'login', 'content': username} #Skal man bruke <> eller '' ? 
        print'Sending json msg'
        json_login = json.dumps(login_dict)
        self.connection.send(json_login)

        #json_login_response = self.connection.recv(1024)
        #login_response = json.loads(json_login_response)
        while True:
            continue



    # def disconnect(self):
    # # TODO: Handle disconnection
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
    #client.run()






