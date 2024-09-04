from task1.impl.file_base import IFile


class File(IFile):
    def __init__(self, name: str):
        self.name = name

    def print(self, indent=0):
        print(f"{'-' * indent}{self.name}")
