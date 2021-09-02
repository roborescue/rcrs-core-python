from agents.agent import Agent


class PoliceForceAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.PoliceForceAgent'

    def get_requested_entities(self):
        return 'entity:policeforce'

    def think(self, timestep, change_set, heard):
        print(
            f'PoliceForceAgent({self.get_id()}): think method. timestep = ', timestep)
