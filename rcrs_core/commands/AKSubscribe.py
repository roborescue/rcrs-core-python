from rcrs_core.commands.Command import Command
from rcrs_core.worldmodel.entityID import EntityID
from rcrs_core.connection import RCRSProto_pb2
from rcrs_core.connection import URN
from typing import List


class AKSubscribe(Command):

    def __init__(self, agent_id: EntityID, time: int, channels: List[int]) -> None:
        super().__init__()
        self.urn = URN.Command.AK_SUBSCRIBE
        self.agent_id = agent_id
        self.time = time
        self.channels = []

        for ch in channels:
            self.channels.append(ch)

    def prepare_cmd(self):
        msg = RCRSProto_pb2.MessageProto()
        msg.urn = self.urn
        msg.components[URN.ComponentControlMSG.AgentID].entityID = self.agent_id.get_value()
        msg.components[URN.ComponentControlMSG.Time].intValue = self.time
        msg.components[URN.ComponentCommand.Channels].intList.values.extend(self.channels)
        return msg
    
