#
# Package: MediaComp
# Module: colors
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies, sounds) from
# http://mediacomputation.org created by Mark Guzdial and Barbara Ericson
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/).
#
"""
Provide module level docstring
"""
# module abc is standard in Python 3: https://docs.python.org/3/library/abc.html
# used to create abstract base classes
import abc

# module math is standard in Python 3: https://docs.python.org/3/library/math.html
# used for sqrt, sin, cos, atan2, ...
import math

# module typing is standard in Python 3.5+: https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton code: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type, doesn't mean
# that at runtime it will actually be of that type: dynamic checking or casting/conversion
#  still needs to be done
import typing

# module colorsys is standard in Python: https://docs.python.org/3.7/library/colorsys.html
# for background on color space systems, see: http://poynton.ca/PDFs/ColorFAQ.pdf
# and https://www.cambridgeincolour.com/tutorials/color-spaces.htm
import colorsys

# Type alias
RGB = typing.Tuple[int, int, int]
RGBA = typing.Tuple[int, int, int, int]
RGBZ = typing.Tuple[int, int, int, int]
RGBfloat = typing.Tuple[float, float, float]
HLS = typing.Tuple[float, float, float]
HSV = typing.Tuple[float, float, float]


# class MetaRGB is the metaclass for BaseRGB
# so object properties of MetaRGB become class properties of BaseRGB.
#
# properties correspond to standard named colors and are read-only,
# so BaseRGB.white = Color(0,0,0) will not be allowed!
#
# the values of the properties are lazily constructed, so that while fetching
# the value of BaseRGB.white multiple times will invoke MetaRGB.white()
# each time, constructing a new Color object will happen only once.
#
class MetaColors(abc.ABCMeta):
    """
    Not a "public" class, do we really need a docstring
    """
    _white = None
    _black = None
    _blue = None
    _red = None
    _green = None
    _gray = None
    _dark_gray = None
    _light_gray = None
    _yellow = None
    _orange = None
    _pink = None
    _magenta = None
    _cyan = None

    @property
    def white(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._white is None:
            MetaColors._white = Color(255, 255, 255)
        return MetaColors._white

    @property
    def black(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._black is None:
            MetaColors._black = Color(0, 0, 0)
        return MetaColors._black

    @property
    def blue(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._blue is None:
            MetaColors._blue = Color(0, 0, 255)
        return MetaColors._blue

    @property
    def red(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._red is None:
            MetaColors._red = Color(255, 0, 0)
        return MetaColors._red

    @property
    def green(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._green is None:
            MetaColors._green = Color(0, 255, 0)
        return MetaColors._green

    @property
    def gray(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._gray is None:
            MetaColors._gray = Color(128, 128, 128)
        return MetaColors._gray

    @property
    def dark_gray(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._dark_gray is None:
            MetaColors._dark_gray = Color(64, 64, 64)
        return MetaColors._dark_gray

    @property
    def light_gray(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._light_gray is None:
            MetaColors._light_gray = Color(192, 192, 192)
        return MetaColors._light_gray

    @property
    def yellow(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._yellow is None:
            MetaColors._yellow = Color(255, 255, 0)
        return MetaColors._yellow

    @property
    def orange(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._orange is None:
            MetaColors._orange = Color(255, 200, 0)
        return MetaColors._orange

    @property
    def pink(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._pink is None:
            MetaColors._pink = Color(255, 175, 175)
        return MetaColors._pink

    @property
    def magenta(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._magenta is None:
            MetaColors._magenta = Color(255, 0, 255)
        return MetaColors._magenta

    @property
    def cyan(cls) -> 'Color':
        """ lazy singleton """
        if MetaColors._cyan is None:
            MetaColors._cyan = Color(255, 0, 255)
        return MetaColors._cyan


class Colors(metaclass=MetaColors):
    """
    Provides attributes that are color objects

    Attributes
    ----------
    white : Color
        Lazily constructed singleton for object initialized with Color(255, 255, 255)
    black : Color
        Lazily constructed singleton for object initialized with Color(0, 0, 0)
    blue : Color
    red : Color
    green : Color
    gray : Color
    darkGray : Color
    lightGray : Color
    yellow : Color
    orange : Color
    pink : Color
    magenta :  Color
    cyan : Color
    """
    pass


class BaseRGB:
    """
    class docstring goes here

    This class is not intended for direct use by importers of this module
    """
    def __init__(self, rgb: RGB):
        self.__rgb: RGB = rgb

    # input may be tuple of uint8
    # output will be tuple of unconstrained int
    @staticmethod
    def unpack(rgb: RGB) -> RGB:
        """
        Converts sequence of at least 3 values to a tuple of 3 ints

        :param rgb: a sequence of 3 values convertible to `int`
        :type rgb: Tuple[int-like, int-like, int-like]
        :return: an actual `Tuple` of `int` values
        """
        return int(rgb[0]), int(rgb[1]), int(rgb[2])

    @staticmethod
    def to_uint8(value: int) -> int:
        """
        clamps int-like value to a 0-255 int value

        :param int value:
        :return: value converted to 0-255 range by camping
        :rtype int:
        """
        return min(255, max(0, int(value)))

    @staticmethod
    def clamp(rgb: RGB) -> RGB:
        """
        Converts input tuple to a tuple of ints each in the range 0-255

        :param rgb: red, green, blue triple with values that may or may
                    not be outside the 0-255 range

        """
        return min(255, max(0, int(rgb[0]))),\
            min(255, max(0, int(rgb[1]))),\
            min(255, max(0, int(rgb[2])))

    @property
    def red(self) -> int:
        """
        The 0-255 `int` value representing the red component of the
        underlying `Tuple`
        """
        return int(self.rgb[0])

    @property
    def green(self) -> int:
        """
        The 0-255 `int` value representing the green component of the
        underlying `Tuple`
        """
        return int(self.rgb[1])

    @property
    def blue(self) -> int:
        """
        The 0-255 :py:type:int value representing the blue component of the
        underlying `Tuple`
        """
        return int(self.rgb[2])

    @property
    def rgb(self) -> RGB:
        """
        An unpacked version of the underlying `Tuple`
        """
        _rgb = self.__rgb
        return int(_rgb[0]), int(_rgb[1]), int(_rgb[2])

    def __repr__(self) -> str:
        return f"BaseRGB(({self.red},{self.green},{self.blue}))"

    def __str__(self) -> str:
        return self.__repr__()

    def distance(self, color: 'BaseRGB') -> float:
        """
        The Cartesian distance between this color and another color

        :param color: the other color
        :type color: :py:class:`~.Color`
        """

        if not isinstance(color, BaseRGB):
            message_prefix = "BaseRGB.distance(): "
            message_middle = "expected color to be a BaseRGB object, actually "
            raise TypeError(message_prefix + message_middle + f"{type(color)}")
        red_diff = float(self.red) - float(color.red)
        green_diff = float(self.green) - float(color.green)
        blue_diff = float(self.blue) - float(color.blue)
        sum_squares = red_diff * red_diff + \
            green_diff * green_diff + \
            blue_diff * blue_diff
        return math.sqrt(sum_squares)


class Color(BaseRGB):
    """
    Class docstring goes here.
    """
    @staticmethod
    def from_rgb(rgb: RGB) -> 'Color':
        """
        Write better docstring

        :param rgb:
        :return:

        """
        return Color(rgb[0], rgb[1], rgb[2])

    @staticmethod
    def from_rgb_float(rgb: RGBfloat) -> 'Color':
        """
        Write better docstring

        :param rgb:
        :return:
        """
        return Color(int(rgb[0] * 255 + 0.5),
                     int(rgb[1] * 255 + 0.5),
                     int(rgb[2] * 255 + 0.5))

    def __init__(self, r: int = 0, g: int = 0, b: int = 0, *,
                 rgb: typing.Optional[RGB] = None):
        if rgb is not None:
            super().__init__(rgb)
        else:
            super().__init__(BaseRGB.clamp((r, g, b)))

    def __repr__(self) -> str:
        return f"Color({self.red},{self.green},{self.blue})"

    def __str__(self) -> str:
        return self.__repr__()

    def _repr_html_(self) -> str:
        html_color: str = "#{0:02x}{1:02x}{2:02x}".format(self.red,
                                                          self.green,
                                                          self.blue)
        text: str = "r:{0:3d}, g:{1:3d}, b:{2:3d}".format(self.red,
                                                          self.green,
                                                          self.blue)
        table_start: str = "<table style='border:0px'><tr>"
        cell_start: str = "<td style='padding:0px;margin:0px;background:"
        middle: str = ";height:64px;'>&nbsp;</td></tr><tr><td><pre>"
        end: str = "</pre></td></tr></table>"
        result: str = table_start + cell_start + html_color + middle + text + end
        return result

    def rgb_float(self) -> RGBfloat:
        """
        Converts internal `int`-based tuple on a scale of 0-255 into a
        `float`-based tuple on a scale of 0.0 - 1.0

        :rtype: RGB_float
        """
        return self.__rgb[0]/255.0, self.__rgb[1]/255.0, self.__rgb[2]/255.0

    def hsv(self) -> HSV:
        """
        Converts from RGB to HSV

        :return: a  Hue, Saturation, Value tuple from
                :py:func:`colorsys.rgb_to_hsv`
        :rtype: HSV
        """
        rgb: RGBfloat = self.rgb_float()
        return colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])

    def hls(self) -> HLS:
        """
        Converts from RGB to HLS

        :return: a  Hue, Lightness, Saturation tuple from
                :py:func:`colorsys.rgb_to_hls`
        :rtype: HLS
        """
        rgb: RGBfloat = self.rgb_float()
        return colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])

    def darker(self) -> 'Color':
        """

        :return: a :py:func:`~Color` with its components scaled by
                multiplying them by 0.7
        :rtype: Color
        """
        rgb: RGB = self.rgb
        return Color(rgb[0] * 0.7, rgb[1] * 0.7, rgb[1] * 0.7)

    def lighter(self) -> 'Color':
        """

        :return: a color with its components scaled by multiplying
                them by 1.0/0.7
        :rtype: Color
        """
        rgb: RGB = self.rgb
        return Color(rgb[0] / 0.7, rgb[1] / 0.7, rgb[1] / 0.7)
