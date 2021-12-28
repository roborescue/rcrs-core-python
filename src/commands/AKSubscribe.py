from commands.Command import Command
from commands. standardCommandURN import StandardCommandURN


class AKSubscribe(Command):

    def __init__(self, agent_id, time, channels) -> None:
        super().__init__()
        self.urn = StandardCommandURN.AK_SUBSCRIBE.value
        self.agent_id = agent_id
        self.time = time
        self.channels = []

        for ch in channels:
            self.channels.append(ch)

    def set_fields(self, fields):
        self.agent_id = fields.get('agent_id')
        self.time = fields.get('time')
        if isinstance(fields.get('channels'), []):
            for ch in fields.get("channels"):
                self.channels.append(ch)

    def get_fields(self):
        fields = {}
        fields['agent_id'] = self.agent_id.get_value()
        fields['time'] = self.time
        channels = []
        for ch in self.channels:
            channels.append(ch)

        fields['channels'] = channels

        return fields
