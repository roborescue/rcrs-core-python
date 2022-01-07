from commands.Command import Command
from worldmodel.entityID import EntityID
from connection import URN
from connection import RCRSProto_pb2


class AKSpeak(Command):

    def __init__(self, agent_id: EntityID, time: int, message: str, channel: int) -> None:
        super().__init__()
        self.urn = URN.Command.AK_SPEAK
        self.agent_id = agent_id
        self.time = time
        self.message = message.encode('utf-8')
        self.channel = channel

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.Message].rawData = self.message
        msg.components[URN.ComponentCommand.Channel].intValue = self.channel
        return msg

