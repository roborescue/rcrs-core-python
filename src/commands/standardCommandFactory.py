from commands.standardCommandURN import StandardCommandURN
from commands.AKRest import AKRest
from commands.AKMove import AKMove
from commands.AKLoad import AKLoad
from commands.AKUnload import AKUnload
from commands.AKSay import AKSay
from commands.AKTell import AKTell
from commands.AKExtinguish import AKExtinguish
from commands.AKRescue import AKRescue
from commands.AKSpeak import AKSpeak
from commands.AKSubscribe import AKSubscribe
from commands.AKClearArea import AKClearArea
from commands.AKClear import AKClear


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
