#!/usr/bin/env python

from __future__ import absolute_import

import os
import sys

if __package__ == "":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from jsonschema2popo.jsonschema2popo import main as _main  # noqa

if __name__ == "__main__":
    sys.exit(_main())
