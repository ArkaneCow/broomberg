import secret

import sys
import socket

class BClient(object):
    def __init__(self, b_user, b_pass, b_host, b_port):
        self.b_user = b_user
        self.b_pass = b_pass
        self.b_host = b_host
        self.b_port = b_port
        print("init BClient with user: " + self.b_user + " pass: " + self.b_pass + " host: " + self.b_host + " port: " + self.b_port)
        init()
    @classmethod
    def bclient_default(cls):
        return cls(secret.SECRET_USER, secret.SECRET_PASSWORD, secret.SECRET_HOST, secret.SECRET_PORT)
    def init():
        print("initializing")
        try:
            self.b_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.b_sock.connect((self.b_host, self.b_port))
        except:
            print("unable to initialize socket")
    def start():
        print("starting BClient")

    def stop():
        print("stopping BClient")
