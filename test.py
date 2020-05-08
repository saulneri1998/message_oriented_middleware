from SimpleMediator import SimpleMediator
from Component import Component
from Message import Message

my_mediator = SimpleMediator()
c1 = Component(my_mediator, "XML")
c2 = Component(my_mediator, "JSON")

c1.send_message(c2.my_id, "CSV", "\{\}")

