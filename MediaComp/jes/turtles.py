#
# Package: MediaComp
# Module: jes.pictures
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies,
# sounds) from http://mediacomputation.org created by Mark Guzdial and others
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/.

# This module contains JES-compatible wrappers for class and instance methods in MediaComp.pictures

# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
"""
Suggested usage in Jupyter:

from MediaComp.jes.turtles import *
"""

import typing
from .. import turtles


##############################################################################
#
# JES wrapper functions functions for methods of turtles.World
#
##############################################################################


# noinspection PyPep8Naming
def makeWorld(width: int = 640, height: int = 480) -> turtles.World:
    """
    Returns a new world of the specified size, where you can put turtles. Default size is 640x480.

    :param int width: the width for your new world (optional)
    :param int height: he height for your new world (optional)
    :return: the new world
    :rtype: turtles.World

    Example 1::
    def makeDefaultWorld():
        earth = makeWorld()

    This creates a world with the default size (640x480).

    Example 2::
    def makeSmallerWorld():
        mars = makeWorld(500, 500)

    This creates a smaller world of size 500x500.
    """
    width = int(width)
    height = int(height)
    if width <= 0 or height <= 0:
        data_message = f"greater than zero, width={width}, height={height}"
        raise ValueError("width and height must both be " + data_message)
    return turtles.World(width, height)


# noinspection PyPep8Naming
def makeTurtle(world: turtles.World) -> turtles.Turtle:

    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.World.new_tutle` class method.

    :param turtles.World world:
    :return:
    :rtype: turtles.Turtle
    :raises TypeError: if ``world`` is not a :py:class:`~.turtles.World`
    """
    if not isinstance(world, turtles.World):
        raise TypeError(f'makeTurtle(), expected World, got{type(world)}')
    return world.new_turtle()


# noinspection PyPep8Naming
def getTurtleList(world: turtles.World) -> typing.List[turtles.Turtle]:
    """
    Write better docstring

    :param turtles.World world:
    :return:
    :rtype: list[turtles.Turtle]
    :raises TypeError: if ``world`` is not a :py:class:`~.turtles.World`
    """

    if not isinstance(world, turtles.World):
        raise TypeError(f'getTurtleList(), expected World, got{type(world)}')
    return list(world)

##############################################################################
#
# JES wrapper functions functions for methods of turtles.Turtle
#
##############################################################################


def forward(turtle: turtles.Turtle, d: float = 100.0) -> None:
    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.Turtle.forward` method.

    :param turtles.Turtle turtle:
    :param float d:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'forward(), expected Turtle, got{type(turtle)}')
    turtle.forward(d)


def backward(turtle: turtles.Turtle, d: float = 100.0) -> None:
    """
    Write gbetter docstring
    Wrapper for :py:meth:`.turtles.Turtle.backward` method.

    :param turtles.Turtle turtle:
    :param float d:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'backward(), expected Turtle, got{type(turtle)}')
    turtle.forward(-d)


# noinspection PyPep8Naming
def moveTo(turtle: turtles.Turtle, x: float, y: float) -> None:
    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.Turtle.move_to` method.

    :param turtles.Turtle turtle:
    :param int x:
    :param int y:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'moveTo(), expected Turtle, got{type(turtle)}')
    turtle.move_to(x, y)


# noinspection PyPep8Naming
def turnLeft(turtle: turtles.Turtle) -> None:
    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.Turtle.turn` method.

    :param turtles.Turtle turtle:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'turnLeft(), expected Turtle, got{type(turtle)}')
    turtle.turn(90.0)


# noinspection PyPep8Naming
def turnRight(turtle: turtles.Turtle) -> None:
    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.Turtle.turn` method.

    :param turtles.Turtle turtle:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'turnRight(), expected Turtle, got{type(turtle)}')
    turtle.turn(-90.0)


def turn(turtle: turtles.Turtle, degrees: float) -> None:
    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.Turtle.turn` method.

    :param turtles.Turtle turtle:
    :param float degrees:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'turn(), expected Turtle, got{type(turtle)}')
    turtle.turn(degrees)


# noinspection PyPep8Naming
def turnToFace(turtle: turtles.Turtle, x: float, y: float) -> None:
    """
    Write better docstring

    Wrapper for :py:meth:`.turtles.Turtle.turn_to_face` method.

    :param turtles.Turtle turtle:
    :param float x:
    :param float y:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'turnToFace, expected Turtle, got{type(turtle)}')
    turtle.turn_to_face(x, y)


# noinspection PyPep8Naming
def penUp(turtle: turtles.Turtle) -> None:
    """
    Write better docstring

    :param turtles.Turtle turtle:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'penUp(), expected Turtle, got{type(turtle)}')
    turtle.pen_up = True


# noinspection PyPep8Naming
def penDown(turtle: turtles.Turtle) -> None:
    """
    Write better docstring

    :param turtles.Turtle turtle:
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'penDown(), expected Turtle, got{type(turtle)}')
    turtle.pen_up = False


# noinspection PyPep8Naming
def getHeading(turtle: turtles.Turtle) -> float:
    """

    Wrapper for :py:attr:`.turtles.Turtle.heading` property.

    :param turtles.Turtle turtle:
    :return:
    :rtype: float
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'getHeading(), expected Turtle, got{type(turtle)}')
    return turtle.heading


# noinspection PyPep8Naming
def getXPos(turtle: turtles.Turtle) -> float:
    """

    Wrapper for :py:attr:`.turtles.Turtle.x` property.

    :param turtle:
    :return:
    :rtype: float
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'getXPos(), expected Turtle, got{type(turtle)}')
    return turtle.x


# noinspection PyPep8Naming
def getYPos(turtle: turtles.Turtle) -> float:
    """

    Wrapper for :py:attr:`.turtles.Turtle.y` property.

    :param turtle:
    :return:
    :rtype: float
    :raises TypeError: if ``turtle`` is not a :py:class:`~.turtles.Turtle`
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError(f'getYPos(), expected Turtle, got{type(turtle)}')
    return turtle.y
