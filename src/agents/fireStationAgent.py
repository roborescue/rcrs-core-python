from agents.agent import Agent
from log.logger import Logger



class FireStationAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'FireStationAgent'
    
    def post_connect(self, world, agent_id):
        self.Log = Logger(self.get_name(), self.agent_id)

    def get_requested_entities(self):
        return 'entity:firestation'

    def think(self, timestep, change_set, heard):
        #print(f'{self.get_name()}({self.agent_id}): think method. timestep = ', timestep, f'world model size = {len(self.world_model.get_entities())}' )
        pass
