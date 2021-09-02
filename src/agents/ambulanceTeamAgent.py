from agents.agent import Agent


class AmbulanceTeamAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.AmbulanceTeamAgent'

    def get_requested_entities(self):
        return 'entity:ambulanceteam'

    def think(self, timestep, change_set, heard):
        print(f'AmbulanceTeamAgent({self.get_id()}): think method. timestep = ', timestep)
