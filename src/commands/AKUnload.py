from Command import Command
from worldmodel.entityID import EntityID
from commands. standardCommandURN import StandardCommandURN


class AKUnload(Command):

    def __init__(self, agent_id, time) -> None:
        super().__init__()
        self.urn = StandardCommandURN.AK_UNLOAD.value
        self.agent_id = agent_id
        self.time = time

    def set_fields(self, fields):
        self.agent_id = EntityID(fields.get('agent_id'))
        self.time = fields.get('time')

    def get_fields(self):
        fields = {}
        fields['agent_id'] = self.agent_id.get_value()
        fields['time'] = self.time

        return fields
