from abc import abstractmethod


class StateInterface:
    """State interface to check if function handle exists."""
    @abstractmethod
    def handle(self):
        raise NotImplementedError
