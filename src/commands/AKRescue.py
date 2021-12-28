from commands.Command import Command
from commands. standardCommandURN import StandardCommandURN

class AKRescue(Command):

    def __init__(self, agent_id, time, target) -> None:
        super().__init__()
        self.urn = StandardCommandURN.AK_RESCUE.value
        self.agent_id = agent_id
        self.target = target
        self.time = time

    def set_fields(self, fields):
        self.agent_id = fields.get('agent_id')
        self.time = fields.get('time')
        self.target = fields.get('target_id')

    def get_fields(self):
        fields = {}
        fields['agent_id'] = self.agent_id.get_value()
        fields['time'] = self.time
        fields['target_id'] = self.target.get_value()

        return fields
