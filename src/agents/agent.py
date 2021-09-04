import threading
from connection.connection import Connection
from messages.AKAcknowledge import AKAcknowledge
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from messages.KASense import KASense
from messages.AKConnect import AKConnect
import queue


class Agent:

    def __init__(self):
        print('agent created .... ')
        self.connection_send_msg = None
        self.name = ''
        self.connect_request_id = None
        self.world_model = None
        self.config = None
        self.random = None
        self.agent_id = None
        self.queue = queue.Queue()

    def get_name(self):
        return self.name

    def get_id(self):
        return self.agent_id

    def set_connection_send_func(self, send_func):
        self.connection_send_msg = send_func

    def start_up(self, request_id):
        self.connect_request_id = request_id
        akconnect_msg = AKConnect()
        akconnect_msg.set_agent(self)
        akconnect_msg.prepare_message()
        self.connection_send_msg(akconnect_msg)

    def test_sucsses(self):
        return self.queue.get()

    def message_received(self, msg):
        if isinstance(msg, KAConnectOK):
            self.handle_connect_ok(msg)
        elif isinstance(msg, KAConnectError):
            self.handle_connect_error(msg)
        elif isinstance(msg, KASense):
            self.process_sense(msg)

    def handle_connect_error(self, msg):
        print(self.get_name(),  "KAConnectError : ", msg.reason)
        self.queue.put(False)

    def handle_connect_ok(self, msg):
        print('handle_connect_ok(msg): ', msg.request_id, msg.agent_id)
        self.agent_id = msg.agent_id
        # entities received from server should be merged to the world model
        world = msg.world

        # configs received from server
        config = msg.config

        ack_msg = AKAcknowledge()
        ack_msg.set_agent_id(msg.agent_id)
        ack_msg.set_request_id(msg.request_id)
        ack_msg.prepare_message()
        self.connection_send_msg(ack_msg)
        
        self.queue.put(True)

    def process_sense(self, msg):
        self.think(msg.get_time(), msg.get_change_set(), msg.get_hearing())
