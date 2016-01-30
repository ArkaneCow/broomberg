import secret

import sys
import socket

class BClient(object):
    def __init__(self, b_user, b_pass, b_host, b_port):
        self.b_user = b_user
        self.b_pass = b_pass
        self.b_host = b_host
        self.b_port = b_port
        print("init BClient with user: " + self.b_user + " pass: " + self.b_pass + " host: " + self.b_host + " port: " + str(self.b_port))
    @classmethod
    def bclient_default(cls):
        return cls(secret.SECRET_USER, secret.SECRET_PASSWORD, secret.SECRET_HOST, secret.SECRET_PORT)
    def fmt(self, *commands):
        return self.b_user + " " + self.b_pass + "\n" + "\n".join(commands)
    def cmd(self, *commands):
        b_sock = None
        try:
            b_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            b_sock.connect((self.b_host, self.b_port))
        except:
            print("unable to initialize socket")
            print("error:", sys.exc_info()[0])
            return
        data = self.fmt(*commands) + "\nCLOSE_CONNECTION\n"
        c_buff = ""
        try:
            b_sock.sendall(bytes(data, "utf-8"))
        except:
            print("unable to send")
            print("error:", sys.exc_info()[0])
            b_sock.close()
            return
        try:
            sfile = b_sock.makefile()
            rline = sfile.readline()
            while rline:
                c_buff += rline.strip() + "\n"
                rline = sfile.readline()
        except:
            print("unable to receive")
            print("error:", sys.exc_info()[0])
            b_sock.sendall(bytes(self.fmt("") + "\nCLOSE_CONNECTION\n"))
            b_sock.close()
            return
        return [l for l in c_buff.split("\n") if l != ""]

        
