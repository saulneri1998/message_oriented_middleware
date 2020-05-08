class Message:

    def __init__(self, __source, __target, __protocol, __body, __ack):
        try:
            self.source = __source
            self.target = __target
            self.protocol = __protocol
            self.body = __body
            self.ack = __ack
        except Exception as e:
            print(e)

