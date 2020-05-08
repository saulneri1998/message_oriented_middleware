class Message:

    def __init__(self, __source, __target, __protocol, __body):
        try:
            self.source = __source
            self.target = __target
            self.protocol = __protocol
            self.body = __body
        except Exception as e:
            print(e)

