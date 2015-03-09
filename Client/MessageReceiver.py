# -*- coding: utf-8 -*-
from threading import Thread

class MessageListener(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        self.client = client
        self.connection = connection
        self.logout = False

        # Flag to run thread as a deamon
        self.daemon = True

        # TODO: Finish initialization of MessageReceiver

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            json_msg = self.connection.recv(1024)
            if not json_msg:
                continue
            msg = json.loads(json_msg)

            if login_response['response'] == 'error': 
                print 'Something went wrong'

            if login_response['response'] == 'logout':
                print 'Loging out'

            if login_response['response'] == 'history':
                print msg['content']

            if login_response['response'] == 'info':
                print msg['content']
            if login_response['response'] == 'message':
                print msg['content']


        pass
