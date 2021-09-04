from messages.message import Message
import messages.ControlMessageProto_pb2 as protoBuf
import random
from messages.controlMessageURN import ControlMessageURN


class AKConnect(Message):

    def __init__(self):
        super().__init__()
        self.urn = ControlMessageURN.AK_CONNECT.value

    def set_agent(self, agent):
        self.agent = agent

    def prepare_message(self):
        self.requestedEntityTypes = self.agent.get_requested_entities()
        self.message = self.write()

    def write(self):
        akConnect = protoBuf.AKConnectProto()
        akConnect.requestID = self.agent.connect_request_id
        akConnect.version = 1
        akConnect.agentName = self.agent.get_name()
        akConnect.requestedEntityTypes.append(self.requestedEntityTypes)
        return akConnect.SerializeToString()

    def read(self, inputStream):
        pass
