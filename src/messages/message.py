from abc import ABC, abstractmethod


class Message(ABC):

    def __init__(self, _urn) -> None:
        self.urn = _urn

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    def get_urn(self):
        return self.urn
