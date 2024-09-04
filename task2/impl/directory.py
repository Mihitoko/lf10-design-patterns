from task2.impl.default_name_strategy import DefaultNameStrategy
from task2.impl.file_base import IFile


class Directory(IFile):

    def __init__(self, name, files=None):
        super().__init__()
        if files is None:
            files = []

        self.name = name
        self.files: list[IFile] = files

    def get_string(self, indent=0):
        ret = [f"{'-' * indent}{self.get_name()}"]
        for file in self.files:
            ret.append(file.get_string(indent + 1))

        return "\n".join(ret)

    def get_name(self):
        return self.name
