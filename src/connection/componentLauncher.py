from connection.connection import Connection


class ComponentLauncher:
    def __init__(self, port, host) -> None:
        self.request_id = 0
        self.port = port
        self.host = host

    def make_connection(self) -> Connection:
        return Connection(self.host, self.port)

    def connect(self, agent, _request_id):
        connection = self.make_connection()
        connection.connect()
        connection.message_received(agent.message_received)
        agent.set_send_msg(connection.send_msg)
        agent.start_up(_request_id)
        #return agent.test_sucsses()
        connection.parseMessageFromKernel()

    def generate_request_ID(self):
        self.request_id += 1
        return self.request_id
