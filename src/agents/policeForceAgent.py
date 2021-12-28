from agents.agent import Agent
from commands.AKMove import AKMove
from messages.AKCommand import AKCommand
from commands.AKClear import AKClear
from constants import kernel_constants
from log.logger import Logger
from connection import URN

class PoliceForceAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'PoliceForceAgent'
        self.Log = Logger('PoliceForceAgent', '')

    def post_connect(self, world, agent_id):
        self.Log = Logger(self.get_name(), self.agent_id)

    def get_requested_entities(self):
        return [URN.Entity.POLICE_FORCE]

    def think(self, time, change_set, heard):
        print(f'{self.get_name()}({self.agent_id}): think method. timestep = ', time)
        self.Log.info(time)

        if time == self.config.get_value(kernel_constants.IGNORE_AGENT_COMMANDS_KEY):
            # Subscribe to channel 1
            self.send_subscribe(time, 1)
        
        path = self.random_walk()
        cmd = AKMove(self.agent_id, time, path)

        # #target = self.world_model.get_entity(self.agent_id).get_position()

        # cmd2 = AKClear(self.agent_id, time, 2100749334)

        # akcommand = AKCommand()
        # # akcommand.add_command(cmd2)
        # akcommand.add_command(cmd)

        # self.send_msg(akcommand)
