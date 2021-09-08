from agents.agent import Agent


class PoliceOfficeAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.PoliceOfficeAgent'

    def get_requested_entities(self):
        return 'entity:policeoffice'

    def think(self, timestep, change_set, heard):
        #print(f'{self.get_name()}({self.get_id()}): think method. timestep = ', timestep, f'world model size = {len(self.world_model.get_entities())}' )
        pass
