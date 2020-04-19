# Python package initialization
"""
Package docstring goes here

This package has multiple modules:
jes
pictures
colors
files
sounds
turtles
"""

# Note: a Python package consists of multiple modules each in their own .py file
# __all__ is the list of modules to import if one does "from package import *

__all__ = ["colors", "pictures", "sounds", "turtles"]

from .. import colors
from .. import sounds


# noinspection PyPep8Naming
def getColorWrapAround() -> bool:  # pylint: disable=invalid-name
    """ Not Implemented
    :rtype bool:
     """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("getColorWrapAround()" + not_implemented)


# noinspection PyPep8Naming
def setColorWrapAround(flag: bool) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param bool flag:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("setColorWrapAround()" + not_implemented)


# noinspection PyPep8Naming
def pickAFile() -> str:  # pylint: disable=invalid-name
    """ Not Implemented
    :rtype str:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("pickAFile()" + not_implemented)


# TODO: wrap ipywidgets.ColorPicker
# noinspection PyPep8Naming
def pickAColor() -> colors.Color:  # pylint: disable=invalid-name
    """ Not Implemented
    :rtype colors.Color:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("pickAColor()" + not_implemented)


# noinspection PyPep8Naming
def blockingPlay(sound: sounds.Sound) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param sounds.Sound sound:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("blockingPlay(sound)" + not_implemented)


# noinspection PyPep8Naming
def stopPlaying(sound: sounds.Sound) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param sounds.Sound sound:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("stopPlaying(sound)" + not_implemented)


# noinspection PyPep8Naming
def makeMovie():  # pylint: disable=invalid-name
    """ Not Implemented """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("makeMovie()" + not_implemented)


# noinspection PyPep8Naming
def makeMovieFromInitialFile(filename: str):  # pylint: disable=invalid-name
    """ Not Implemented
    :param str filename:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("makeMovieFromInitialFile()" + not_implemented)


# noinspection PyPep8Naming
def addFrameToMovie(frame, movie) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param frame:
    :param movie:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("addFrameToMove()" + not_implemented)


# noinspection PyPep8Naming
def writeFramesToDirectory(movie, directory) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param movie:
    :param directory:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("writeFramesToDirectory()" + not_implemented)


# noinspection PyPep8Naming
def playMovie(movie) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param movie:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("playMovie()" + not_implemented)


# noinspection PyPep8Naming
def writeAVI(movie, path: str, framesPerSecond: float = 16.0) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param movie:
    :param str path:
    :param float framesPerSecond:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("writeAVI()" + not_implemented)


# noinspection PyPep8Naming
def writeQuicktime(movie, path: str, framesPerSecond: float = 16.0) -> None:  # pylint: disable=invalid-name
    """ Not Implemented
    :param movie:
    :param str path:
    :param float framesPerSecond:
    """
    not_implemented = " is not implemented in the MediaComp.jes module"
    raise NotImplementedError("writeQuicktime()" + not_implemented)
