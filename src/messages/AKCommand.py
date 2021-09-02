from messages.message import Message
from messages.controlMessageURN import ControlMessageURN


class AKCommand(Message):
    def __init__(self):
        Message.__init__(self)
        self.urn = ControlMessageURN.AK_COMMAND.value

    def read(self):
        pass

    def write(self):
        pass
