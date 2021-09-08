from messages.message import Message
import messages.ControlMessageProto_pb2 as protoBuf
from messages.controlMessageURN import ControlMessageURN
from config.config import Config
from entities.standardEntityFactory import StandardEntityFactory
from properties.standardPropertyURN import StandardPropertyURN
from entities.standardEntityURN import StandardEntityURN


class KAConnectOK(Message):

    def __init__(self, data):
        self.urn = ControlMessageURN.KA_CONNECT_OK.value
        self.data = bytes(data)
        self.config = Config()
        self.world = []
        self.read()

    def read(self):
        kaConnectok = protoBuf.KAConnectOKProto()
        kaConnectok.ParseFromString(self.data)
        self.request_id = kaConnectok.requestID
        self.agent_id = kaConnectok.agentID
        print(kaConnectok)
        for entity_proto in kaConnectok.entities:

            _urn = StandardEntityURN.from_id(entity_proto.urnID)
            entity = StandardEntityFactory.make_entity(
                _urn, entity_proto.entityID)
            properties = {}
            for property_proto in entity_proto.properties:
                properties[StandardPropertyURN.from_id(
                    property_proto.urnID)] = property_proto.fields

            entity.set_entity(properties)
            self.world.append(entity)

        for key, value in kaConnectok.config.data.items():
            self.config.set_value(key, value)

    def write(self):
        pass
