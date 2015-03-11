# -*- coding: utf-8 -*-
import SocketServer
import json, time

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """


    # Shared by all clientHandlers:
    activeClients = {}
    validChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    msgHistory = []

    def transmit(self, message, sender):
        replyPacket = {"timestamp": time.time(), "sender": sender, "response": "message", "content": message}
        self.connection.send(json.dumps(replyPacket))

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.username = ""
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        print 'Hello ', self.ip, '!\n'
        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            if not received_string:
                continue
            packet = json.loads(received_string)
            if packet["request"] == "login":
                newUsername = packet["content"]
                if newUsername in self.activeClients:
                    replyPacket = {"timestamp": time.time(), "sender": newUsername, "response": "error", "content": "Username already taken!"}
                    self.connection.send(json.dumps(replyPacket))
                else:
                    valid = True
                    for letter in newUsername:
                        if letter not in self.validChars:
                            valid = False
                            break

                    if valid:
                        print "Valid username " + newUsername
                        self.username = newUsername
                        self.activeClients[self.username] = self
                        replyPacket = {"timestamp": time.time(), "sender": newUsername, "response": "history", "content": self.msgHistory}
                        self.connection.send(json.dumps(replyPacket))
                    else:
                        replyPacket = {"timestamp": time.time(), "sender": newUsername, "response": "error", "content": "Invalid username!"}
                        self.connection.send(json.dumps(replyPacket))

            elif packet["request"] == "help":
                print "Sending help message"
                helpMsg = "Some info"
                replyPacket = {"timestamp": time.time(), "sender": "", "response": "info", "content": helpMsg}
                self.connection.send(json.dumps(replyPacket))

            if self.username not in self.activeClients:
                print "Not logged in"
                break

            elif packet["request"] == "logout":
                print "Logging out"
                del self.activeClients[self.username]
                del self

            elif packet["request"] == "msg":
                print "Broadcasting message to active clients: " + packet["content"]
                self.msgHistory.append(self.username + ": " + packet["content"])
                for client in self.activeClients:
                    self.activeClients[client].transmit( packet["content"], self.username )

            elif packet["request"] == "names":
                print "Sending list of active usernames: "
                usernames = []
                for client in self.activeClients:
                    usernames.append(client)
                    print client

                replyPacket = {"timestamp": time.time(), "sender": self.username, "response": "info", "content": usernames}
                self.connection.send(json.dumps(replyPacket))
                


            # TODO: Add handling of received payload from client



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = '', 9996
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
