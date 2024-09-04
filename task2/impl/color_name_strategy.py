from task2.impl.file_base import IFile
from task2.impl.strategy_base import INameStrategy

RED = "\033[0;31m"
GREEN = "\033[1;32m"
NC = '\033[0m'
LIGHT_BLACK = '\033[0;90m'


class NameWithColorStrategy(INameStrategy):

    def __init__(self, color: str = None):
        self.color = color

    def get_name(self, file: IFile) -> str:
        if self.color is None:
            return file.get_name()
        return f"{self.color}{file.get_name()}{NC}"
