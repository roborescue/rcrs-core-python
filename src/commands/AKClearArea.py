from commands.Command import Command
from connection import URN
from connection import RCRSProto_pb2

class AKClearArea(Command):

    def __init__(self, agent_id: int, time: int, destinationX: int, destinationY: int) -> None:
        super().__init__()
        self.urn = URN.Command.AK_CLEAR_AREA
        self.agent_id = agent_id
        self.time = time
        self.x = destinationX
        self.y = destinationY

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.DestinationX].intValue = self.x
        msg.components[URN.ComponentCommand.DestinationY].intValue = self.y
        return msg

