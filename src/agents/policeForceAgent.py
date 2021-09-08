from agents.agent import Agent
from commands.AKMove import AKMove
from messages.AKCommand import AKCommand
from worldmodel.entityID import EntityID
from commands.AKClear import AKClear


class PoliceForceAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.PoliceForceAgent'

    def get_requested_entities(self):
        return 'entity:policeforce'

    def think(self, timestep, change_set, heard):
        print(f'{self.get_name()}({self.get_id()}): think method. timestep = ', timestep)
        # if timestep > 1:
        #     return
        path = self.random_walk()
        cmd = AKMove(self.get_id(), timestep, path)

        
        #target = self.world_model.get_entity(self.get_id()).get_position()

        cmd2 = AKClear(self.get_id(), timestep, EntityID(2100749334))

        akcommand = AKCommand()
        #akcommand.add_command(cmd2)
        akcommand.add_command(cmd)

        self.connection_send_msg(akcommand)
