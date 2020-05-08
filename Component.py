from Message import Message

class Component:
    id = 0
    message_template = """
MESSAGE RECEIVED IN {}:
    FROM: {}
    PROTOCOL: {}
    BODY: {}
"""

    def __init__(self, __mediator, __supported_protocol):
        try:   
            self.mediator = __mediator
            self.my_id = Component.id
            Component.id += 1
            self.supported_protocol = __supported_protocol
            self.mediator.add_member(self)
        except Exception as e:
            print(e)
        

    def send_message(self, target, protocol, body):
        try:
            msg = Message(self.my_id, target, protocol, body)
            self.mediator.notify(msg)
        except Exception as e:
            print(e)

    def process_message(self, msg):
        try:
            print(Component.message_template.format(
                    self.my_id, 
                    msg.source, 
                    msg.protocol, 
                    msg.body
                )
            )
        except Exception as e:
            print(e)
    
    