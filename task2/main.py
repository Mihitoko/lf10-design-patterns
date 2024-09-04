"""
Task:
1. Implement the strategy patter for Directory (see File class)
2. Create a strategy that colors file names
3. Create a strategy that adds the size next to the file/dir name, i.e. the output should look sth like this:

A <25>
-a.txt <1>
-B <8>
--C <8>
---c.txt <8>
-D <16>
--d.txt <16>
"""
from task2.impl.directory import Directory
from task2.impl.file import File
from task2.impl.size_name_strategy import NameWithSizeStrategy


def main():
    c = File('c.txt', name_strategy=NameWithSizeStrategy())
    cdir = Directory('C', [c], name_strategy=NameWithSizeStrategy())
    bdir = Directory('B', [cdir], name_strategy=NameWithSizeStrategy())
    d = File('d.txt', name_strategy=NameWithSizeStrategy())
    ddir = Directory('D', [d], name_strategy=NameWithSizeStrategy())
    a = File('a.txt', name_strategy=NameWithSizeStrategy())
    adir = Directory('A', [a, bdir, ddir], name_strategy=NameWithSizeStrategy())

    print(adir.get_string())


if __name__ == '__main__':
    main()
