import abc


class StateInterface:
    @abc.abstractmethod
    def handle(self):
        raise NotImplementedError
