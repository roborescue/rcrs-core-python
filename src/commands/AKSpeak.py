from commands.Command import Command
from worldmodel.entityID import EntityID
from commands. standardCommandURN import StandardCommandURN


class AKSpeak(Command):

    def __init__(self, agent_id, time, data, channel) -> None:
        super().__init__()
        self.urn = StandardCommandURN.AK_SPEAK.value
        self.agent_id = agent_id
        self.data = data
        self.time = time
        self.channel = channel

    def set_fields(self, fields):
        self.agent_id = EntityID(fields.get('agent_id'))
        self.time = fields.get('time')
        self.data = fields.get('data')
        self.channel = fields.get('channel')

    def get_fields(self):
        fields = {}
        fields['agent_id'] = self.agent_id.get_value()
        fields['time'] = self.time
        fields['data'] = self.data
        fields['channel'] = self.channel

        return fields
