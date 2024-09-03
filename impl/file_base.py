import abc


class IFile(abc.ABC):

    @abc.abstractmethod
    def print_name(self):
        ...
