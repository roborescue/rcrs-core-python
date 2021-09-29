from messages.AKAcknowledge import AKAcknowledge
from messages.AKCommand import AKCommand
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from messages.KASense import KASense
from messages.AKConnect import AKConnect
from messages.AKCommand import AKCommand
from messages.Shutdown import Shutdown
from commands.AKSubscribe import AKSubscribe
import queue
from worldmodel.entityID import EntityID
from worldmodel.worldmodel import WorldModel
import random
from log.logger import Logger


class Agent:

    def __init__(self):
        print('agent created .... ')
        #self.connection_send_msg = None
        self.name = ''
        self.connect_request_id = None
        self.world_model = WorldModel()
        self.config = None
        self.random = None
        self.agent_id = None
        self.queue = queue.Queue()

        
    def get_name(self):
        return self.name

    def get_id(self):
        return self.agent_id

    def set_connection_send_func(self, send_func):
        self.send_msg = send_func

    def start_up(self, request_id):
        self.connect_request_id = request_id
        akconnect_msg = AKConnect()
        akconnect_msg.set_agent(self)
        akconnect_msg.prepare_message()
        self.send_msg(akconnect_msg)

    def test_sucsses(self):
        return self.queue.get()

    def message_received(self, msg):
        if isinstance(msg, KASense):
            self.process_sense(msg)
        elif isinstance(msg, KAConnectOK):
            self.handle_connect_ok(msg)
        elif isinstance(msg, KAConnectError):
            self.handle_connect_error(msg)
        
    def handle_connect_error(self, msg):
        Log = Logger(self.get_name())
        Log.warning("failed : " + msg.reason)
        self.queue.put(False)

    def handle_connect_ok(self, msg):
        print('handle_connect_ok(msg): ', msg.request_id, msg.agent_id)
        self.queue.put(True)
        self.agent_id = EntityID(msg.agent_id)
        # entities received from server should be merged to the world model
        world = msg.world

        self.world_model.add_entities(world)

        # configs received from server
        self.config = msg.config

        ack_msg = AKAcknowledge()
        ack_msg.set_agent_id(msg.agent_id)
        ack_msg.set_request_id(msg.request_id)
        ack_msg.prepare_message()
        self.send_msg(ack_msg)

        self.post_connect(world, self.agent_id)
 
    def get_position(self):
        return self.world_model.get_entity(self.get_id()).get_position()

    def process_sense(self, msg):
        self.world_model.merge(msg.get_change_set())
        self.think(msg.get_time(), msg.get_change_set(), msg.get_hearing())

    def random_walk(self):
        # calculate 10 step path
        path = []
        start_pos = EntityID(self.get_position())
        for i in range(50):
            edges = self.world_model.get_entity(start_pos).get_edges()
            neighbors = []
            for edge in edges:
                if edge.get_neighbour() is not None:
                    neighbors.append(edge.get_neighbour())
            next = random.choice(neighbors)
            path.append(next)
            start_pos = EntityID(next)

        return path

    def send_subscribe(self, time, channel):
        akcommand = AKCommand()
        akcommand.add_command(AKSubscribe(self.agent_id(), time, channel))

        self.send_msg(akcommand)

    
