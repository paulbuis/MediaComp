#
#
# Package: MediaComp
# Module: jes
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies, sounds) from
# http://mediacomputation.org created by Mark Guzdial and others
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/.

"""
Suggested usage in Juptyer:

from MediaComp.jes import *

"""

# module typing is standard in Python 3.5+: https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton code: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type, doesn't mean
# that at runtime it will actually be of that type: dynamic checking or casting/conversion still needs to be done
# static inspection may incorrectly show Tuple as an unused import, it is used for type aliases only

import typing

# from . import colors (taken care of by from . import pictures)
from . import pictures
# from . import files (taken care of by from . import pictures)
from . import sounds
from . import turtles

# from .colors import * (taken care of by from .pictures import pictures)
from .pictures import *
from .files import *


# noinspection PyPep8Naming
# noinspection PyArgumentList
def makeColor(redColor: typing.Union[int, Color], green: int = 0, blue: int = 0) -> colors.Color:
    """
    Takes three integer inputs for the red, green, and blue components (in order) and returns a color object.
    If green and blue are omitted, the red value is used as the intensity of a gray color.
    Also it works with only a color as input and returns a new color object with the same RGB values as the original.

    :param redColor: the amount of red you want in the color (or a Color object you want to duplicate)
    :param green: the amount of green you want in the color (optional)
    :param blue: the amount of blue you want in the picture (optional)
    :return: the color made from the inputs
    """
    if isinstance(redColor, Color):
        red = redColor.red
        green = redColor.green
        blue = redColor.blue
    else:
        red = redColor
    return colors.Color(red, green, blue)


def color_type_error(fun_name: str, param_name: str, expected: str, actual: typing.Any) -> str:
    return f"In MediaComp.pictures.{fun_name}: {param_name} expected a {expected}, actually {type(actual)}"


# noinspection PyPep8Naming
def makeDarker(color: colors.BaseRGB) -> colors.Color:
    """
    Takes a color and returns a slightly darker version of the original color.

    :param color: the color you want to darken
    :return: the new, darker color
    """
    if not isinstance(color, colors.Color):
        raise TypeError(color_type_error("makeDarker", "color", "Color", color))
    return color.darker()


# noinspection PyPep8Naming
def makeLighter(color: colors.Color) -> colors.Color:
    """
    Takes a color and returns a slightly lighter version of the original color.

    :param color: the color you want to lighten
    :return: the new, lighter color
    """
    if not isinstance(color, colors.Color):
        raise TypeError(color_type_error("makeLighter", "color", "Color", color))
    return color.lighter()


# noinspection PyPep8Naming
def makeBrighter(color: colors.Color) -> colors.Color:
    """
    Takes a color and returns a slightly lighter version of the original color. (Same as makeLighter)

    :param color: the color you want to lighten
    :return: the new, lighter color
    """
    if not isinstance(color, colors.Color):
        raise TypeError(color_type_error("makeBrighter", "color", "Color", color))
    return makeLighter(color)


def distance(color1: colors.Color, color2: colors.BaseRGB) -> float:
    """
    Takes two Color objects and returns a single number representing the distance between the colors.
    The red, green, and blue values of the colors are taken as a point in (x, y, z) space,
    and the Cartesian distance is computed.

    :param color1: the first color you want compared
    :param color2: the second color you want compared
    :return: a floating point number representing the Cartesian distance between the colors
    """
    if not isinstance(color1, colors.Color):
        raise TypeError(color_type_error("distance", "color1", "Color", color1))
    if not isinstance(color1, colors.BaseRGB):
        raise TypeError(color_type_error("distance", "color2", "Color", color2))
    return color1.distance(color2)


# Color objects are not mutable.
# But, these variables named "white", "black", etc., can be assigned to something
# else by a perverse user, so we are not going to depend
# on them, but JES provides them, so we will too.
white = colors.Colors.white
"""`Color(255, 255, 255)`"""

black = colors.Colors.black
"""`Color(0, 0, 0)`"""

blue = colors.Colors.blue
"""`Color(0, 0, 255)`"""

red = colors.Colors.red
"""`Color(255, 0, 0)`"""

green = colors.Colors.green
"""`Color(0, 255, 0)`"""

gray = colors.Colors.gray
"""`Color(128, 128, 128)`"""

darkGray = colors.Colors.darkGray
"""`Color(64, 64, 64)`"""

lightGray = colors.Colors.lightGray
"""`Color(192, 192, 192)`"""

yellow = colors.Colors.yellow
"""`Color(255, 255, 0)`"""

orange = colors.Colors.orange
"""`Color(255, 200, 0)`"""

pink = colors.Colors.pink
"""`Color(255, 175, 175)`"""

magenta = colors.Colors.magenta
"""`Color(255, 0, 255)`"""

cyan = colors.Colors.cyan
"""`Color(255, 0, 255)`"""

##########################################################################################
#
# JES wrapper functions functions for methods of pictures.PixelInfo
#
# PixelInfo is a subclass of colors.Color (PixelInfo also has x, y coordinates)
# PixelInfo is the superclass of pictures.Pixel (PixelInfo has read-only color properties)
#   Hence, these functions can also be used with Pixel objects
#
##########################################################################################


# noinspection PyPep8Naming
def getRed(pixel: pictures.PixelInfo) -> int:
    """
    Takes a Pixel object and returns the value (between 0 and 255) of the amount of redness in that pixel.

    :param pixel: the pixel you want to get the amount of red from
    :return: the red value of the pixel
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getRed", "pixel", "Pixel or PixelInfo", pixel))
    return pixel.red


# noinspection PyPep8Naming
def getGreen(pixel: pictures.PixelInfo) -> int:
    """
    Takes a Pixel object and returns the value (between 0 and 255) of the amount of greenness in that pixel.

    :param pixel: the pixel you want to get the amount of green from
    :return: the green value of the pixel
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getGreen", "pixel", "Pixel or PixelInfo", pixel))
    return pixel.green


# noinspection PyPep8Naming
def getBlue(pixel: pictures.PixelInfo) -> int:
    """
    Takes a Pixel object and returns the value (between 0 and 255) of the amount of blueness in that pixel.

    :param pixel: the pixel you want to get the amount of blue from
    :return: the blue value of the pixel
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getBlue", "pixel", "Pixel or PixelInfo", pixel))
    return pixel.blue


# noinspection PyPep8Naming
def getColor(pixel: pictures.PixelInfo) -> colors.Color:
    """
    Takes a Pixel and returns the Color object at that pixel.

    :param pixel: the pixel you want to extract the color from
    :return: the color of the pixel
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getColor", "pixel", "Pixel", pixel))
    return pixel.color


# noinspection PyPep8Naming
def getX(pixel: pictures.PixelInfo) -> int:
    """
    Takes in a pixel object and returns the x position of where that pixel is in the picture

    :param pixel: the pixel you want to find the x-coordinate of
    :return: the x-coordinate of the pixel
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getX", "pixel", "Pixel or PixelInfo", pixel))
    return pixel.x


# noinspection PyPep8Naming
def getY(pixel: pictures.PixelInfo) -> int:
    """
    Takes in a pixel object and returns the y position of where that pixel is in the picture.

    :param pixel: the pixel you want to find the y-coordinate of
    :return: the y-coordinate of the pixel
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getY", "pixel", "Pixel or PixelInfo", pixel))
    return pixel.y


#################################################################################
#
# JES wrapper functions functions for methods of pictures.Pixel
#
# Pixel is a subclass of pictures.PixelInfo which is a subclass of pictures.Color
#     unlike its superclasses, its color can be changed which changes
#     the underlying pictures.Picture object
#
#################################################################################


# noinspection PyPep8Naming
def setColor(pixel: pictures.Pixel, color: colors.Color) -> None:
    """
    Takes in a pixel and a color, and sets the pixel to the given color.

    :param pixel: the pixel you want to set the color of
    :param color: the color you want to set the pixel to
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setColor", "pixel", "Pixel", pixel))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("setColor", "color", "Color", color))
    pixel.color = color


# noinspection PyPep8Naming
def setRed(pixel: pictures.Pixel, redValue: int) -> None:
    """
    Takes in a Pixel object and a value (between 0 and 255) and sets the redness of that pixel to the given value.

    :param pixel: the pixel you want to set the red value of
    :param redValue: a number (0 - 255) for the new red value of the pixel
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setRed", "pixel", "Pixel", pixel))
    pixel.red = redValue


# noinspection PyPep8Naming
def setGreen(pixel: pictures.Pixel, greenValue: int) -> None:
    """
    Takes in a Pixel object and a value (between 0 and 255) and sets the greenness of that pixel to the given value.

    :param pixel: the pixel you want to set the green value of
    :param greenValue: a number (0 - 255) for the new green value of the pixel
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setGreen", "pixel", "Pixel", pixel))
    pixel.green = greenValue


# noinspection PyPep8Naming
def setBlue(pixel: pictures.Pixel, blueValue: int) -> None:
    """
    Takes in a Pixel object and a value (between 0 and 255) and sets the blueness of that pixel to the given value.

    :param pixel: the pixel you want to set the blue value of
    :param blueValue: a number (0 - 255) for the new blue value of the pixel
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setBlue", "pixel", "Pixel", pixel))
    pixel.blue = blueValue


##############################################################################
#
# JES wrapper functions functions for methods of pictures.TextStyle
#
##############################################################################


# noinspection PyPep8Naming
def makeStyle(fontName: str, emphasis: str, size: float) -> pictures.TextStyle:
    """
    Takes a font name, emphasis, and size in points as input. Returns a Font object with the given parameters.

    :param fontName: the name of the font you want in the style (sansSerif, serif, mono)
    :param emphasis: the type of emphasis you want in the style (italic, bold, italic + bold, plain)
    :param size: the size of the font you want in the style
    :return:
    """
    return pictures.TextStyle(fontName, emphasis, size)

##############################################################################
#
# JES wrapper functions functions for methods of pictures.PILImage
#
##############################################################################


# noinspection PyPep8Naming
def addArc(picture: pictures.PILImage, startX: int, startY: int, width: int, height: int,
           start: float, angle: float,
           color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, (x,y) coordinates, width, height, two integer angles, and (optionally) a color as input.
    Adds an outline of an arc starting at (x,y) at an initial angle of "start" with the given width and height.
    The angle of the arc itself is "angle", which is relative to "start."
    Default color is black.

    :param picture: the picture you want to draw the arc on
    :param startX: the x-coordinate of the center of the arc
    :param startY: the y-coordinate of the center of the arc
    :param width: the width of the arc
    :param height: the height of the arc
    :param start: the start angle of the arc in degrees
    :param angle: the angle of the arc relative to start in degrees
    :param color: the color you want to draw in (optional)
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addArc", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_arc(startX, startY, width, height, start, angle, color)


# noinspection PyPep8Naming
def addArcFilled(picture: pictures.PILImage, startX: int, startY: int, width: int, height: int,
                 start: float, angle: float,
                 color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, (x,y) coordinates, width, height, two integer angles, and (optionally) a color as input.
    Adds an o filled arc starting at (x,y) at an initial angle of "start" with the given width and height.
    The angle of the arc itself is "angle", which is relative to "start."
    Default color is black.

    :param picture: the picture you want to draw the arc on
    :param startX: the x-coordinate of the center of the arc
    :param startY: the y-coordinate of the center of the arc
    :param width: the width of the arc
    :param height: the height of the arc
    :param start: the start angle of the arc in degrees
    :param angle: the angle of the arc relative to start in degrees
    :param color: the color you want to draw in (optional)
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addArcFilled", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_arc_filled(startX, startY, width, height, start, angle, color)


# noinspection PyPep8Naming
def addLine(picture: pictures.Picture, startX: int, startY: int, endX: int, endY: int,
            color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers), and an ending (x, y) position,
    two more numbers, four total), and (optionally) a color as input.

    Adds a line from the starting point to the ending point in the picture. Default color is black.

    :param picture: the picture you want to draw the line on
    :param startX: the x position you want the line to start
    :param startY: the y position you want the line to start
    :param endX: the x position you want the line to end
    :param endY: the y position you want the line to end
    :param color: the color you want to draw in (optional)
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("addLine", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_line(startX, startY, endX, endY, color)


# noinspection PyPep8Naming
def addOval(picture: pictures.PILImage, startX: int, startY: int, width: int, height: int,
            color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers), a width and height (two more numbers, four total),
    and (optionally) a color as input. Adds an oval outline of the given dimensions using the (x,y) as the upper left
    corner of the bounding rectangle. Default color is black.

    :param picture: the picture you want to draw the rectangle on
    :param startX: the x-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    :param startY: the y-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    :param width: the width of the oval
    :param height: the height of the oval
    :param color: the color you want to draw in (optional)
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addOval", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_oval(startX, startY, height, width, color)


# noinspection PyPep8Naming
def addOvalFilled(picture: pictures.PILImage, startX: int, startY: int,
                  width: int, height: int, color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers), a width and height (two more numbers, four total),
    and (optionally) a color as input. Adds a filled oval outline of the given dimensions using the (x,y) as the upper
    left corner of the bounding rectangle. Default color is black.

    :param picture: the picture you want to draw the rectangle on
    :param startX: the x-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    :param startY: the y-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    :param width: the width of the oval
    :param height: the height of the oval
    :param color: the color you want to draw in (optional)

    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addOvalFilled", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_oval_filled(startX, startY, height, width, color)


# noinspection PyPep8Naming
def addRect(picture: pictures.PILImage, startX: int, startY: int, width: int, height: int,
            color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers), a width and height (two more numbers, four total),
    and (optionally) a color as input. Adds a rectangular outline of the specified dimensions using the (x,y) as the
    upper left corner. Default color is black.

    :param picture: the picture you want to draw the rectangle on
    :param startX: the x-coordinate of the upper left-hand corner of the rectangle
    :param startY: the y-coordinate of the upper left-hand corner of the rectangle
    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :param color: the color you want to draw in (optional)
    :return:
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addRect", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_oval_filled(startX, startY, height, width, color)


# noinspection PyPep8Naming
def addRectFilled(picture: pictures.PILImage, startX: int, startY: int, width: int, height: int,
                  color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers), a width and height (two more numbers, four total),
    and (optionally) a color as input. Adds a filled rectangle of the specified dimensions using the (x,y) as the
    upper left corner. Default color is black.

    :param picture: the picture you want to draw the rectangle on
    :param startX: the x-coordinate of the upper left-hand corner of the rectangle
    :param startY: the y-coordinate of the upper left-hand corner of the rectangle
    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :param color: the color you want to draw in (optional)
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addRectFilled", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_line(startX, startY, width, height, color)


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def addText(picture: pictures.Picture, xpos: int, ypos: int, text: str, color=colors.Colors.black) -> None:
    """
    Takes a picture, an x position and a y position (two numbers),
    and some text as a string, which will get drawn into the picture,
    in the specified color. Default is black.

    :param picture: the picture you want to draw the rectangle on
    :param xpos: the x-coordinate where you want to start writing the text
    :param ypos: the x-coordinate where you want to start writing the text
    :param text: string containing the text you want written
    :param color: the color you want to draw in (optional)
    :return:
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addRectFilled", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    picture.add_text(xpos, ypos, text, color)


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def addTextWithStyle(picture: pictures.Picture, xpos: int, ypos: int, text: str, style: str,
                     color=colors.Colors.black) -> None:
    """
    Takes a picture, an x position and a y position (two numbers),
    and some text as a string, which will get drawn into the picture,
    in the given font style and specified color. Default is black.

    :param picture: the picture you want to draw the rectangle on
    :param xpos: the x-coordinate where you want to start writing the text
    :param ypos: the y-coordinate where you want to start writing the text
    :param text: string containing the text you want written
    :param style: the font style you want to draw in (See makeStyle)
    :param color: the color you want to draw in (optional)
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addRectFilled", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color", "Color", color))
    text_style = pictures.TextStyle(style, "", 10)  # TODO: fix this !
    picture.add_text_with_style(xpos, ypos, text, text_style, color)


# TODO: implement this
# display will embed in HTML via JesImage._repr_html_ method
def show(picture: pictures.Picture) -> None:
    """
    Shows the picture provided as input.
    :param picture: the picture you want to see
    :return:
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("show", "picture", "Picture", picture))
    # function display is in imported module IPython.core.display
    # probably will trigger type checker warning, display is heavily overloaded
    # IPython.core.display.display(picture)
    raise NotImplemented


# TODO: edit doc string
# just alias show() since we aren't interactive
def repaint(picture: pictures.Picture) -> None:
    """

    :param picture:
    :return:
    """
    show(picture)


# noinspection PyPep8Naming
def copyInto(smallPicture: pictures.PILImage, bigPicture: pictures.PILImage, startX: int, startY: int) -> None:
    """
    Takes two pictures, a x position and a y position as input, and modifies bigPicture by copying into it as
    much of smallPicture as will fit, starting at the x,y position in the destination picture.

    :param smallPicture: the picture to paste into the big picture
    :param bigPicture: the picture to be modified
    :param startX: the X coordinate of where to place the small picture on the big one
    :param startY: the Y coordinate of where to place the small picture on the big one
    """
    if not isinstance(smallPicture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("copyInto", "smallPicture", "Picture", smallPicture))
    if not not isinstance(bigPicture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("copyInto", "bigPicture", "Picture", bigPicture))
    startX = int(startX)
    startY = int(startY)
    bigPicture.copy_into(smallPicture, startX, startY)


# noinspection PyPep8Naming
def writePictureTo(picture: pictures.PILImage, path: str) -> None:
    """
    Takes a picture and a file name (string) as input, then writes the picture to the file as a JPEG, PNG, or BMP.
    (Be sure to end the filename in ".jpg" or ".png" or ".bmp" for the operating system to understand it well.)

    :param picture: the picture you want to be written out to a file
    :param path:
    :return: the path to the file you want the picture written to
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("writePictureTo", "pict", "Picture", picture))
    picture.save(path)


# noinspection PyPep8Naming
def getHeight(picture: pictures.PILImage) -> int:
    """
    Takes a picture as input and returns its length in the number of pixels yop-to-bottom in the picture.

    :param picture: the picture you want to get the height of
    :return: the height of the picture
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("getHeight", "pict", "Picture", picture))
    return picture.height


# noinspection PyPep8Naming
def getWidth(picture: pictures.PILImage) -> int:
    """
    Takes a picture as input and returns its length in the number of pixels left-to-right in the picture.

    :param picture: the picture you want to get the width of
    :return:
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("getWidth", "pict", "Picture", picture))
    return picture.width


##############################################################################
#
# JES wrapper functions functions for methods of pictures.RGBImage
#
##############################################################################


# noinspection PyPep8Naming
def setAllPixelsToAColor(picture: pictures.RGBImage, color: colors.BaseRGB = colors.Colors.black) -> None:
    """
    Modifies the whole image so that every pixel in that image is the given color.

    :param picture: the picture to change the pixels of
    :param color: the color to set each pixel to
    """
    if not isinstance(picture, pictures.RGBImage):
        raise TypeError(pictures.type_error_message("setAllPixelsToAColor", "image", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("setAllPixelsToAColor", "color", "Color", color))
    picture.set_color(color)


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def getPixel(picture: pictures.RGBImage, xpos: int, ypos: int) -> pictures.Pixel:
    """
    Takes a picture, an x position and a y position (two numbers), and returns the Pixel
    object at that point in the picture. (Same as getPixelAt)

    :param picture: the picture you want to get the pixel from
    :param xpos: the x-coordinate of the pixel you want
    :param ypos: the y-coordinate of the pixel you want
    :return:
    """
    if not isinstance(picture, pictures.RGBImage):
        raise TypeError(pictures.type_error_message("getPixel", "pict", "Picture", picture))
    return picture[xpos, ypos]


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def getPixelAt(picture: pictures.RGBImage, xpos: int, ypos: int) -> pictures.Pixel:
    """
    Takes a picture, an x position and a y position (two numbers), and returns the Pixel
    object at that point in the picture. (Same as getPixelAt)

    :param picture: the picture you want to get the pixel from
    :param xpos: the x-coordinate of the pixel you want
    :param ypos: the y-coordinate of the pixel you want
    :return:
    """
    return getPixel(picture, xpos, ypos)


# noinspection PyPep8Naming
def getPixels(picture: pictures.RGBImage) -> typing.List[pictures.Pixel]:
    """
    Takes a picture as input and returns the sequence of Pixel objects in the picture.
    :param picture: the picture you want to get the pixels from
    :return: a list of all the pixels in the picture
    """
    if not isinstance(picture, pictures.RGBImage):
        raise TypeError(pictures.type_error_message("getPixels", "pict", "Picture", picture))
    return [pixel for pixel in picture]


# noinspection PyPep8Naming
def getAllPixels(picture: pictures.RGBImage) -> typing.List[pictures.Pixel]:
    """
    Takes a picture as input and returns the sequence of Pixel objects in the picture
    (Same as getPixels)

    :param picture: the picture you want to get the pixels from
    :return: a list of all the pixels in the picture
    """
    return getPixels(picture)


##############################################################################
#
# JES wrapper functions functions for methods of pictures.Picture
#
##############################################################################


# noinspection PyPep8Naming
def makePicture(path: str) -> pictures.Picture:
    """
    Takes a filename as input, reads the file, and creates a picture from it. Returns the picture.

    :param path: the name of the file you want to open as a picture
    :return: a picture object made from the file
    """
    picture: pictures.Picture = pictures.Picture.from_file(path)
    return picture


# noinspection PyPep8Naming
def makeEmptyPicture(width: int, height: int, color: colors.BaseRGB = colors.Colors.white) -> pictures.Picture:
    """
    Makes a new "empty" picture and returns it to you. The width and height must be between 0 and 10000.
    Default color is white.

    :param width: the width of the empty picture
    :param height: height of the empty picture
    :param color: background color of the empty picture (optional)
    :return: a new picture object with all the pixels set to the specified color
    """
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("setAllPixelsToAColor", "color", "Color", color))

    width = int(width)
    if width < 0:
        width = 0
    elif width > 10000:
        width = 10000

    height = int(height)
    if height < 0:
        height = 0
    elif height > 10000:
        height = 10000

    image: pictures.Picture = pictures.Picture.make_empty(width=width, height=height, color=color)
    return image


# noinspection PyPep8Naming
def duplicatePicture(picture: pictures.Picture) -> pictures.Picture:
    """
     Takes a picture as input and returns a new picture object with the same image as the original.

    :param picture: the picture you want to duplicate
    :return: a new picture object with the same image as the original
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("duplicatePicture", "image", "Picture", picture))
    return picture.copy()


##############################################################################
#
# JES wrapper functions functions for methods in module MediaComp.files
#
##############################################################################


# TODO: Add doc string
# noinspection PyPep8Naming
def getMediaPath(file_name: typing.Optional[str] = None):
    """

    :return:
    """
    return files.media_path(file_name)


# TODO: add doc string
# noinspection PyPep8Naming
def setMediaPath(dir_name: typing.Optional[str] = None):
    """

    :param dir_name:
    :return:
    """
    if dir_name is None:
        dir_name = "."
    files.set_media_path(dir_name)

##############################################################################
#
# JES wrapper functions functions for methods of sounds.Sample
#
##############################################################################


# noinspection PyPep8Naming
def getSampleValue(sample: sounds.Sample) -> int:
    """
    Takes a Sample object and returns its value (between -32768 and 32767).

    :param sample: a sample of a sound
    :return: the integer value of that sample
    """
    if not isinstance(sample, sounds.Sample):
        raise TypeError(f'getSampleValue(), expected Sample, got{type(sample)}')
    return sample.value


# noinspection PyPep8Naming
def setSampleValue(sample: sounds.Sample, value: int) -> None:
    """
    Takes a Sample object and a value (should be between -32768 and 32767), and sets the sample to that value.

    :param sample: the sound sample you want to change the value of
    :param value: the value you want to set the sample to
    """
    value = int(value)
    if not isinstance(sample, sounds.Sample):
        raise TypeError(f'setSampleValue(), expected Sample, got{type(sample)}')
    sample.value = value


# noinspection PyPep8Naming
def getSound(sample: sounds.Sample) -> sounds.Sound:
    """
    Takes a Sample object and returns the Sound that it belongs to.

    :param sample: a sample belonging to a sound
    :return: he sound the sample belongs to
    """
    return sample.sound


##############################################################################
#
# JES wrapper functions functions for methods of sounds.Sound
#
##############################################################################


# noinspection PyPep8Naming
def makeSound(path: str) -> sounds.Sound:
    """
    Takes a filename as input, reads the file, and creates a sound from it. Returns the sound.

    :param path: a string path of a wav file
    :return: the sound created from the file at the given path
    """
    return sounds.Sound.from_file(str(path))


# noinspection PyPep8Naming
def makeEmptySound(numSamples: int, samplingRate: float = 22050):
    """
    Takes one or two integers as input. Returns an empty Sound object with the given number of samples
    and (optionally) the given sampling rate. Default rate is 22050 bits/second.

    The resulting sound must not be longer than 600 seconds.
    Prints an error statement if numSamples or samplingRate are less than 0, or if (numSamples/samplingRate) > 600.
    :param numSamples: the number of samples in sound
    :param samplingRate:the number of samples per second of sound (optional)
    :return:  An Empty Sound.
    """
    numSamples = int(numSamples)
    if numSamples < 0:
        raise ValueError
    if numSamples/samplingRate > 600.0:
        raise ValueError
    raise sounds.Sound.make_empty(numSamples, samplingRate)


# noinspection PyPep8Naming
def makeEmptySoundBySeconds(duration: float, samplingRate: float = 22050):
    """
    Takes a floating point number and optionally an integer as input.
    Returns an empty Sound object of the given duration and (optionally) the given sampling rate.

    Default rate is 22050 bits/second. If the given arguments do not multiply to an integer,
    the number of samples is rounded up.

    Prints an error statement if duration or samplingRate are less than 0, or if duration > 600.

    :param duration: the time in seconds for the duration of the sound
    :param samplingRate: the integer value representing the number of samples per second of sound (optional)
    :return: An Empty Sound.
    """
    num_samples = int(duration*samplingRate + 0.5)
    return makeEmptySound(num_samples, samplingRate)


# noinspection PyPep8Naming
def duplicateSound(sound: sounds.Sound) -> sounds.Sound:
    return sound.copy()


# TODO: fix this!!!
def play(sound: sounds.Sound) -> None:
    """
    :param sound:
    :return:
    """
    # noinspection PyProtectedMember
    # IPython.display.display((IPython.display.Audio(sound.samples, rate=int(sound.rate)),))
    raise NotImplemented


# noinspection PyPep8Naming
def getDuration(sound: sounds.Sound) -> float:
    """
    Takes a sound as input and returns the number of seconds that sound lasts.

    :param sound: the sound you want to find the length of (in seconds)
    :return: the number of seconds the sound lasts
    """
    return sound.duration


# noinspection PyPep8Naming
def getSamplingRate(sound: sounds.Sound) -> float:
    """
    Takes a sound as input and returns the number representing the number of samples in each second for the sound.

    :param sound: the sound you want to get the sampling rate from
    :return: the number of samples per second
    """
    return sound.rate


# noinspection PyPep8Naming
def getSamples(sound: sounds.Sound):
    """
    Takes a sound as input and returns the Samples in that sound.

    :param sound: the sound you want to get the samples from
    :return: a list of all the samples in the sound
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError
    return [sample for sample in sound]


# noinspection PyPep8Naming
def getSampleObjectAt(sound: sounds.Sound, index: int) -> sounds.Sample:
    """
    Takes a sound and an index (an integer value), and returns the Sample object at that index

    :param sound: the sound you want to get the sample from
    :param index: the index value of the sample you want to get
    :return: the sample object at that index
    """
    return sounds.Sample(index, sound)


# noinspection PyPep8Naming
def getSampleValueAt(sound: sounds.Sound, index: int) -> int:
    """
    Takes a sound and an index (an integer value), and returns the value of the sample (between -32768 and 32767)
    for that object.

    :param sound: the sound you want to get the sample from
    :param index: the index of the sample you want to get the value of
    :return: the value of the sample (between -32768 and 32767)
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getSampleValueAt(), expected Sound, got{type(sound)}')
    index = int(index)
    return sound[index]


# noinspection PyPep8Naming
def setSampleValueAt(sound: sounds.Sound, index: int, value: int) -> None:
    """
    Takes a sound, an index, and a value (should be between -32768 and 32767),
    and sets the value of the sample at the given index in the given sound to the given value.

    :param sound: the sound you want to change a sample in
    :param index: the index of the sample you want to get the value of
    :param value: the value you want to set the sample to
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'setSampleValueAt(), expected Sound, got{type(sound)}')
    sound[index] = value


# noinspection PyPep8Naming
def getLength(sound: sounds.Sound) -> int:
    """
    Takes a sound as input and returns the number of samples in that sound.

    :param sound: the sound you want to find the length of (how many samples it has)
    :return: the number of samples in sound
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getLength(), expected Sound, got{type(sound)}')
    return sound.length


# noinspection PyPep8Naming
def getNumSamples(sound: sounds.Sound) -> int:
    """
    Takes a sound as input and returns the number of samples in that sound. (Same as getLength)

    :param sound: the sound you want to find the length of (how many samples it has)
    :return:  he number of samples in sound
    """
    return getLength(sound)


# noinspection PyPep8Naming
def writeSoundTo(sound: sounds.Sound, path: str) -> None:
    """
    Takes a sound and a filename (a string) and writes the sound to that file as a WAV file.
    Make sure that the filename ends in '.wav' if you want the operating system to treat it right.)

    :param sound: the sound you want to write out to a file
    :param path : the path to the file you want the picture written to
    :return:
    """
    path = str(path)
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'writeSoundTo(), expected Sound, got{type(sound)}')
    sound.write(path)

##############################################################################
#
# JES wrapper functions functions for methods of turtles.World
#
##############################################################################


# noinspection PyPep8Naming
def makeWorld(width: int = 640, height: int = 480) -> turtles.World:
    """
    Returns a new world of the specified size, where you can put turtles. Default size is 640x480.

    :param width: the width for your new world (optional)
    :param height: he height for your new world (optional)
    :return: the new world

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
    return turtles.World(width, height)


# noinspection PyPep8Naming
def makeTurtle(world: turtles.World) -> turtles.Turtle:
    # TODO edit doc string
    """

    :param world:
    :return:
    """
    if not isinstance(world, turtles.World):
        raise TypeError
    return world.new_turtle()


# noinspection PyPep8Naming
def getTurtleList(world: turtles.World) -> typing.List[turtles.Turtle]:
    """

    :param world:
    :return:
    """

    if not isinstance(world, turtles.World):
        raise TypeError
    return [turtle for turtle in world]

##############################################################################
#
# JES wrapper functions functions for methods of turtles.Turtle
#
##############################################################################


def forward(turtle: turtles.Turtle, d: float = 100.0) -> None:
    """

    :param turtle:
    :param d:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.forward(d)


def backward(turtle: turtles.Turtle, d: float = 100.0) -> None:
    """

    :param turtle:
    :param d:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.forward(-d)


# noinspection PyPep8Naming
def moveTo(turtle: turtles.Turtle, x: float, y: float) -> None:
    """

    :param turtle:
    :param x:
    :param y:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.move_to(x, y)


# noinspection PyPep8Naming
def turnLeft(turtle: turtles.Turtle) -> None:
    """

    :param turtle:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.turn(90.0)


# noinspection PyPep8Naming
def turnRight(turtle: turtles.Turtle) -> None:
    """

    :param turtle:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.turn(-90.0)


def turn(turtle: turtles.Turtle, degrees: float) -> None:
    """

    :param turtle:
    :param degrees:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.turn(degrees)


# noinspection PyPep8Naming
def turnToFace(turtle: turtles.Turtle, x: float, y: float) -> None:
    """

    :param turtle:
    :param x:
    :param y:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.turn_to_face(x, y)


# noinspection PyPep8Naming
def penUp(turtle: turtles.Turtle) -> None:
    """

    :param turtle:
    :return:
    """
    print('in jes.penUp')
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.pen_up = True
    print('leaving jes.penUp')


# noinspection PyPep8Naming
def penDown(turtle: turtles.Turtle) -> None:
    """

    :param turtle:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    turtle.pen_up = False


# noinspection PyPep8Naming
def getHeading(turtle: turtles.Turtle) -> float:
    """

    :param turtle:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    return turtle.heading


# noinspection PyPep8Naming
def getXPos(turtle: turtles.Turtle) -> float:
    """

    :param turtle:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    return turtle.x


# noinspection PyPep8Naming
def getYPos(turtle: turtles.Turtle) -> float:
    """

    :param turtle:
    :return:
    """
    if not isinstance(turtle, turtles.Turtle):
        raise TypeError
    return turtle.y

# Unimplemented functions


# noinspection PyPep8Naming
def getColorWrapAround() -> bool:
    raise NotImplemented("getColorWrapAround() is not implemented in the MediaComp.jes module")


# noinspection PyPep8Naming
def setColorWrapAround(flag: bool) -> None:
    raise NotImplemented("gstColorWrapAround() is not implemented in the MediaComp.jes module")


# noinspection PyPep8Naming
def PickAFile() -> str:
    raise NotImplemented("pickAFile() is not implemented in the MediaComp.jes module")


# TODO: wrap ipywidgets.ColorPicker
# noinspection PyPep8Naming
def PickAColor() -> str:
    raise NotImplemented("pickAColor() is not implemented in the MediaComp.jes module")


# noinspection PyPep8Naming
def blockingPlay(sound: sounds.Sound):
    raise NotImplemented("blockingPlay(sound) is not implemented in the MediaComp.jes module")


# noinspection PyPep8Naming
def stopPlaying(sound: sounds.Sound):
    raise NotImplemented("stopPlaying(sound) is not implemented in the MediaComp.jes module")


# noinspection PyPep8Naming
def makeMovie():
    raise NotImplemented


# noinspection PyPep8Naming
def makeMoveFromInitialFile(filename: str):
    """

    :param filename:
    :return:
    """
    raise NotImplemented


# noinspection PyPep8Naming
def addFrameToMovie(frame, movie):
    """

    :param frame:
    :param movie:
    :return:
    """
    raise NotImplemented


# noinspection PyPep8Naming
def writeFramesToDirectory(movie, directory):
    """

    :param movie:
    :param directory:
    :return:
    """
    raise NotImplemented


# noinspection PyPep8Naming
def playMovie(movie):
    """

    :param movie:
    :return:
    """
    raise NotImplemented


# noinspection PyPep8Naming
def writeAVI(movie, path, framesPerSecond: float = 16.0):
    """

    :param movie:
    :param path:
    :param framesPerSecond:
    :return:
    """
    raise NotImplemented


# noinspection PyPep8Naming
def writeQuicktime(movie, path, framesPerSecond: float = 16):
    """

    :param movie:
    :param path:
    :param framesPerSecond:
    :return:
    """
    raise NotImplemented
