from abc import ABC, abstractmethod
from enum import Enum

from lib.task_queue import BlockingTaskSingleton


class CommittedOffset(Enum):
    CURRENT = 0

class StateManager(ABC):

    def __init__(self, pattern_detector, broker_q):
        self.pattern_detector = pattern_detector
        self.pattern_detector.register_state_manager(self)
        self.broker_q: BlockingTaskSingleton = broker_q

    @abstractmethod
    def add_state(self, state, ts=None):
        pass

    def get_latest_committed_offset(self):
        return CommittedOffset.CURRENT

    def get_current_lag(self):
        return 0