from connection import URN
from messages.message import Message
from connection import RCRSProto_pb2

class AKAcknowledge(Message):

    def __init__(self):
        super().__init__()
        self.urn = URN.ControlMSG.AK_ACKNOWLEDGE
        self.request_id = None
        self.agent_id = None

        self.message = None

    def prepare_message(self, request_id, agent_id):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = URN.ControlMSG.AK_ACKNOWLEDGE
        msg.components[URN.ComponentControlMSG.RequestID].intValue = request_id
        msg.components[URN.ComponentControlMSG.AgentID].entityID = agent_id
        return msg
       