from messages.message import Message
from messages.controlMessageURN import ControlMessageURN
import messages.ControlMessageProto_pb2 as protoBuf


class KAConnectError(Message):

    def __init__(self, data):
        Message.__init__(self)
        self.urn = ControlMessageURN.KA_CONNECT_ERROR.value
        self.data = data
        self.read()

    def read(self):
        err = protoBuf.KAConnectErrorProto()
        err.ParseFromString(self.data)
        self.request_id = err.requestID
        self.reason = err.reason

    def write(self):
        pass
