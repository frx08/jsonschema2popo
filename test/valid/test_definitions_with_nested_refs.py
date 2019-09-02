#!/usr/bin/env/python


class ABcd:
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
            if not isinstance(value, ABcd._Child1._Child2):
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
        if not isinstance(value, ABcd._Child1):
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
        return "<Class ABcd. Child1: {}>".format(self.__Child1)


class Ref:

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
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__ListVal
            ]
        return d

    def __repr__(self):
        return "<Class Ref. IntVal: {}, ListVal: {}>".format(
            self.__IntVal, self.__ListVal
        )


class AAAA:

    _types_map = {
        "X": {"type": int, "subtype": None},
        "YRef": {"type": ABcd._Child1._Child2, "subtype": None},
    }
    _formats_map = {}

    def __init__(self, X=None, YRef=None):
        pass
        self.__X = X
        self.__YRef = YRef

    def _get_X(self):
        return self.__X

    def _set_X(self, value):
        if not isinstance(value, int):
            raise TypeError("X must be int")

        self.__X = value

    X = property(_get_X, _set_X)

    def _get_YRef(self):
        return self.__YRef

    def _set_YRef(self, value):
        if not isinstance(value, ABcd._Child1._Child2):
            raise TypeError("YRef must be ABcd._Child1._Child2")

        self.__YRef = value

    YRef = property(_get_YRef, _set_YRef)

    def as_dict(self):
        d = dict()
        if self.__X is not None:
            d["X"] = self.__X.as_dict() if hasattr(self.__X, "as_dict") else self.__X
        if self.__YRef is not None:
            d["YRef"] = (
                self.__YRef.as_dict()
                if hasattr(self.__YRef, "as_dict")
                else self.__YRef
            )
        return d

    def __repr__(self):
        return "<Class AAAA. X: {}, YRef: {}>".format(self.__X, self.__YRef)


class RootObject:
    def __init__(self):
        pass

    def as_dict(self):
        d = dict()
        return d

    def __repr__(self):
        return "<Class RootObject. >".format()
