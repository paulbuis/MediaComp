#
# Package: MediaComp
# Module: turtles
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures,
# movies, sounds) from http://mediacomputation.org created by
# Mark Guzdial and others licensed under the
# Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/.
#
"""
.. module:: turtles
   :synopsis: class Turtle and class World to implement JES work-a-like

.. moduleauthor:: Paul Buis <00pebuis@bsu.edu>
"""
# module math is standard in Python 3:
#   https://docs.python.org/3/library/math.html
# used for sqrt, sin, cos, atan2, radians, degrees, ...
import math

import collections.abc

# module typing is standard in Python 3.5+:
#           https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations:
#           https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton
#           ode: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type,
# doesn't mean that at runtime it will actually be of that type: dynamic
# checking or casting/conversion still needs to be done
import typing

from . import pictures


def type_error_message(fun_name: str, param_name: str, expected: str,
                       actual: typing.Any) -> str:
    """ generates error messages for raising TypeErrors """
    return f"In MediaComp.turtles.{fun_name}: {param_name} expected a " +\
           f"{expected}, actually {type(actual)}"


class Turtle:
    """
    Use ``addTurtle`` method from class ``World`` to create
    new ``Turtle`` instances
    """
    def __init__(self, world: 'World', x_start: float = 0.0, y_start: float = 0.0,
                 heading: float = 0.0):
        if not isinstance(world, World):
            raise TypeError(type_error_message("__init__", "world",
                                               "World", world))
        self.__x: float = float(x_start)
        self.__y: float = float(y_start)
        self.__pen_up: bool = False
        self.__heading: float = float(heading)
        self.__world: 'World' = world

    def __str__(self) -> str:
        return f"Turtle: at x={self.__x}, y={self.__y}, " +\
               f"heading: {self.__heading} degrees, " +\
               "pen: " + ('up' if self.__pen_up else 'down')

    @property
    def x(self) -> float:  # pylint: disable=invalid-name
        """
        the x coordinate of this ``Turtle`` within its ``World``

        :type: float
        """
        return self.__x

    @property
    def y(self) -> float:  # pylint: disable=invalid-name
        """
        the y coordinate of this ``Turtle`` within its ``World``

        :type: float
        """
        return self.__y

    @property
    def pen_up(self) -> bool:
        """
        `True` if the ``Turtle``'s pen is up (and hence not drawing lines
        when it moves)

        `False` if the ``Turtle``'s pen is down (and hence drawing lines
        when it moves)

        :type: bool
        """
        return self.__pen_up

    @pen_up.setter
    def pen_up(self, flag: bool) -> None:
        if bool(flag):
            self.pen_up = True
        else:
            self.pen_up = False

    @property
    def heading(self) -> float:
        """
        The direction the `Turtle` is heading in degrees.
         is right, 90 is up, 180 is left, 270 is down

        :type: float
        """
        return self.__heading

    @heading.setter
    def heading(self, degrees: float) -> None:
        degrees = float(degrees) % 360.0
        self.__heading = degrees

    def forward(self, distance: float) -> None:
        """
        Requests the `Turtle` to move in the direction it is
        currently headed

        :param float distance: How many pixel units to move forward
        """
        distance = float(distance)
        radians = math.radians(self.__heading)
        delta_x = math.sin(radians) * distance
        delta_y = math.cos(radians) * distance
        self.move_to(self.__x + delta_x, self.__y + delta_y)

    def turn(self, degrees: float) -> None:
        """
        Requests the turtle to turn counterclockwise by the specified number
        of degrees. A negative number can be used to turn clockwise.

        This adjusts the turtles heading by adding the specified number
        of degrees to the current heading.

        If the result is outside the 0 - 360 degree range,
        the new heading is adjusted to be in the 0 - 360
        degree range by using the remainder when dividing by 360.

        :param float degrees: number of degrees to turn counterclockwise
        """
        degrees = float(degrees)
        new_heading = (self.__heading + degrees) % 360.0
        self.__heading = new_heading

    def move_to(self, x_position: float, y_position: float) -> None:
        """
        Moves the turtle to a new location without changing its heading

        Note: if the pen is down, a line is drawn in the
            ``Turtle``'s ``World``

        :param float x_position: x coordinate of the location to move to
        :param float y_position: y coordinate of the location to move to
        """
        x_position = float(x_position)
        y_position = float(y_position)
        if not self.__pen_up:
            self.__world.picture.add_line(int(self.__x), int(self.__y),
                                          int(x_position), int(y_position))
        self.__x = x_position
        self.__y = y_position

    def turn_to_face(self, x_position: float, y_position: float) -> None:
        """
        Adjusts the ``Turtle``'s heading so it is facing the
        specified location.

        This does not cause its location to change

        :param float x_position: x coordinate of the location to turn towards
        :param float y_position: y coordinate of the location to turn towards
        """
        delta_x = self.__x - float(x_position)
        delta_y = self.__y - float(y_position)
        radians = math.atan2(delta_x, delta_y)
        degrees = math.degrees(radians)
        self.__heading = degrees


class World(collections.abc.Iterable):
    """
    The world where the turtles live
    """

    def __init__(self, width: int = 640, height: int = 480):
        """
        Write better docstring

        :param int width:
        :param int height:
        """
        self.picture: pictures.Picture = pictures.Picture.make_empty(width,
                                                                     height)
        self.__turtle_list: typing.List[Turtle] = list()

    def new_turtle(self, x_position: float = 0.0, y_position: float = 0.0,
                   heading: float = 0.0) -> Turtle:
        """
        Write better docstring

        :param float x_position:
        :param float y_position:
        :param float heading:
        :return:
        :rtype: Turtle
        """
        turtle = Turtle(self, x_position, y_position, heading)
        self.__turtle_list.append(turtle)
        return turtle

    def __str__(self) -> str:
        return f"World: {len(self.__turtle_list)} turtles"

    def __iter__(self) -> typing.Iterator[Turtle]:
        return iter(self.__turtle_list)
