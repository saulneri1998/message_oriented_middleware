from Message import Message

class XMLMessageAdapter(Message):

    def __init__(self, __msg):
        try:
            self.source = __msg.source
            self.target = __msg.target
            self.protocol = "XML"
            self.body = __msg.body
            self.ack = __msg.ack
        except Exception as e:
            print(e)
