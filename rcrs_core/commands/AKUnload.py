from rcrs_core.commands.Command import Command
from rcrs_core.worldmodel.entityID import EntityID
from rcrs_core.connection import URN
from rcrs_core.connection import RCRSProto_pb2
from rcrs_core.connection import URN
from rcrs_core.connection import RCRSProto_pb2



class AKUnload(Command):

    def __init__(self, agent_id: EntityID, time: int) -> None:
        super().__init__()
        self.urn = URN.Command.AK_UNLOAD
        self.agent_id = agent_id
        self.time = time

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        return msg