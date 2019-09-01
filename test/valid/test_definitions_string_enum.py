#!/usr/bin/env/python

import enum


class ABcd(enum.Enum):

    A = "A"
    B = "B"
    C = "C"

    def as_dict(self):
        return self.value

    def __repr__(self):
        return "<Enum ABcd. {}: {}>".format(self.name, self.value)


class RootObject:
    def __init__(self):
        pass

    def as_dict(self):
        d = dict()
        return d

    def __repr__(self):
        return "<Class RootObject. >".format()
