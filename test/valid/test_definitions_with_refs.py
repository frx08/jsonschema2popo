#!/usr/bin/env/python


class ABcd:

    _types_map = {
        "Child1": {"type": int, "subtype": None},
        "Child2": {"type": str, "subtype": None},
    }
    _formats_map = {}

    def __init__(self, Child1=None, Child2=None):
        pass
        self.__Child1 = Child1
        self.__Child2 = Child2

    def _get_Child1(self):
        return self.__Child1

    def _set_Child1(self, value):
        if not isinstance(value, int):
            raise TypeError("Child1 must be int")

        self.__Child1 = value

    Child1 = property(_get_Child1, _set_Child1)

    def _get_Child2(self):
        return self.__Child2

    def _set_Child2(self, value):
        if not isinstance(value, str):
            raise TypeError("Child2 must be str")

        self.__Child2 = value

    Child2 = property(_get_Child2, _set_Child2)

    def as_dict(self):
        d = dict()
        if self.__Child1 is not None:
            d["Child1"] = (
                self.__Child1.as_dict()
                if hasattr(self.__Child1, "as_dict")
                else self.__Child1
            )
        if self.__Child2 is not None:
            d["Child2"] = (
                self.__Child2.as_dict()
                if hasattr(self.__Child2, "as_dict")
                else self.__Child2
            )
        return d

    def __repr__(self):
        return "<Class ABcd. Child1: {}, Child2: {}>".format(
            self.__Child1, self.__Child2
        )


class SubRef:

    _types_map = {"ChildA": {"type": ABcd, "subtype": None}}
    _formats_map = {}

    def __init__(self, ChildA=None):
        pass
        self.__ChildA = ChildA

    def _get_ChildA(self):
        return self.__ChildA

    def _set_ChildA(self, value):
        if not isinstance(value, ABcd):
            raise TypeError("ChildA must be ABcd")

        self.__ChildA = value

    ChildA = property(_get_ChildA, _set_ChildA)

    def as_dict(self):
        d = dict()
        if self.__ChildA is not None:
            d["ChildA"] = (
                self.__ChildA.as_dict()
                if hasattr(self.__ChildA, "as_dict")
                else self.__ChildA
            )
        return d

    def __repr__(self):
        return "<Class SubRef. ChildA: {}>".format(self.__ChildA)


class DirectRef:

    _types_map = {
        "Child1": {"type": int, "subtype": None},
        "Child2": {"type": str, "subtype": None},
    }
    _formats_map = {}

    def __init__(self, Child1=None, Child2=None):
        pass
        self.__Child1 = Child1
        self.__Child2 = Child2

    def _get_Child1(self):
        return self.__Child1

    def _set_Child1(self, value):
        if not isinstance(value, int):
            raise TypeError("Child1 must be int")

        self.__Child1 = value

    Child1 = property(_get_Child1, _set_Child1)

    def _get_Child2(self):
        return self.__Child2

    def _set_Child2(self, value):
        if not isinstance(value, str):
            raise TypeError("Child2 must be str")

        self.__Child2 = value

    Child2 = property(_get_Child2, _set_Child2)

    def as_dict(self):
        d = dict()
        if self.__Child1 is not None:
            d["Child1"] = (
                self.__Child1.as_dict()
                if hasattr(self.__Child1, "as_dict")
                else self.__Child1
            )
        if self.__Child2 is not None:
            d["Child2"] = (
                self.__Child2.as_dict()
                if hasattr(self.__Child2, "as_dict")
                else self.__Child2
            )
        return d

    def __repr__(self):
        return "<Class DirectRef. Child1: {}, Child2: {}>".format(
            self.__Child1, self.__Child2
        )


class RootObject:
    def __init__(self):
        pass

    def as_dict(self):
        d = dict()
        return d

    def __repr__(self):
        return "<Class RootObject. >".format()
