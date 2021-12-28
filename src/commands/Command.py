class Command:
    def __init__(self) -> None:
        self.urn = ''
        self.time = 0
        self.agent_id = -1

    def set_urn(self, _urn):
        self.urn = _urn

    def set_time(self, _time):
        self.time = _time

    def set_agent_id(self, _agent_id):
        self.agent_id = _agent_id

    def get_agent_id(self):
        return self.agent_id

    def get_time(self):
        return self.time

    def setFields(self, fields):
        pass

    def getFields():
        pass
