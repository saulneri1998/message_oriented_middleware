from SimpleMediator import SimpleMediator
from MediatorProxy import MediatorProxy
from Component import Component
from Message import Message

my_mediator = SimpleMediator()
allowed = [0, 1]
my_mediator_proxy = MediatorProxy(allowed)

c1 = Component(my_mediator_proxy, "XML")
c2 = Component(my_mediator_proxy, "JSON")
c1.send_message(c2.my_id, "CSV", "\{\}", True)
# c1.send_message(c2.my_id, "CSV", "\{\}")



c1.checkLogger()

