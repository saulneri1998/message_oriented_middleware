from SimpleMediator import SimpleMediator
from MediatorProxy import MediatorProxy
from Component import Component
from Message import Message

my_mediator = SimpleMediator()
my_mediator_proxy = MediatorProxy([1,3])

try:   
    c1 = Component(my_mediator, "XML")
    c2 = Component(my_mediator, "JSON")
except:
    # nada

c1.send_message(c2.my_id, "CSV", "\{\}")

