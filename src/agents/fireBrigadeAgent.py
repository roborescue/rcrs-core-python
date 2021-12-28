from agents.agent import Agent
from messages.AKCommand import AKCommand
from commands.AKMove import AKMove
from log.logger import Logger


class FireBrigadeAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'FireBrigadeAgent'
    
    def post_connect(self, world, agent_id):
        self.Log = Logger(self.get_name(), self.agent_id)

    def get_requested_entities(self):
        return 'entity:firebrigade'

    def think(self, timestep, change_set, heard):
        # print(f'{self.get_name()}({self.agent_id}): think method. timestep = ', timestep, f'world model size = {len(self.world_model.get_entities())}' )
        path = self.random_walk()
        cmd = AKMove(self.agent_id, timestep, path)
        
        akcommand = AKCommand()
        akcommand.add_command(cmd)

        self.send_msg(akcommand)

