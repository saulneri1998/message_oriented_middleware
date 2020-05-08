from Mediator import Mediator
from XMLMessageAdapter import XMLMessageAdapter
from JSONMessageAdapter import JSONMessageAdapter
from CSVMessageAdapter import CSVMessageAdapter
from Logger import Logger

class SimpleMediator(Mediator):

    def __init__(self):
        try:
            super().__init__()
            self.logger = Logger.Instance()
        except Exception as e:
            print(e)

    def add_member(self, member):
        try:
            self.members.append(member)
        except Exception as e:
            print(e)

    def remove_member(self, member):
        try:
            self.members.remove(member)
        except Exception as e:
            print(e)

    def translate(self, msg, supported_protocol):
        try:
            if supported_protocol == "XML":
                return XMLMessageAdapter(msg)
            elif supported_protocol == "JSON":
                return JSONMessageAdapter(msg)
            elif supported_protocol == "CSV":
                return CSVMessageAdapter(msg)
        except Exception as e:
            print(e)

    def notify(self, msg):
        try:
            target = None
            for m in self.members:
                if m.my_id == msg.target:
                    target = m
                    break

            if target.supported_protocol != msg.protocol:
                msg = self.translate(msg, target.supported_protocol)

            target.process_message(msg)
            self.logger.addLog("{} sent message to {}".format(msg.source, msg.target))

        except Exception as e:
            print(e)
