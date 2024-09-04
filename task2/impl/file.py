import os
import random

from task2.impl.default_name_strategy import DefaultNameStrategy
from task2.impl.file_base import IFile
from task2.impl.strategy_base import INameStrategy


class File(IFile):

    def __init__(self, name: str, name_strategy: INameStrategy = None):
        self.name = name
        self.size = random.randrange(1, 20)
        self.name_strategy = name_strategy
        if self.name_strategy is None:
            self.name_strategy = DefaultNameStrategy()

    def get_string(self, indent=0):
        return f"{'-' * indent}{self.name_strategy.get_name(self)}"

    def get_name(self):
        return self.name

    def get_size(self) -> int:
        return self.size
