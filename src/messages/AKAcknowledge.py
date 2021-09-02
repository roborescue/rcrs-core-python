from messages.message import Message
import messages.ControlMessageProto_pb2 as protoBuf
from messages.controlMessageURN import ControlMessageURN


class AKAcknowledge(Message):

    def __init__(self):
        super().__init__()
        self.urn = ControlMessageURN.AK_ACKNOWLEDGE.value
        self.request_id = None
        self.agent_id = None

        self.message = None

    def set_request_id(self, id):
        self.request_id = id

    def set_agent_id(self, id):
        self.agent_id = id

    def prepare_message(self):
        self.message = self.write()

    def write(self):
        akAck = protoBuf.AKAcknowledgeProto()
        akAck.requestID = self.request_id
        akAck.agentID = self.agent_id
        return akAck.SerializeToString()
