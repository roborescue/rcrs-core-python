from messages.KASense import KASense
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from messages.Shutdown import Shutdown
from messages.controlMessageURN import ControlMessageURN


class ControlMessageFactory:
    def __init__(self) -> None:
        pass

    def make_message(self, urn, data):

        if urn == ControlMessageURN.KA_SENSE.value:
            return KASense(data)
        elif urn == ControlMessageURN.KA_CONNECT_OK.value:
            return KAConnectOK(data)
        elif urn == ControlMessageURN.KA_CONNECT_ERROR.value:
            return KAConnectError(data)
        elif urn == ControlMessageURN.SHUTDOWN.value:
            return Shutdown(data)

        return None
