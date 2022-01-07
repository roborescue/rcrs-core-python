from commands.Command import Command
from worldmodel.entityID import EntityID
from connection import URN
from connection import RCRSProto_pb2

class AKClear(Command):
    def __init__(self, agent_id: EntityID, time: int, target: EntityID) -> None:
        super().__init__()
        self.urn = URN.Command.AK_CLEAR
        self.agent_id = agent_id
        self.time = time
        self.target = target

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.Target].entityID = self.target.get_value()
        return msg

    
