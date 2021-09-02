from message import AKConnect
from message import AKAcknowledge
from message import KASense
from message import AKCommand
from message import KAConnectOK
from message import KAConnectError
from message import Shutdown


from controlMessageURN import ControlMessageURN

class ControlMessageFactory:
    def __init__(self) -> None:
        pass
    def make_message(urn, data ):
        
        if urn ==  ControlMessageURN.KA_SENSE.value:
            return KASense( data )
        elif urn == ControlMessageURN.KA_CONNECT_OK.value:
            return KAConnectOK( data )
        elif urn ==  ControlMessageURN.KA_CONNECT_ERROR.value:
            return KAConnectError( data )
        elif urn ==  ControlMessageURN.SHUTDOWN.value:
            return Shutdown( data )
        
        return None
        
            