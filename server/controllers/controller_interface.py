from abc import abstractmethod


class ControllerInterface:
    """Interface for controllers."""
    @abstractmethod
    def add_routes(self, app):
        raise NotImplementedError
