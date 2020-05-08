from Mediator import Mediator
from SimpleMediator import SimpleMediator

class MediatorProxy(Mediator):

    def __init__(self, __allowed_ids):
        super().__init__()
        self.allowed_ids = __allowed_ids
        self.mediator = SimpleMediator()

    def add_member(self, member):
        if member.my_id in self.allowed_ids:
            self.mediator.add_member(member)
        else:
            raise Exception("Authentication failed!!!")

    def remove_member(self, member):
        self.mediator.remove_member(member)

    def notify(self, msg):
        self.mediator.notify(msg)

