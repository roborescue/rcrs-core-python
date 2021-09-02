from messages.message import Message
from messages.controlMessageURN import ControlMessageURN


class KAConnectError(Message):

    def __init__(self, data):
        Message.__init__(self)
        self.urn = ControlMessageURN.KA_CONNECT_ERROR.value
        self.data = data

    def read(self):
        pass

    def write(self):
        pass
