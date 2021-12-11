from messages.message import Message
from connection import RCRSProto_pb2
from connection import URN
from messages.controlMessageURN import ControlMessageURN

class AKConnect(Message):

    def __init__(self):
        super().__init__()
        self.urn = ControlMessageURN.AK_CONNECT.value
    
    def prepare_message(self, request_id, agent):

        msg = RCRSProto_pb2.MessageProto()
        msg.urn = URN.ControlMSG.AK_CONNECT
        msg.components[URN.ComponentControlMSG.RequestID].intValue = request_id
        msg.components[URN.ComponentControlMSG.Version].intValue = 2
        msg.components[URN.ComponentControlMSG.Name].stringValue = agent.name
        for urn in agent.get_requested_entities():
            msg.components[URN.ComponentControlMSG.RequestedEntityTypes].intList.values.append(urn)

        return msg