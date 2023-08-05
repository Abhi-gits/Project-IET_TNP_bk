from django import get_version

VERSION = (1, 0, 0, "final", 0)

__version__ = get_version(VERSION)


"""The only down side of using the get_version directly from the Django module is that it won’t be able to resolve the git hash for alpha versions."""