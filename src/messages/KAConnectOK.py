from messages.message import Message
from config.config import Config
from entities.standardEntityFactory import StandardEntityFactory
from connection import URN


class KAConnectOK(Message):

    def __init__(self, data):
        self.urn = URN.ControlMSG.KA_CONNECT_OK
        self.data = data
        self.config = Config()
        self.world = []
        self.read()

    def read(self):

        entities = self.data.components[URN.ComponentControlMSG.Entities].entityList.entities
        self.request_id = self.data.components[URN.ComponentControlMSG.RequestID].intValue
        self.agent_id = self.data.components[URN.ComponentControlMSG.AgentID].entityID
        config = self.data.components[URN.ComponentControlMSG.AgentConfig].config

        for e in entities:
            entity = StandardEntityFactory.make_entity(URN.MAP[e.urn], e.entityID)
            properties = {}
            for property in e.properties:
                value = getattr(property, property.WhichOneof('value')) if property.defined else None
                properties[URN.MAP[property.urn]] = value
            entity.set_entity(properties)
            self.world.append(entity)

        for key, value in config.data.items():
            self.config.set_value(key, value)

