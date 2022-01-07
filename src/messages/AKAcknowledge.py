from connection import URN
from messages.message import Message
from connection import RCRSProto_pb2

class AKAcknowledge(Message):

    def __init__(self):
        super().__init__(URN.ControlMSG.AK_ACKNOWLEDGE)

    def write(self, request_id, agent_id):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.get_urn()
        msg.components[URN.ComponentControlMSG.RequestID].intValue = request_id
        msg.components[URN.ComponentControlMSG.AgentID].entityID = agent_id.get_value()
        return msg
    
    def read(self):
        pass

    