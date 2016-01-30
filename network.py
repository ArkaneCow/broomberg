
class BClient(object):
    def __init__(self, b_user, b_pass):
        self.b_user = b_user
        self.b_pass = b_pass
    @classmethod
    def bclient_default(cls):
        
