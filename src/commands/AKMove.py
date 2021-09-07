from commands.Command import Command
from worldmodel.entityID import EntityID
from commands. standardCommandURN import StandardCommandURN


class AKMove(Command):

    # def __init__(self, agent_id, time, path, destinationX, destinationY) -> None:
    def __init__(self, agent_id, time, path) -> None:
        super().__init__()
        self.urn = StandardCommandURN.AK_MOVE.value

        self.agent_id = agent_id
        self.path = path
        self.x = -1 #destinationX
        self.y = -1 #destinationY
        self.time = time

    def set_fields(self, fields):
        self.agentId = EntityID(fields.get('agent_id'))
        self.time = fields.get('time')
        self.target = fields.get('target_id')

    def get_fields(self):
        fields = {}
        fields['agent_id'] = self.agent_id.get_value()
        fields['time'] = self.time
        fields['x'] = self.x
        fields['y'] = self.y
        fields['path'] = self.path

        return fields
