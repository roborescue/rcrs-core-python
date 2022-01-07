from worldmodel.entityID import EntityID
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self) -> None:
        pass
   
    @abstractmethod
    def prepare_cmd():
        pass
