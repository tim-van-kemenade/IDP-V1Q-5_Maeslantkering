from abc import abstractmethod
import time


class AbstractWorker:
    """Worker interface used to see if handle and get_timeout are present in the workers and run them in the main.py as
    thread.
    """
    def run(self):
        while True:
            self.handle()
            time.sleep(self.get_timeout())

    @abstractmethod
    def handle(self):
        raise NotImplementedError

    @abstractmethod
    def get_timeout(self) -> int:
        raise NotImplementedError
