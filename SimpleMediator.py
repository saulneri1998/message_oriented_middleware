from Mediator import Mediator
from XMLMessageAdapter import XMLMessageAdapter
from JSONMessageAdapter import JSONMessageAdapter
from CSVMessageAdapter import CSVMessageAdapter

class SimpleMediator(Mediator):

    def __init__(self):
        super().__init__()

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def translate(self, msg, supported_protocol):
        if supported_protocol == "XML":
            return XMLMessageAdapter(msg)
        elif supported_protocol == "JSON":
            return JSONMessageAdapter(msg)
        elif supported_protocol == "CSV":
            return CSVMessageAdapter(msg)

    def notify(self, msg):
        target = None
        for m in self.members:
            if m.my_id == msg.target:
                target = m
                break

        if target.supported_protocol != msg.protocol:
            msg = self.translate(msg, target.supported_protocol)

        target.process_message(msg)
