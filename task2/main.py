"""
Task:
Implement the Directory class and print out the following folder structure with correct tabulation:

A
-a.txt
-B
--C
---c.txt
-D
--d.txt
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
