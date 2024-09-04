import abc

from task2.impl.file_base import IFile


class INameStrategy(abc.ABC):

    @abc.abstractmethod
    def get_name(self, file: IFile) -> str:
        ...
