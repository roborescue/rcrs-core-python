from standardCommandURN import StandardCommandURN
from commands import AKRest
from commands import AKMove
from commands import AKLoad
from commands import AKUnload
from commands import AKSay
from commands import AKTell
from commands import AKExtinguish
from commands import AKRescue
from commands import AKSpeak
from commands import AKSubscribe
from commands import AKClearArea
from commands import AKClear



class StandardCommandFactory:
    def __init__(self) -> None:
        pass

    def make_command(urn):
        if urn == StandardCommandURN.AK_REST.value:
            return AKRest()
        elif urn == StandardCommandURN.AK_MOVE.value:
            return AKMove()
        elif urn == StandardCommandURN.AK_LOAD.value:
            return AKLoad()
        elif urn == StandardCommandURN.AK_UNLOAD.value:
            return AKUnload()
        elif urn == StandardCommandURN.AK_SAY.value:
            return AKSay()
        elif urn == StandardCommandURN.AK_TELL.value:
            return AKTell()
        elif urn == StandardCommandURN.AK_EXTINGUISH.value:
            return AKExtinguish()
        elif urn == StandardCommandURN.AK_RESCUE.value:
            return AKRescue()
        elif urn == StandardCommandURN.AK_CLEAR.value:
            return AKClear()
        elif urn == StandardCommandURN.AK_CLEAR_AREA.value:
            return AKClearArea()
        elif urn == StandardCommandURN.AK_SUBSCRIBE.value:
            return AKSubscribe()
        elif urn == StandardCommandURN.AK_SPEAK.value:
            return AKSpeak()

        #Logger.warn( "Unrecognised message urn: " + urn )
        return None
