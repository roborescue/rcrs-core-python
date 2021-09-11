from agents.agent import Agent
from messages.AKCommand import AKCommand
from commands.AKMove import AKMove



class AmbulanceTeamAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.AmbulanceTeamAgent'

    def get_requested_entities(self):
        return 'entity:ambulanceteam'

    def think(self, timestep, change_set, heard):
        #print(f'{self.get_name()}({self.get_id()}): think method. timestep = ', timestep, f'world model size = {len(self.world_model.get_entities())}' )
        path = self.random_walk()
        cmd = AKMove(self.get_id(), timestep, path)

        akcommand = AKCommand()
        akcommand.add_command(cmd)

        self.connection_send_msg(akcommand)
