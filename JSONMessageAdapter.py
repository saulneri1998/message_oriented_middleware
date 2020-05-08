from Message import Message

class JSONMessageAdapter(Message):

    def __init__(self, __msg):
        try:
            self.source = __msg.source
            self.target = __msg.target
            self.protocol = "JSON"
            self.body = __msg.body
        except Exception as e:
            print(e)
