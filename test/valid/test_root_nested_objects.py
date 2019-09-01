#!/usr/bin/env/python


class Abcd:
    class _Child1:
        class _Child2:

            _types_map = {
                "IntVal": {"type": int, "subtype": None},
                "ListVal": {"type": list, "subtype": str},
            }
            _formats_map = {}

            def __init__(self, IntVal=None, ListVal=None):
                pass
                self.__IntVal = IntVal
                self.__ListVal = ListVal

            def _get_IntVal(self):
                return self.__IntVal

            def _set_IntVal(self, value):
                if not isinstance(value, int):
                    raise TypeError("IntVal must be int")

                self.__IntVal = value

            IntVal = property(_get_IntVal, _set_IntVal)

            def _get_ListVal(self):
                return self.__ListVal

            def _set_ListVal(self, value):
                if not isinstance(value, list):
                    raise TypeError("ListVal must be list")
                if not all(isinstance(i, str) for i in value):
                    raise TypeError("ListVal list values must be str")

                self.__ListVal = value

            ListVal = property(_get_ListVal, _set_ListVal)

            def as_dict(self):
                d = dict()
                if self.__IntVal is not None:
                    d["IntVal"] = (
                        self.__IntVal.as_dict()
                        if hasattr(self.__IntVal, "as_dict")
                        else self.__IntVal
                    )
                if self.__ListVal is not None:
                    d["ListVal"] = [
                        p.as_dict() if hasattr(p, "as_dict") else p
                        for p in self.__ListVal
                    ]
                return d

            def __repr__(self):
                return "<Class _Child2. IntVal: {}, ListVal: {}>".format(
                    self.__IntVal, self.__ListVal
                )

        _types_map = {
            "IntVal": {"type": int, "subtype": None},
            "Child2": {"type": _Child2, "subtype": None},
        }
        _formats_map = {}

        def __init__(self, IntVal=None, Child2=None):
            pass
            self.__IntVal = IntVal
            self.__Child2 = Child2

        def _get_IntVal(self):
            return self.__IntVal

        def _set_IntVal(self, value):
            if not isinstance(value, int):
                raise TypeError("IntVal must be int")

            self.__IntVal = value

        IntVal = property(_get_IntVal, _set_IntVal)

        def _get_Child2(self):
            return self.__Child2

        def _set_Child2(self, value):
            if not isinstance(value, Abcd._Child1._Child2):
                raise TypeError("Child2 must be _Child2")

            self.__Child2 = value

        Child2 = property(_get_Child2, _set_Child2)

        def as_dict(self):
            d = dict()
            if self.__IntVal is not None:
                d["IntVal"] = (
                    self.__IntVal.as_dict()
                    if hasattr(self.__IntVal, "as_dict")
                    else self.__IntVal
                )
            if self.__Child2 is not None:
                d["Child2"] = (
                    self.__Child2.as_dict()
                    if hasattr(self.__Child2, "as_dict")
                    else self.__Child2
                )
            return d

        def __repr__(self):
            return "<Class _Child1. IntVal: {}, Child2: {}>".format(
                self.__IntVal, self.__Child2
            )

    _types_map = {"Child1": {"type": _Child1, "subtype": None}}
    _formats_map = {}

    def __init__(self, Child1=None):
        pass
        self.__Child1 = Child1

    def _get_Child1(self):
        return self.__Child1

    def _set_Child1(self, value):
        if not isinstance(value, Abcd._Child1):
            raise TypeError("Child1 must be _Child1")

        self.__Child1 = value

    Child1 = property(_get_Child1, _set_Child1)

    def as_dict(self):
        d = dict()
        if self.__Child1 is not None:
            d["Child1"] = (
                self.__Child1.as_dict()
                if hasattr(self.__Child1, "as_dict")
                else self.__Child1
            )
        return d

    def __repr__(self):
        return "<Class Abcd. Child1: {}>".format(self.__Child1)
