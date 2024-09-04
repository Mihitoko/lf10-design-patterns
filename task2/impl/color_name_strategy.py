from task2.impl.colors import Colors
from task2.impl.file_base import IFile
from task2.impl.strategy_base import INameStrategy


class NameWithColorStrategy(INameStrategy):

    def __init__(self, color: str = None):
        self.color = color

    def get_name(self, file: IFile) -> str:
        if self.color is None:
            return file.get_name()
        return Colors.color_string(file.get_name(), self.color)
