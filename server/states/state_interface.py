from abc import abstractmethod


class StateInterface:
    @abstractmethod
    def handle(self):
        raise NotImplementedError
