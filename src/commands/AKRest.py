from commands.Command import Command
from worldmodel.entityID import EntityID
from connection import RCRSProto_pb2
from connection import URN


class AKRest(Command):

    def __init__(self, agent_id: EntityID, time: int) -> None:
        super().__init__()
        self.urn = URN.Command.AK_REST
        self.agent_id = agent_id
        self.time = time

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        return msg

