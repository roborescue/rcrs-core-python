from connection.connection import Connection


class ComponentLauncher:
    def __init__(self, port, host) -> None:
        self.request_id = 0
        self.port = port
        self.host = host

    def make_connection(self) -> Connection:
        return Connection(self.host, self.port)

    def connect(self, agent):
        connection = self.make_connection()
        connection.set_message_received_func(agent.message_received)
        connection.connect()
        agent.set_connection_send_func(connection.send_msg)
        agent.start_up(self.generate_request_ID())
        return agent.test_sucsses()

    def generate_request_ID(self):
        self.request_id += 1
        return self.request_id
