from impl.file_base import IFile


class File(IFile):
    def __init__(self, name: str):
        self.name = name

    def print_name(self):
        print(self.name)
