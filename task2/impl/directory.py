from task2.impl.default_name_strategy import DefaultNameStrategy
from task2.impl.file_base import IFile


class Directory(IFile):

    def __init__(self, name, files=None, name_strategy=None):
        super().__init__()

        self.name_strategy = name_strategy
        if self.name_strategy is None:
            self.name_strategy = DefaultNameStrategy()

        if files is None:
            files = []

        self.name = name
        self.files: list[IFile] = files

    def get_string(self, indent=0):
        ret = [f"{'-' * indent}{self.name_strategy.get_name(self)}"]
        for file in self.files:
            ret.append(file.get_string(indent + 1))

        return "\n".join(ret)

    def get_name(self):
        return self.name

    def get_size(self) -> int:
        s = 0
        for file in self.files:
            s += file.get_size()
        return s
