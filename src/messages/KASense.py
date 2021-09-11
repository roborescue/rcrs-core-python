from commands.Command import Command
from properties.standardPropertyFactory import StandardPropertyFactory
from worldmodel.changeSet import ChangeSet
import messages.ControlMessageProto_pb2 as protoBuf
from messages.controlMessageURN import ControlMessageURN
from worldmodel.entityID import EntityID
from messages.message import Message


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

            #print(_urn, _fields)

            command = Command()
            command.set_urn(_urn)

    def write(self):
        pass
