#
# Package: MediaComp
# Module: files
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies, sounds) from
# http://mediacomputation.org created by Mark Guzdial and Barbara Ericson
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/).
#
"""
Module docstring goes here
"""

# module typing is standard in Python 3.5+: https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton code: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type, doesn't mean
# that at runtime it will actually be of that type: dynamic checking or
# casting/conversion still needs to be done
import typing

import pathlib

__PATH: pathlib.Path = pathlib.Path.cwd()  # pylint: invalid-name

# TODO: use an ipyfilechooser (https://pypi.org/project/ipyfilechooser/)
# to implement something compatible with usage pattern of JES pickAFile()


def media_path(filename: typing.Optional[str]) -> pathlib.Path:
    """
    Translates relative filenames into absolute paths

    :param filename: a string representing a relative filename
    :return: absolute path ending in specified filename
    """
    if filename is None:
        return __PATH
    return __PATH.joinpath(filename)


def set_media_path(filename: typing.Optional[str] = None) -> bool:
    """
    Sets the name of the directory where media file will be read from.

    :param filename: name of directory to use as base for opening media files
    :return: True if path change was successful, false if unsuccessful
    """
    global __PATH  # pylint: disable=global-statement
    if filename is None:
        __PATH = pathlib.Path.cwd()
        return True
    file_path = pathlib.Path(filename)
    if file_path.is_absolute():
        if file_path.is_dir():
            __PATH = file_path
            return True
        return False
    # file_path must be relative
    new_path = __PATH.joinpath(file_path)
    if new_path.is_dir():
        __PATH = new_path
        return True
    return False
