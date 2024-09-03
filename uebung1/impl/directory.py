from uebung1.impl.file_base import IFile


class Directory(IFile):
    def __init__(self, name, files=None):
        super().__init__()

        if files is None:
            files = []

        self.name = name
        self.files: list[IFile] = files

    def print(self, indent=0):
        print(f"{'-' * indent}{self.name}")
        for file in self.files:
            file.print(indent + 1)
