import abc


class IFile(abc.ABC):

    @abc.abstractmethod
    def print(self, indent=0):
        ...
