from rcrs_core.commands.Command import Command
from rcrs_core.connection import RCRSProto_pb2
from rcrs_core.properties.standardPropertyFactory import StandardPropertyFactory
from rcrs_core.worldmodel.changeSet import ChangeSet
from rcrs_core.worldmodel.entityID import EntityID
from rcrs_core.messages.message import Message
from rcrs_core.connection import URN


class KASense(Message):

    def __init__(self, data: RCRSProto_pb2):
        super().__init__(URN.ControlMSG.KA_SENSE)
        self.agent_id = None
        self.time = None
        self.updates = None
        self.data = data
        self.change_set = ChangeSet()
        self.hear = []
        self.read()

    def read(self):
        self.agent_id = self.data.components[URN.ComponentControlMSG.AgentID].entityID
        self.time = self.data.components[URN.ComponentControlMSG.Time].intValue
        changes = self.data.components[URN.ComponentControlMSG.Updates].changeSet
        self.hear = self.data.components[URN.ComponentControlMSG.Hearing].commandList
        for change in changes.changes:
            entity_id = EntityID(change.entityID)
            for p in change.properties:
                property_urn = URN.MAP[p.urn]
                _property = StandardPropertyFactory.make_property(property_urn)
                value = getattr(p, p.WhichOneof('value')) if p.defined else None
                if _property is not None and value is not None:
                    _property.set_fields(value)
                    self.change_set.add_change(entity_id, change.urn, _property)
        for entity_id in changes.deletes:
            self.change_set.entity_deleted(EntityID(entity_id))

    def write(self):
        pass
