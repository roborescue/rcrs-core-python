from Command import Command
from commands. standardCommandURN import StandardCommandURN


class AKClearArea(Command):

    def __init__(self, agent_id, time, destinationX, destinationY) -> None:
        super().__init__()
        self.urn = StandardCommandURN.AK_CLEAR_AREA.value
        self.agent_id = agent_id
        self.time = time
        self.x = destinationX
        self.y = destinationY

    def set_fields(self, fields):
        self.agent_id = fields.get('agent_id')
        self.time = fields.get('time')
        self.target = fields.get('target_id')
        self.target = fields.get('x')
        self.target = fields.get('y')

    def get_fields(self):
        fields = {}
        fields['agent_id'] = self.agent_id.get_value()
        fields['time'] = self.time
        fields['x'] = self.x
        fields['y'] = self.y

        return fields
