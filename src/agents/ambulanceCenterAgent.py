from agents.agent import Agent


class AmbulanceCenterAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.AmbulanceCenterAgent'

    def get_requested_entities(self):
        return 'entity:ambulancecentre'

    def think(self, timestep, change_set, heard):
        print(f'AmbulanceCenterAgent({self.get_id()}): think method. timestep = ', timestep)
