from Message import Message

class Component:
    id = 0

    def __init__(self, __mediator, __supported_protocol):
        self.mediator = __mediator
        self.my_id = Component.id
        Component.id += 1
        self.supported_protocol = __supported_protocol
        self.mediator.add_member(self)

    def send_message(self, target, protocol, body):
        msg = Message(self.my_id, target, protocol, body)
        self.mediator.notify(msg)

    def process_message(self, msg):
        print("""
MESSAGE RECEIVED IN {}:
    FROM: {}
    PROTOCOL: {}
    BODY: {}
""".format(self.my_id, msg.source, msg.protocol, msg.body))
    
    