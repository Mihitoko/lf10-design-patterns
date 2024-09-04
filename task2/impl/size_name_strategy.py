from task2.impl.file_base import IFile
from task2.impl.strategy_base import INameStrategy
class NameWithSizeStrategy(INameStrategy):
    def get_name(self, file: IFile) -> str:
        return f"{file.get_name()} <{file.get_size()}>"
