from Message import Message

class XMLMessageAdapter(Message):

    def __init__(self, __msg):
        self.source = __msg.source
        self.target = __msg.target
        self.protocol = "XML"
        self.body = __msg.body
