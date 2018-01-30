from abc import abstractmethod
import time

class AbstractWorker:
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
