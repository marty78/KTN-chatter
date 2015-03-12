# -*- coding: utf-8 -*-
import json, socket, time
from threading import Thread

class MessageListener(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """
    # self.logged_in = True

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        self.logged_in = True
        Thread.__init__(self)
        self.client = client
        self.connection = connection
        self.logout = False

        super(MessageListener, self).__init__()
        # Flag to run thread as a deamon
        self.daemon = True


        # TODO: Finish initialization of MessageReceiver

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while self.logged_in:
            json_msg = self.connection.recv(1024)
            if not json_msg:
                continue
            # print json_msg
            msg = json.loads(json_msg)

            if msg['response'] == 'error': 
                print msg['content']

            if msg['response'] == 'logout':
                print 'Logging out'

            if msg['response'] == 'history':
                print "History:"
                print msg['content']

            if msg['response'] == 'info':
                print msg['content']

            if msg['response'] == 'message':
                print msg['content']

            print "\n"
        pass
