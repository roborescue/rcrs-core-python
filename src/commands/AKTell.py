from commands.Command import Command
from connection import URN
from connection import RCRSProto_pb2


class AKTell(Command):

    def __init__(self, agent_id: int, time: int, message: str) -> None:
        super().__init__()
        self.urn = URN.Command.AK_TELL
        self.agent_id = agent_id
        self.message = message.encode('utf-8')
        self.time = time

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.Message].rawData = self.message
        return msg
