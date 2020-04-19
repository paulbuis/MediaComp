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

from MediaComp.jes.pictures import *
"""

import typing

from .. import colors
from .. import pictures


##############################################################################
#
# JES wrapper functions functions for methods of pictures.PixelInfo
#
# PixelInfo is a subclass of colors.Color
#   (PixelInfo also has x, y coordinates)
# PixelInfo is the superclass of pictures.Pixel
#   (PixelInfo has read-only color properties)
#   Hence, these functions can also be used with Pixel objects
#
##############################################################################


# noinspection PyPep8Naming
def getRed(pixel: pictures.PixelInfo) -> int:
    """
    Takes a Pixel object and returns the value (between 0 and 255)
    of the amount of redness in that pixel.

    :param pixel: the pixel you want to get the amount of red from
    :return: the red value of the pixel
    :rtype: int
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getRed", "pixel",
                                                    "Pixel or PixelInfo",
                                                    pixel))
    return pixel.red


# noinspection PyPep8Naming
def getGreen(pixel: pictures.PixelInfo) -> int:
    """
    Takes a Pixel object and returns the value (between 0 and 255)
    of the amount of greenness in that pixel.

    :param pixel: the pixel you want to get the amount of green from
    :return: the green value of the pixel
    :rtype: int
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getGreen", "pixel",
                                                    "Pixel or PixelInfo",
                                                    pixel))
    return pixel.green


# noinspection PyPep8Naming
def getBlue(pixel: pictures.PixelInfo) -> int:
    """
    Takes a Pixel object and returns the value (between 0 and 255)
    of the amount of blueness in that pixel.

    :param pixel: the pixel you want to get the amount of blue from
    :type pixel: PixelInfo or Color
    :return: the blue value of the pixel
    :rtype: int
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getBlue", "pixel",
                                                    "Pixel or PixelInfo",
                                                    pixel))
    return pixel.blue


# noinspection PyPep8Naming
def getColor(pixel: pictures.PixelInfo) -> colors.Color:
    """
    Takes a Pixel and returns the Color object at that pixel.

    :param pixel: the pixel you want to extract the color from
    :return: the color of the pixel
    :rtype: Color
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getColor", "pixel",
                                                    "Pixel or PixelInfo",
                                                    pixel))
    return pixel.color


# noinspection PyPep8Naming
def getX(pixel: pictures.PixelInfo) -> int:
    """
    Takes in a pixel object and returns the x position of where that
    pixel is in the picture

    Wrapper for :py:attr:`.pictures.Pixel.x` property

    :param pixel: the pixel you want to find the x-coordinate of
    :return: the x-coordinate of the pixel
    :rtype: int
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getX", "pixel",
                                                    "Pixel or PixelInfo",
                                                    pixel))
    return pixel.x


# noinspection PyPep8Naming
def getY(pixel: pictures.PixelInfo) -> int:
    """
    Takes in a pixel object and returns the y position of where that
    pixel is in the picture.

    Wrapper for :py:attr:`.pictures.Pixel.y` property

    :param pixel: the pixel you want to find the y-coordinate of
    :return: the y-coordinate of the pixel
    :rtype: int
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.PixelInfo):
        raise TypeError(pictures.type_error_message("getY", "pixel",
                                                    "Pixel or PixelInfo",
                                                    pixel))
    return pixel.y


##############################################################################
#
# JES wrapper functions functions for methods of pictures.Pixel
#
# Pixel is a subclass of pictures.PixelInfo which is a subclass of colors.Color
#     unlike its superclasses, its color can be changed which changes
#     the underlying pictures.Picture object
#
##############################################################################


# noinspection PyPep8Naming
def setColor(pixel: pictures.Pixel, color: colors.Color) -> None:
    """
    Takes in a pixel and a color, and sets the pixel to the given color.

    Wrapper for an assignment to :py:attr:`.pictures.Pixel.color` property

    :param Pixel pixel: the pixel you want to set the color of
    :param Color color: the color you want to set the pixel to
    :raises TypeError: if either ``pixel`` is not a
        :py:class:`~.pictures.Pixel` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setColor", "pixel",
                                                    "Pixel", pixel))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("setColor", "color",
                                                    "Color", color))
    pixel.color = color


# noinspection PyPep8Naming
def setRed(pixel: pictures.Pixel, redValue: int) -> None:
    """
    Takes in a Pixel object and a value (between 0 and 255) and sets the
    redness of that pixel to the given value.

    Wrapper for an assignment to :py:attr:`.pictures.Pixel.red` property

    :param Pixel pixel: the pixel you want to set the red value of
    :param int redValue: a number (0 - 255) for the new red value of the pixel
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setRed", "pixel",
                                                    "Pixel", pixel))
    pixel.red = redValue


# noinspection PyPep8Naming
def setGreen(pixel: pictures.Pixel, greenValue: int) -> None:
    """
    Takes in a Pixel object and a value (between 0 and 255) and sets the
    greenness of that pixel to the given value.

    Wrapper for an assignment to :py:attr:`.pictures.Pixel.green` property

    :param Pixel pixel: the pixel you want to set the green value of
    :param int greenValue: a number (0 - 255) for the new green value
        of the pixel
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setGreen",
                                                    "pixel", "Pixel", pixel))
    pixel.green = greenValue


# noinspection PyPep8Naming
def setBlue(pixel: pictures.Pixel, blueValue: int) -> None:
    """
    Takes in a Pixel object and a value (between 0 and 255) and sets the
    blueness of that pixel to the given value.

    Wrapper for an assignment to :py:attr:`.pictures.Pixel.blue` property

    :param pixel: the pixel you want to set the blue value of
    :param blueValue: a number (0 - 255) for the new blue value of the pixel
    :raises TypeError: if ``pixel`` is not a :py:class:`~.pictures.Pixel`
    """
    if not isinstance(pixel, pictures.Pixel):
        raise TypeError(pictures.type_error_message("setBlue", "pixel",
                                                    "Pixel", pixel))
    pixel.blue = blueValue


##############################################################################
#
# JES wrapper functions functions for methods of pictures.TextStyle
#
##############################################################################


# noinspection PyPep8Naming
def makeStyle(fontName: str, emphasis: str, size: float) -> pictures.TextStyle:
    """
    Takes a font name, emphasis, and size in points as input.
    Returns a Font object with the given parameters.

    :param fontName: the name of the font you want in the style
        (sansSerif, serif, mono)
    :param emphasis: the type of emphasis you want in the style
        (italic, bold, italic + bold, plain)
    :param size: the size of the font you want in the style
    :rtype: pictures.TextStyle
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
           color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, (x,y) coordinates, width, height, two integer angles,
    and (optionally) a color as input.
    Adds an outline of an arc starting at (x,y) at an initial angle of "start"
    with the given width and height.
    The angle of the arc itself is "angle", which is relative to "start."
    Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_arc` method.

    :param pictures.Picture picture: the picture you want to draw the arc on
    :param int startX: the x-coordinate of the center of the arc
    :param int startY: the y-coordinate of the center of the arc
    :param int width: the width of the arc
    :param int height: the height of the arc
    :param float start: the start angle of the arc in degrees
    :param float angle: the angle of the arc relative to start in degrees
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addArc", "picture",
                                                    "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArc", "color",
                                                    "Color", color))
    picture.add_arc(startX, startY, width, height, start, angle, color)


# noinspection PyPep8Naming
def addArcFilled(picture: pictures.PILImage, startX: int, startY: int,
                 width: int, height: int,
                 start: float, angle: float,
                 color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, (x,y) coordinates, width, height, two integer angles,
    and (optionally) a color as input.
    Adds an o filled arc starting at (x,y) at an initial angle of "start"
    with the given width and height.
    The angle of the arc itself is "angle", which is relative to "start."
    Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_arc_filled` method.

    :param pictures.Picture picture: the picture you want to draw the arc on
    :param int startX: the x-coordinate of the center of the arc
    :param int startY: the y-coordinate of the center of the arc
    :param int width: the width of the arc
    :param int height: the height of the arc
    :param float start: the start angle of the arc in degrees
    :param float angle: the angle of the arc relative to start in degrees
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addArcFilled", "picture",
                                                    "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addArcFilled", "color",
                                                    "Color", color))
    picture.add_arc_filled(startX, startY, width, height, start, angle, color)


# noinspection PyPep8Naming
def addLine(picture: pictures.Picture, startX: int, startY: int,
            endX: int, endY: int,
            color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers),
    and an ending (x, y) position, two more numbers, four total),
    and (optionally) a color as input.

    Adds a line from the starting point to the ending point in the picture.
    Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_line` method.

    :param pictures.Picture picture: the picture you want to draw the line on
    :param int startX: the x position you want the line to start
    :param int startY: the y position you want the line to start
    :param int endX: the x position you want the line to end
    :param int endY: the y position you want the line to end
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("addLine", "picture",
                                                    "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addLine", "color",
                                                    "Color", color))
    picture.add_line(startX, startY, endX, endY, color)


# noinspection PyPep8Naming
def addOval(picture: pictures.Picture, startX: int, startY: int, width: int, height: int,
            color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input.
    Adds an oval outline of the given dimensions using the (x,y) as
    the upper left corner of the bounding rectangle.
    Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_oval` method.

    :param pictures.Picture picture: the picture you want to draw the
        rectangle on
    :param int startX: the x-coordinate of the upper left-hand corner
        of the bounding rectangle of the oval
    :param int startY: the y-coordinate of the upper left-hand corner
        of the bounding rectangle of the oval
    :param int width: the width of the oval
    :param int height: the height of the oval
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addOval", "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addOval", "color", "Color", color))
    picture.add_oval(startX, startY, height, width, color)


# noinspection PyPep8Naming
def addOvalFilled(picture: pictures.PILImage, startX: int, startY: int,
                  width: int, height: int, color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input. Adds a filled oval outline
    of the given dimensions using the (x,y) as the upper
    left corner of the bounding rectangle.
    Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_oval_filled` method.

    :param pictures.Picture picture: the picture you want to draw the
        rectangle on
    :param int startX: the x-coordinate of the upper left-hand corner of
        the bounding rectangle of the oval
    :param int startY: the y-coordinate of the upper left-hand corner of
        the bounding rectangle of the oval
    :param int width: the width of the oval
    :param int height: the height of the oval
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addOvalFilled",
                                                    "picture", "Picture",
                                                    picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addOvalFilled",
                                                    "color", "Color", color))
    picture.add_oval_filled(startX, startY, height, width, color)


# noinspection PyPep8Naming
def addRect(picture: pictures.Picture, startX: int, startY: int,
            width: int, height: int,
            color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input. Adds a rectangular outline of the
    specified dimensions using the (x,y) as the upper left corner.
    Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_rect` method.

    :param pictures.Picture picture: the picture you want to draw the
        rectangle on
    :param int startX: the x-coordinate of the upper left-hand corner of
        the rectangle
    :param int startY: the y-coordinate of the upper left-hand corner of
        the rectangle
    :param int width: the width of the rectangle
    :param int height: the height of the rectangle
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addRect", "picture",
                                                    "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addRect", "color",
                                                    "Color", color))
    picture.add_oval_filled(startX, startY, height, width, color)


# noinspection PyPep8Naming
def addRectFilled(picture: pictures.PILImage, startX: int, startY: int,
                  width: int, height: int,
                  color: colors.Color = colors.Colors.black) -> None:
    """
    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input.
    Adds a filled rectangle of the specified dimensions using the (x,y) as the
    upper left corner. Default color is black.

    Wrapper for :py:meth:`.pictures.Picture.add_rect_filled` method.

    :param pictures.Picture picture: the picture you want to draw the
        rectangle on
    :param int startX: the x-coordinate of the upper left-hand corner of
        the rectangle
    :param int startY: the y-coordinate of the upper left-hand corner of
        the rectangle
    :param int width: the width of the rectangle
    :param int height: the height of the rectangle
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addRectFilled", "picture",
                                                    "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addRectFilled",
                                                    "color", "Color", color))
    picture.add_line(startX, startY, width, height, color)


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def addText(picture: pictures.Picture, xpos: int, ypos: int, text: str,
            color=colors.Colors.black) -> None:
    """
    Takes a picture, an x position and a y position (two numbers),
    and some text as a string, which will get drawn into the picture,
    in the specified color. Default is black.

    Wrapper for :py:meth:`.pictures.Picture.add_text` method.

    :param pictures.Picture picture: the picture you want to draw the
        rectangle on
    :param int xpos: the x-coordinate where you want to start writing the text
    :param int ypos: the x-coordinate where you want to start writing the text
    :param str text: string containing the text you want written
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not a
        :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addText", "picture",
                                                    "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addText", "color",
                                                    "Color", color))
    picture.add_text(xpos, ypos, text, color)


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def addTextWithStyle(picture: pictures.Picture, xpos: int, ypos: int,
                     text: str, style: str,
                     color=colors.Colors.black) -> None:
    """
    Takes a picture, an x position and a y position (two numbers),
    and some text as a string, which will get drawn into the picture,
    in the given font style and specified color. Default is black.

    Wrapper for :py:meth:`.pictures.Picture.add_text_with_style` method.

    :param pictures.Picture picture: the picture you want to draw the
        rectangle on
    :param int xpos: the x-coordinate where you want to start writing the text
    :param int ypos: the y-coordinate where you want to start writing the text
    :param str text: string containing the text you want written
    :param str style: the font style you want to draw in (See makeStyle)
    :param colors.Color color: the color you want to draw in (optional)
    :raises TypeError: if either ``picture`` is not a
        :py:class:`~.pictures.Picture` or if ``color`` is not
        a :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("addTextWithStyle",
                                                    "picture", "Picture",
                                                    picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("addTextWithStyle",
                                                    "color", "Color", color))
    text_style = pictures.TextStyle(style, "", 10)  # TODO: fix this !
    picture.add_text_with_style(xpos, ypos, text, text_style, color)


# TODO: implement this
# display will embed in HTML via JesImage._repr_html_ method
def show(picture: pictures.Picture) -> None:
    """
    Shows the picture provided as input.
    :param pictures.Picture picture: the picture you want to see
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("show", "picture",
                                                    "Picture", picture))
    # function display is in imported module IPython.core.display
    # probably will trigger type checker warning, display is heavily overloaded
    # IPython.core.display.display(picture)
    raise NotImplementedError


# just alias show() since we aren't interactive
def repaint(picture: pictures.Picture) -> None:
    """
    Write better docstring
    :param pictures.Picture picture:
    """
    show(picture)


# noinspection PyPep8Naming
def copyInto(smallPicture: pictures.PILImage, bigPicture: pictures.PILImage,
             startX: int, startY: int) -> None:
    """
    Takes two pictures, a x position and a y position as input, and modifies
    bigPicture by copying into it as much of smallPicture as will fit,
    starting at the x,y position in the destination picture.

    Wrapper for :py:meth:`.pictures.Picture.copy_into` method.

    :param pictures.Picture smallPicture: the picture to paste into the
        big picture
    :param pictures.Picture bigPicture: the picture to be modified
    :param int startX: the X coordinate of where to place the small picture
        on the big one
    :param int startY: the Y coordinate of where to place the small picture
        on the big one
    :raises TypeError: if either ``smallPicture`` or ``bigPicture`` is
        not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(smallPicture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("copyInto", "smallPicture",
                                                    "Picture", smallPicture))
    if not isinstance(bigPicture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("copyInto", "bigPicture",
                                                    "Picture", bigPicture))
    startX = int(startX)
    startY = int(startY)
    bigPicture.copy_into(smallPicture, startX, startY)


# noinspection PyPep8Naming
def writePictureTo(picture: pictures.Picture, path: str) -> None:
    """
    Takes a picture and a file name (string) as input, then writes the
    picture to the file as a JPEG, PNG, or BMP.
    (Be sure to end the filename in ".jpg" or ".png" or ".bmp" for the
    operating system to understand it well.)

    Wrapper for :py:meth:`.pictures.Picture.save` method

    :param pictures.Picture picture: the picture you want to be written
        out to a file
    :param str path: the path to the file you want the picture written to
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("writePictureTo",
                                                    "picture", "Picture",
                                                    picture))
    picture.save(path)


# noinspection PyPep8Naming
def getHeight(picture: pictures.PILImage) -> int:
    """
    Takes a picture as input and returns its length in the number of
    pixels yop-to-bottom in the picture.

    Wrapper for :py:attr:`.pictures.Picture.height` property.

    :param Picture picture: the picture you want to get the height of
    :return: the height of the picture
    :rtype: int
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("getHeight", "picture",
                                                    "Picture", picture))
    return picture.height


# noinspection PyPep8Naming
def getWidth(picture: pictures.PILImage) -> int:
    """
    Takes a picture as input and returns its length in the number of
    pixels left-to-right in the picture.

    Wrapper for :py:attr:`.pictures.Picture.width` property.

    :param Picture picture: the picture you want to get the width of
    :return: the width of the picture
    :rtype: int
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(picture, pictures.PILImage):
        raise TypeError(pictures.type_error_message("getWidth", "picture",
                                                    "Picture", picture))
    return picture.width


# noinspection PyPep8Naming
def setAllPixelsToAColor(picture: pictures.Picture,
                         color: colors.Color = colors.Colors.black) -> None:
    """
    Modifies the whole image so that every pixel in that image is
    the given color.

    Wrapper for :py:meth:`.pictures.Picture.set_color` method.

    :param pictures.Picture picture: the picture to change the pixels of
    :param colors.Color color: the color to set each pixel to
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
        or if ``color`` is not a :py:class:`~.colors.Color`
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("setAllPixelsToAColor",
                                                    "picture", "Picture", picture))
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("setAllPixelsToAColor",
                                                    "color", "Color", color))
    picture.set_color(color)


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def getPixel(picture: pictures.Picture, xpos: int, ypos: int) -> pictures.Pixel:
    """
    Takes a picture, an x position and a y position (two numbers), and
    returns the Pixel object at that point in the picture.
    (Same as getPixelAt)

    :param pictures.Picture picture: the picture you want to get the pixel from
    :param int xpos: the x-coordinate of the pixel you want
    :param int ypos: the y-coordinate of the pixel you want
    :return: the Pixel object at the x,y position in the picture.
    :rtype: pictures.Pixel
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("getPixel", "picture", "Picture", picture))
    return picture[xpos, ypos]


# noinspection SpellCheckingInspection
# noinspection PyPep8Naming
def getPixelAt(picture: pictures.Picture, xpos: int, ypos: int) -> pictures.Pixel:
    """
    Takes a picture, an x position and a y position (two numbers),
    and returns the Pixel object at that point in the picture.
    (Same as getPixelAt)

    :param pictures.Picture picture: the picture you want to get
        the pixel from
    :param int xpos: the x-coordinate of the pixel you want
    :param int ypos: the y-coordinate of the pixel you want
    :return: the Pixel object at the x,y position in the picture
    :rtype: pictures.Pixel
    """
    return getPixel(picture, xpos, ypos)


# noinspection PyPep8Naming
def getPixels(picture: pictures.Picture) -> typing.List[pictures.Pixel]:
    """
    Takes a picture as input and returns the sequence of Pixel objects
    in the picture.

    :param pictures.Picture picture: the picture you want to get the
            pixels from
    :return: a list of all the pixels in the picture
    :rtype: list[pictures.Pixel]
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("getPixels", "picture",
                                                    "Picture", picture))
    return list(picture)


# noinspection PyPep8Naming
def getAllPixels(picture: pictures.Picture) -> typing.List[pictures.Pixel]:
    """
    Takes a picture as input and returns the sequence of Pixel objects
    in the picture (Same as getPixels)

    :param pictures.Picture picture: the picture you want to get the
        pixels from
    :return: a list of all the pixels in the picture
    :rtype: list[pictures.Pixel]
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
    Takes a filename as input, reads the file, and creates a picture from it.
    Returns the picture.

    Wrapper for :py:meth:`pictures.Picture.from_file` class method

    :param str path: the name of the file you want to open as a picture
    :return: a picture object made from the file
    :rtype: pictures.Picture
    """
    picture: pictures.Picture = pictures.Picture.from_file(path)
    return picture


# noinspection PyPep8Naming
def makeEmptyPicture(width: int, height: int,
                     color: colors.Color = colors.Colors.white) -> pictures.Picture:
    """
    Makes a new "empty" picture and returns it to you.
    The width and height must be between 0 and 10000.
    Default color is white.

    Wrapper for :py:meth:`.pictures.Picture.make_empty` class method

    :param int width: the width of the empty picture
    :param int height: height of the empty picture
    :param color.Colors color: background color of the empty
            picture (optional)
    :return: a new picture object with all the pixels set to the
            specified color
    :rtype: pictures.Picture
    :raises TypeError: if ``color`` is not a :py:class:`~.colors.Color`
    """
    if not isinstance(color, colors.BaseRGB):
        raise TypeError(pictures.type_error_message("setAllPixelsToAColor",
                                                    "color", "Color", color))

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

    image: pictures.Picture = pictures.Picture.make_empty(width=width,
                                                          height=height,
                                                          color=color)
    return image


# noinspection PyPep8Naming
def duplicatePicture(picture: pictures.Picture) -> pictures.Picture:
    """
    Takes a picture as input and returns a new picture object with the
    same image as the original.

    Wrapper for :py:meth:`.pictures.Picture.copy` method.

    :param picture: the picture you want to duplicate
    :return: a new picture object with the same image as the original
    :rtype: pictures.Picture
    :raises TypeError: if ``picture`` is not a :py:class:`~.pictures.Picture`
    """
    if not isinstance(picture, pictures.Picture):
        raise TypeError(pictures.type_error_message("duplicatePicture",
                                                    "picture", "Picture",
                                                    picture))
    return picture.copy()
