from abc import abstractmethod


class ControllerInterface:
    @abstractmethod
    def add_routes(self, app):
        raise NotImplementedError
