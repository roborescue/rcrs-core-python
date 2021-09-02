from commands.Command import Command
from worldmodel.entityID import EntityID


class AKClear(Command):

    def __init__(self) -> None:
        super().__init__()
        
        self.target = ''

    def setFields(self, fields):
        self.agentId = EntityID(fields.get('agent_id'))
        self.time = fields.get('time')
        self.target = fields.get('target_id')