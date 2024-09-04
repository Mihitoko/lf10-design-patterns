from task2.impl.file_base import IFile
from task2.impl.strategy_base import INameStrategy


class DefaultNameStrategy(INameStrategy):

    def get_name(self, file: IFile) -> str:
        return file.get_name()
