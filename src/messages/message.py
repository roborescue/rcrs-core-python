
from commands.Command import Command
from properties.standardPropertyFactory import StandardPropertyFactory
from worldmodel.changeSet import ChangeSet
from entities.standardEntityFactory import StandardEntityFactory
from config.config import Config
import messages.ControlMessageProto_pb2 as protoBuf
import random
from entities.standardEntityURN import StandardEntityURN
from properties.standardPropertyURN import StandardPropertyURN
from messages.controlMessageURN import ControlMessageURN
from worldmodel.entityID import EntityID


class Message:

    def __init__(self) -> None:
        self.urn = ''
        pass

    def read(self):
        pass

    def write(self):
        pass

    def get_urn(self):
        return self.urn


class AKConnect(Message):

    def __init__(self):
        super().__init__()
        self.urn = ControlMessageURN.AK_CONNECT.value

    def set_agent(self, agent):
        self.agent = agent
        self.agent_name = agent.get_name()

    def prepare_message(self):
        self.request_id = random.randint(1, 100)
        self.requestedEntityTypes = self.agent.get_requested_entities()
        self.message = self.write()

    def write(self):
        akConnect = protoBuf.AKConnectProto()
        akConnect.requestID = self.request_id
        akConnect.version = 1
        akConnect.agentName = self.agent_name
        akConnect.requestedEntityTypes.append(self.requestedEntityTypes)
        return akConnect.SerializeToString()

    def read(self, inputStream):
        pass


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


class KAConnectError(Message):

    def __init__(self, data):
        Message.__init__(self)
        self.urn = ControlMessageURN.KA_CONNECT_ERROR.value
        self.data = data

    def read(self):
        pass

    def write(self):
        pass


class KASense(Message):

    def __init__(self, _data):
        super().__init__()
        self.urn = ControlMessageURN.KA_SENSE.value
        self.agent_id = None
        self.time = None
        self.updates = None
        self.data = _data
        self.change_set = ChangeSet()
        self.hear = []
        self.read()

    def get_time(self):
        return self.time

    def get_change_set(self):
        return self.change_set

    def get_hearing(self):
        return self.hear

    def read(self):
        kaSenseProto = protoBuf.KASenseProto()
        kaSenseProto.ParseFromString(self.data)

        self.agent_id = kaSenseProto.agentID
        self.time = kaSenseProto.time

        changes_map = kaSenseProto.changes.changes
        entities_urns = kaSenseProto.changes.entitiesURNs
        for entity_id_proto in changes_map.keys():
            entity_id = EntityID(entity_id_proto)
            urn = entities_urns.get(entity_id_proto)

            property_map_proto = changes_map.get(entity_id_proto)
            for property_urn in property_map_proto.property.keys():
                property = StandardPropertyFactory.make_property(property_urn)
                if property is not None:
                    fields = property_map_proto.property.get(property_urn)
                    property.set_fields(fields)

                    self.change_set.add_change(entity_id, urn, property)

        for _entity_id in kaSenseProto.changes.deletes:
            self.change_set.entity_deleted(EntityID(_entity_id))

        for command_proto in kaSenseProto.hears:
            _urn = command_proto.urn
            _fields = command_proto.fields

            print(_urn, _fields)

            command = Command()
            command.set_urn(_urn)

    def write(self):
        pass


class AKCommand(Message):
    def __init__(self):
        Message.__init__(self)
        self.urn = ControlMessageURN.AK_COMMAND.value

    def read(self):
        pass

    def write(self):
        pass


class Shutdown(Message):
    def __init__(self, data) -> None:
        super().__init__()
        self.urn = ControlMessageURN.SHUTDOWN.value

    def read(self):
        pass

    def write(self):
        pass
