import abc


class IFile(abc.ABC):

    @abc.abstractmethod
    def get_string(self, indent=0):
        ...

    @abc.abstractmethod
    def get_name(self):
        ...
