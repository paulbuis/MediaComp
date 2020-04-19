#
# Package: MediaComp
# Module: jes.colors
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies,
# sounds) from http://mediacomputation.org created by Mark Guzdial and others
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/.

# This package contains JES-compatible wrappers for class and instance methods in MediaComp.colors


# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
"""
Suggested usage in Jupyter:

from MediaComp.jes.colors import *
"""
import typing
from .. import colors


# noinspection PyPep8Naming
# noinspection PyShadowingNames
def makeColor(redColor: typing.Union[int, colors.Color], green: int = 0,  # pylint: disable=redefined-outer-name
              blue: int = 0) -> colors.Color:  # pylint: disable=redefined-outer-name
    """
    Takes three integer inputs for the red, green, and blue components
    (in order) and returns a color object.
    If green and blue are omitted, the red value is used as the intensity
    of a gray color.
    Also it works with only a color as input and returns a new color object
    with the same RGB values as the original.

    :param redColor: the amount of red you want in the color (or a Color
        object you want to duplicate)
    :param int green: the amount of green you want in the color (optional)
    :param int blue: the amount of blue you want in the picture (optional)
    :return: the color made from the inputs
    :rtype: Color
    """
    if isinstance(redColor, colors.Color):
        red = redColor.red  # pylint: disable=redefined-outer-name
        green = redColor.green
        blue = redColor.blue
    else:
        red = redColor  # pylint: disable=redefined-outer-name
    return colors.Color(red, green, blue)


def color_type_error(fun_name: str, param_name: str, expected: str,
                     actual: typing.Any) -> str:
    """ generates error message when TypeErrors are raised """
    return f"In MediaComp.pictures.{fun_name}: {param_name} " + \
           f"expected a {expected}, actually {type(actual)}"


# noinspection PyPep8Naming
def makeDarker(color: colors.Color) -> colors.Color:
    """
    Takes a color and returns a slightly darker version of the
    original color.

    :param Color color: the color you want to darken
    :return: the new, darker color
    :rtype: Color
    :raises TypeError: if ``color`` is not a :py:class:`~.colors.Color`
    """
    if not isinstance(color, colors.Color):
        raise TypeError(color_type_error("makeDarker", "color",
                                         "Color", color))
    return color.darker()


# noinspection PyPep8Naming
def makeLighter(color: colors.Color) -> colors.Color:
    """
    Takes a color and returns a slightly lighter version of
    the original color.

    :param Color color: the color you want to lighten
    :return: the new, lighter color
    :rtype: Color
    :raises TypeError: if ``color`` is not a :py:class:`~.colors.Color`
    """
    if not isinstance(color, colors.Color):
        raise TypeError(color_type_error("makeLighter", "color",
                                         "Color", color))
    return color.lighter()


# noinspection PyPep8Naming
def makeBrighter(color: colors.Color) -> colors.Color:
    """
    Takes a color and returns a slightly lighter version of the original
    color. (Same as makeLighter)

    :param color: the color you want to lighten
    :return: the new, lighter color
    :rtype: Color
    :raises TypeError: if ``color`` is not a :py:class:`~.colors.Color`
    """
    if not isinstance(color, colors.Color):
        raise TypeError(color_type_error("makeBrighter", "color",
                                         "Color", color))
    return makeLighter(color)


def distance(color1: colors.Color, color2: colors.Color) -> float:
    """
    Takes two Color objects and returns a single number representing the
    distance between the colors.
    The red, green, and blue values of the colors are taken as a point
    in (x, y, z) space, and the Cartesian distance is computed.

    :param color1: the first color you want compared
    :param color2: the second color you want compared
    :return: a floating point number representing the Cartesian distance
        between the colors
    :rtype: float
    :raises TypeError: if either ``color1`` or ``color2`` is not a :py:class:`~.colors.Color`
    """
    if not isinstance(color1, colors.Color):
        raise TypeError(color_type_error("distance", "color1", "Color", color1))
    if not isinstance(color2, colors.BaseRGB):
        raise TypeError(color_type_error("distance", "color2", "Color", color2))
    return color1.distance(color2)


# Color objects are not mutable.
# But, these variables named "white", "black", etc., can be assigned to
# something else by a perverse user, so we are not going to depend
# on them, but JES provides them, so we will too.
white = colors.Colors.white
"""
:value: `Color(255, 255, 255)`
:type: colors.Color
"""

black = colors.Colors.black
"""
:value: `Color(0, 0, 0)`
:type: colors.Color
"""

blue = colors.Colors.blue
"""
:value: `Color(0, 0, 255)`
:type: colors.Color
"""

red = colors.Colors.red
"""
:value: `Color(255, 0, 0)`
:type: colors.Color
"""

green = colors.Colors.green
"""
:value: `Color(0, 255, 0)`
:type: colors.Color
"""

gray = colors.Colors.gray
"""
:value: `Color(128, 128, 128)`
:type: colors.Color
"""

darkGray = colors.Colors.dark_gray
"""
:value: `Color(64, 64, 64)`
:type: colors.Color
"""

lightGray = colors.Colors.light_gray
"""
:value: `Color(192, 192, 192)`
:type: colors.Color
"""

yellow = colors.Colors.yellow
"""
:value: `Color(255, 255, 0)`
:type: colors.Color
"""

orange = colors.Colors.orange
"""
:value: `Color(255, 200, 0)`
:type: .Color
"""

pink = colors.Colors.pink
"""
:value: `Color(255, 175, 175)`
:type: Color
"""

magenta = colors.Colors.magenta
"""
:value: `Color(255, 0, 255)`
:type: Color
"""

cyan = colors.Colors.cyan
"""
:value: `Color(255, 0, 255)`
:type: Color
"""
