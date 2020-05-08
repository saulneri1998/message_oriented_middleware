from Mediator import Mediator
from SimpleMediator import SimpleMediator

class MediatorProxy(Mediator):

    def __init__(self, __allowed_ids):
        try:
            super().__init__()
            self.allowed_ids = __allowed_ids
            self.mediator = SimpleMediator()
        except Exception as e:
            print(e)

    def add_member(self, member):
        try:
            if member.my_id in self.allowed_ids:
                self.mediator.add_member(member)
            else:
                raise Exception("Authentication failed!!!")
        except Exception as e:
            print(e)

    def remove_member(self, member):
        try:
            self.mediator.remove_member(member)
        except Exception as e:
            print(e)

    def notify(self, msg):
        try:
            self.mediator.notify(msg)
        except Exception as e:
            print(e)    

