from task2.impl.file_base import IFile


class File(IFile):

    def __init__(self, name: str):
        self.name = name

    def get_string(self, indent=0):
        return f"{'-' * indent}{self.get_name()}"

    def get_name(self):
        return self.name
