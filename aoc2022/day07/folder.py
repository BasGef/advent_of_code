from __future__ import annotations
import weakref

from file import File


class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = {}
        self.parent = None

    @property
    def size(self):
        return sum(f.size for f in self.contents.values())

    def append(self, obj: File | Folder):
        if isinstance(obj, Folder):
            obj.parent = weakref.ref(self)()  # ensure garbage collection works
        self[obj.name] = obj

    def __contains__(self, item):
        return item in self.contents

    def __setitem__(self, key, value):
        self.contents[key] = value

    def __getitem__(self, item):
        return self.contents[item]

    def __delitem__(self, key):
        del self.contents[key]

    def __iter__(self):
        return iter(self.contents.values())
