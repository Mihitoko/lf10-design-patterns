"""
Task:
1. Implement the strategy patter for Directory (see File class)
2. Create a strategy that colors file names (filenames and dir name should have different colors)
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


def main():
    c = File('c.txt')
    cdir = Directory('C', [c])
    bdir = Directory('B', [cdir])
    d = File('d.txt')
    ddir = Directory('D', [d])
    a = File('a.txt')
    adir = Directory('A', [a, bdir, ddir])

    print(adir.get_string())


if __name__ == '__main__':
    main()
