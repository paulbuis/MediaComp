#
# Package: MediaComp
# Module: pictures
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies, sounds) from
# http://mediacomputation.org created by Mark Guzdial and Barbara Ericson
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/).
"""
Module docstring goes here!
"""
# module base64 is standard in Python 3: https://docs.python.org/3/library/base64.html
# using base64.b64encode in Picture.to_base64
import base64

# module io is standard in Python 3: https://docs.python.org/3/library/io.html
# using io.BytesIO in Picture.to_base64
import io

import os

import pathlib

import collections.abc


# module typing is standard in Python 3.5+: https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton code: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type, doesn't mean
# that at runtime it will actually be of that type: dynamic checking or casting/conversion
# still needs to be done
import typing

# PIL refers to the Pillow library installed by default in the Anaconda distribution of Python
# PIL is the Python Image Library, Pillow is a fork of PIL
# For documentation on Pillow, see: https://pillow.readthedocs.io/en/stable/

# suppress static type checker complain "error: No library stub file for module 'PIL.Image'"
import PIL.Image  # type: ignore
# suppress static type checker complain "error: No library stub file for module 'PIL.ImageDraw'"
import PIL.ImageDraw  # type: ignore
# suppress static type checker complain "error: No library stub file for module 'PIL.ImageFont'"
import PIL.ImageFont  # type: ignore
# suppress static type checker complain "error: No library stub file for module 'PIL.PyAccess'"
from PIL.PyAccess import PyAccess as PixelAccess  # type: ignore

# suppress static type checker complain "error: No library stub file for
# module 'matplotlob.font_manager'"
# suppress static type checker complain "error: No library stub file for module 'matplotlob'"
import matplotlib.font_manager  # type: ignore

# The IPython.core.display module is specific to IPython which is used in Jupyter
# See https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html
# import IPython.core.display

# import the color and file modules in this package
from . import colors
from . import files

# make the names in the color and file modules public to
# consumers of this module so they don't have to import colors module also
Colors = colors.Colors
Color = colors.Color


def set_media_path(path: typing.Optional[str] = None) -> bool:
    """
    forwards to files.set_media_path so module that imports this module
    does not have to import files module also

    :param path:
    :return:
    :rtype bool:
    """
    return files.set_media_path(path)


def media_path(filename: typing.Optional[str]) -> pathlib.Path:
    """
    forwards to files.media_path so module that imports this module
    does not have to import files module also

    :param Optional[str] filename:
    :return:
    :rtype pathlib.Path:
    """
    return files.media_path(filename)


# Type aliases
RGB = typing.Tuple[int, int, int]
ImageSize = typing.Tuple[int, int]
Point = typing.Tuple[int, int]
PointSequence = typing.Sequence[Point]
BaseRGB = colors.BaseRGB
PixelInfoTuple = typing.Tuple[Point, RGB]
Transform = typing.Callable[['PixelInfo'], Color]
Transform2 = typing.Callable[[PixelInfoTuple], PixelInfoTuple]
Predicate = typing.Callable[['PixelInfo'], bool]
Combine = typing.Callable[['PixelInfo', 'PixelInfo'], Color]


def type_error_message(fun_name: str, param_name: str, expected: str, actual: typing.Any) -> str:
    """ generates error message for TypeError """
    return f"In MediaComp.pictures.{fun_name}: {param_name} " +\
           f"expected a {expected}, actually {type(actual)}"


class PixelInfo(colors.Color):
    """
    Class level docstring goes here
    """

    def __init__(self, xy: Point, rgb: typing.Optional[RGB] = None):
        super().__init__(rgb=rgb)
        self._xy: Point = (int(xy[0]), int(xy[1]))

    # Overrides Color.__repr__
    def __repr__(self) -> str:
        return f"PixelInfo(xy = ({self.x}, {self.y}), " + \
               f"pixel_color = Color(red={self.red}, green={self.green}, blue={self.blue}))"

    # Overrides Color.__str__
    def __str__(self) -> str:
        return f"Pixel(red={self.red}, green={self.green}, " + \
               f"blue={self.blue}, x={self.x}, y={self.y})"

    @property
    def color(self) -> colors.Color:
        """
        Write better docstring

        :type: colors.Color
        """
        rgb: RGB = self.rgb
        return colors.Color(rgb[0], rgb[1], rgb[2])

    @property
    def x(self) -> int:  # pylint: disable=invalid-name
        """
        Write better docstring

        :type: int
        """
        return int(self._xy[0])

    @property
    def y(self) -> int:  # pylint: disable=invalid-name
        """
        Write better docstring

        :type: int
        """
        return int(self._xy[1])


class Pixel(PixelInfo):
    """
    Class level docstring goes here
    """

    def __init__(self, xy: Point, pixel_access: PixelAccess):
        self.__pixel_access: PixelAccess = pixel_access
        super().__init__(xy)

    # Overrides PixelInfo.__str__ method
    def __str__(self) -> str:
        return f"Pixel(xy=({self.x}, {self.y}), Color(r={self.red}, g={self.green}, b={self.blue}))"

    @property
    def color(self) -> colors.Color:
        """
        Write better docstring

        :type: colors.Color
        """
        rgb: RGB = self.__pixel_access[self._xy]
        return colors.Color(rgb[0], rgb[1], rgb[2])

    @color.setter
    def color(self, rgb: colors.BaseRGB) -> None:
        if not isinstance(rgb, colors.BaseRGB):
            raise TypeError
        self.rgb = rgb.rgb

    # Overrides BaseRGB.red property getter
    @property
    def red(self) -> int:
        """
        Write better docstring

        :type: int
        """
        return self.rgb[0]

    @red.setter
    def red(self, value: int) -> None:
        value = min(255, max(0, int(value)))
        rgb: RGB = self.__pixel_access[self._xy]
        self.__pixel_access[self._xy] = (value, rgb[1], rgb[2])

    # Overrides BaseRGB.green property getter
    @property
    def green(self) -> int:
        """
        Write better docstring
        :type: int
        """
        return self.rgb[1]

    @green.setter
    def green(self, value: int) -> None:
        value = min(255, max(0, int(value)))
        rgb: RGB = self.__pixel_access[self._xy]
        self.__pixel_access[self._xy] = (rgb[0], value, rgb[2])

    # Overrides BaseRGB.blue property getter
    @property
    def blue(self) -> int:
        """
        Write better docstring

        :type: int
        """
        return self.rgb[2]

    @blue.setter
    def blue(self, value: int) -> None:
        value = min(255, max(0, int(value)))
        rgb: RGB = self.__pixel_access[self._xy]
        self.__pixel_access[self._xy] = (rgb[0], rgb[1], value)

    # Overrides BaseRGB.rgb property getter
    @property
    def rgb(self) -> RGB:
        """
        Write better docstring

        :type: RGB
        """
        rgb: RGB = self.__pixel_access[self._xy]
        return int(rgb[0]), int(rgb[1]), int(rgb[2])

    @rgb.setter
    def rgb(self, value: RGB) -> None:
        self.__pixel_access[self._xy] = value


class TextStyle:
    """
    Class-level docstring goes here
    """

    @staticmethod
    def find_font_file(query: str) -> typing.Optional[str]:
        """
        Write better docstring

        :param str query:
        :return:
        """
        matches = list(filter(lambda path: query in os.path.basename(path),
                              matplotlib.font_manager.findSystemFonts()))
        if len(matches) == 0:
            return None
        return matches[0]

    def __init__(self, font_name: str, emphasis: str, size: float):
        """
        Write better docstring

        :param font_name:
        :param emphasis:
        :param size:
        """
        self.__font_name = str(font_name)
        font_file: typing.Optional[str] = TextStyle.find_font_file(self.__font_name)
        # TODO: emphasis still ignored in font searching
        self.__emphasis = str(emphasis)
        self.__size = float(size)
        self.__font: PIL.ImageFont.ImageFont = PIL.ImageFont.truetype(font_file, self.__size)

    @property
    def font_name(self) -> str:
        """
        name of font used to draw with

        :type: str
        """
        return self.__font_name

    @property
    def font(self) -> PIL.ImageFont.ImageFont:
        """
        Write better docstring

        :type: PIL.ImageFont.ImageFont
        """
        return self.__font

    @property
    def emphasis(self) -> str:
        """
        kind of emphasis to use, 'bold', 'italic', 'bold + italic'

        :type: str
        """
        return self.__emphasis

    @property
    def size(self) -> float:
        """
        size of font in points

        :type: float
        """
        return self.__size


# class PILImage has no pixel-level operations and is agnostic about how many and what kind
# of channels are in the image. Such things will be found in subclasseses of PILImage
class PILImage:
    """
    Class level docstring
    """
    def __init__(self, pil_image: PIL.Image.Image):
        self._pil_image = pil_image

    @property
    def height(self) -> int:
        """
        height of image in pixels

        :type: int
        """
        image_height = self._pil_image.height
        return int(image_height)

    @property
    def width(self) -> int:
        """
        width of image in pixels

        :type: int
        """
        image_width = self._pil_image.width
        return int(image_width)

    @property
    def size(self) -> ImageSize:
        """
        (height, width) tuple

        :type: ImageSize
        """
        return self.height, self.width

    # overriden by Picture subclass
    def copy(self) -> 'PILImage':
        """
        Makes a deep copy of this object

        :return: the copy
        :rtype PILImage:
        """
        return PILImage(self._pil_image.copy())

    def set_color(self, color: colors.BaseRGB = colors.Colors.black):
        """
        Write better docstring

        :param color:
        :return:
        """
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.rectangle([(0, 0), (self.width, self.height)], fill=color)

    def copy_into(self, big_picture: 'PILImage', left: int, top: int):
        """
        Write better docstring

        :param big_picture:
        :param int left:
        :param int top:
        :return:
        """
        big_picture._pil_image.paste(self._pil_image, (left, top))  # pylint: disable=protected-access

    def add_arc(self, x: int, y: int,  # pylint: disable=invalid-name;  # pylint: disable=too-many-arguments
                width: int, height: int,
                start: float, angle: float,
                color: colors.BaseRGB = colors.Colors.black
                ) -> None:
        """
        Write better docstring

        :param int x:
        :param int y:
        :param int width:
        :param int height:
        :param float start:
        :param float angle:
        :param colors.Color color:
        :raises TypeError:
        """
        x = int(x)  # pylint: disable=invalid-name
        y = int(y)  # pylint: disable=invalid-name
        width = int(width)
        height = int(height)
        start = float(start)
        angle = float(angle)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_arc", "c", "Color", color))

        fill_color: RGB = color.rgb
        draw = PIL.ImageDraw.Draw(self._pil_image)
        bounding_box: PointSequence = [(x, y), (x + width, y + height)]
        draw.arc(bounding_box, start=start, end=start+angle, fill=fill_color, width=1)

    def add_arc_filled(self, x: int, y: int,  # pylint: disable=invalid-name;  # pylint: disable=too-many-arguments
                       width: int, height: int,
                       start: float, angle: float,
                       color: colors.BaseRGB = colors.Colors.black
                       ) -> None:
        """
        Write better docstring

        :param int x:
        :param int y:
        :param int width:
        :param int height:
        :param float start:
        :param float angle:
        :param colors.Color color:
        :raises TypeError:
        """
        x = int(x)  # pylint: disable=invalid-name
        y = int(y)  # pylint: disable=invalid-name
        width = int(width)
        height = int(height)
        start = float(start)
        angle = float(angle)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_arc_filled", "color", "Color", color))
        fill_color: RGB = color.rgb
        bounding_box: PointSequence = [(x, y), (x + width, y + height)]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.pieslice(bounding_box, start=start, end=start+angle, fill=fill_color, width=1)

    def add_line(self, start_x: int, start_y: int,  # pylint: disable=too-many-arguments
                 width: int, height: int,
                 color: colors.BaseRGB = colors.Colors.black
                 ) -> None:
        """
        Write better docstring

        :param int start_x:
        :param int start_y:
        :param int width:
        :param int height:
        :param colors.Color color:
        :raises TypeError:
        """
        start_x = int(start_x)
        start_y = int(start_y)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_line", "color", "Color", color))
        bounding_box: PointSequence = [(start_x, start_y), (start_x + width, start_y + height)]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.line(bounding_box, fill=color.rgb, width=1)

    def add_oval(self, center_x: int, center_y: int,  # pylint: disable=too-many-arguments
                 width: int, height: int,
                 color: colors.BaseRGB = colors.Colors.black
                 ) -> None:
        """
        Write better docstring
        :param int center_x:
        :param int center_y:
        :param int width:
        :param int height:
        :param colors.Color color:
        :raises TypeError:
        """
        center_x = int(center_x)
        center_y = int(center_y)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_oval", "color", "Color", color))
        bounding_box: PointSequence = [(center_x, center_y), (center_x + width, center_y + height)]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.ellipse(bounding_box, outline=color.rgb, width=1)

    def add_oval_filled(self, center_x: int, center_y: int,  # pylint: disable=too-many-arguments
                        width: int, height: int,
                        color: colors.BaseRGB = colors.Colors.black
                        ) -> None:
        """
        Write better docstring

        :param int center_x:
        :param int center_y:
        :param int width:
        :param int height:
        :param colors.Color color:
        :raises TypeError:
        """
        center_x = int(center_x)
        center_y = int(center_y)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_oval_filled", "color", "Color", color))
        left_top = (center_x - width//2, center_y - height//2)
        right_bottom = (center_x + width//2, center_y + width//2)
        bounding_box = [left_top, right_bottom]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.ellipse(bounding_box, outline=color.rgb, fill=color.rgb, width=1)

    def add_rect(self, left: int, top: int,  # pylint: disable=too-many-arguments
                 width: int, height: int,
                 color: colors.BaseRGB = colors.Colors.black
                 ) -> None:
        """
        Takes a picture, a starting (left, top) position (two numbers),
        a width and height (two more numbers, four total),
        and (optionally) a color as input. Adds a rectangular outline of the
        specified dimensions using the (left,top) as the upper left corner.
        Default color is black.

        Wrapped by for :py:func:`.jes.addRect` function.

        :param int left:
        :param int top:
        :param int width:
        :param int height:
        :param colors.Color color:
        :raises TypeError:
        """
        left = int(left)
        top = int(top)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_rect", "color", "Color", color))
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.rectangle([(left, top), (left + width, top + height)], outline=color.rgb, width=1)

    def add_rect_filled(self, left: int, top: int, width: int, height: int,  # pylint: disable=too-many-arguments
                        color: colors.BaseRGB = colors.Colors.black
                        ) -> None:
        """
        Write better docstring

        :param int left:
        :param int top:
        :param int width:
        :param int height:
        :param colors.Color color:
        :raises TypeError:
        """
        left = int(left)
        top = int(top)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_rect_filled", "color", "Color", color))
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.rectangle([(left, top), (left+width, top+height)], fill=color.rgb, width=1)

    def add_text(self, x_pos: int, y_pos: int, text: str,
                 color: colors.BaseRGB = colors.Colors.black
                 ) -> None:
        """
        Write better docstring

        :param int x_pos:
        :param int y_pos:
        :param str text:
        :param colors.Color color:
        :raises TypeError
        """
        x_pos = int(x_pos)
        y_pos = int(y_pos)
        text = str(text)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_text", "color", "Color", color))
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.text((x_pos, y_pos), text, fill=color.rgb)

    def add_text_with_style(self, x_pos: int, y_pos: int,  # pylint: disable=too-many-arguments
                            text: str, style: TextStyle,
                            color: colors.BaseRGB = colors.Colors.black
                            ) -> None:
        """
        Write better docstring

        :param int x_pos:
        :param int y_pos:
        :param str text:
        :param str style:
        :param colors.Color color:
        :raises TypeError:
        """
        x_pos = int(x_pos)
        y_pos = int(y_pos)
        text = str(text)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_text_styled",
                                               "color", "Color", color))
        if not isinstance(style, TextStyle):
            raise TypeError(type_error_message("PILImage.add_text_styled",
                                               "style",
                                               "TextStyle", style))
        draw: PIL.ImageDraw.ImageDraw = PIL.ImageDraw.Draw(self._pil_image)
        draw.text((x_pos, y_pos), text, font=style.font, fill=color.rgb)


#
# Picture operates on files containing RGB images
#
# All interactions with the filesystem should be here
# not in superclasses
#
# class Picture adds pixel-level operations to PILImage
# and works only with 3-channel 8-bit/channel images
#
class Picture(PILImage, collections.abc.Iterable):
    """
    Class-level docstrings
    """
    def __init__(self, pil_image: PIL.Image.Image):
        if pil_image.mode == "RGB":
            super().__init__(pil_image)
        else:
            super().__init__(pil_image.convert(mode="RGB"))
        self.__pixel_access: PIL.PyAccess.PyAccess = self._pil_image.load()

    @classmethod
    def from_file(cls, filename: typing.Union[str, os.PathLike]) -> 'Picture':
        """
        Write better docstring

        :param filename:
        :return:
        :rtype: Picture
        """
        if not isinstance(filename, os.PathLike):
            filename = files.media_path(str(filename))
        img = PIL.Image.open(filename)
        img.load()
        return cls(img)

    @classmethod
    def make_empty(cls, width: int, height: int,
                   color: colors.BaseRGB = colors.Colors.black) -> 'Picture':
        """
        Write better docstring

        :param int width:
        :param int height:
        :param colors.Color color:
        :return:
        :rtype: Picture
        """
        height = int(height)
        width = int(width)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("setAllPixelsToAColor", "color", "Color", color))
        return cls(PIL.Image.new("RGB", (width, height), color.rgb))

    def __str__(self) -> str:
        return "<image> size:" + str(self.size)

    def _repr_html_(self) -> str:
        return '<img src="' + self.to_base64() + '" />'

    # TODO: fix it so it uses IPython display mechanism for PNG rather than HTML
    # def _repr_png_(self):
    #    pass

    def __getitem__(self, key: Point) -> Pixel:
        index_x = int(key[0])
        index_y = int(key[1])

        if index_x >= self.width:
            index_x = self.width - 1
        if index_y >= self.height:
            index_y = self.height - 1
        if index_x < 0:
            index_x = 0
        if index_y < 0:
            index_y = 0
        return Pixel((index_x, index_y), self.__pixel_access)

    def __setitem__(self, key: Point, value: colors.BaseRGB) -> None:
        index_x = int(key[0])  # pylint: disable=invalid-name
        index_y = int(key[1])  # pylint: disable=invalid-name

        # silently discard value if out of range, is that really a good thing?
        if index_x < 0 or index_x >= self.width:
            return
        if index_y < 0 or index_y >= self.height:
            return

        if not isinstance(value, colors.BaseRGB):
            raise TypeError(type_error_message("Picture.setitem", "value", "Color", value))

        self.__pixel_access[index_x, index_y] = value.rgb

    def __iter__(self) -> typing.Iterator[Pixel]:
        for j in range(self.height):
            for i in range(self.width):
                yield Pixel((i, j), self.__pixel_access)

    def to_base64(self) -> str:
        """
        convert to base64 string of bytes in PNG encoding

        :return:
        """
        file_like_backed_by_byte_buffer = io.BytesIO()
        self._pil_image.save(file_like_backed_by_byte_buffer, format='PNG', optimize=True)
        unencoded_byte_buffer = file_like_backed_by_byte_buffer.getvalue()
        encoded_byte_buffer = base64.b64encode(unencoded_byte_buffer)
        base64_string = str(encoded_byte_buffer)[2:-1]  # discard "b'" and beginning and "'" at end
        return 'data:image/png;base64,' + base64_string

    # TODO test this
    def save(self, file_name: str) -> None:
        """
        save image to file
        :param file_name: name of file to save
        """
        self._pil_image.save(file_name)

    def copy(self) -> 'Picture':
        """
        Makes a copy of the picture

        :return: The copy
        :rtype: Picture
        """
        return Picture(self._pil_image.copy())

    def resize(self, height: int, width: int) -> 'Picture':
        """
        Write better docstring

        :param int height:
        :param int width:
        :return:
        """
        height = int(height)
        width = int(width)
        new_image = self._pil_image.resize((width, height))
        return Picture(new_image)

    def map(self, transform: Transform, left_top: Point = (0, 0),
            right_bottom: Point = (1000000, 1000000)) -> 'Picture':
        """
        Write better docstring

        :param transform:
        :param Point left_top:
        :param Point right_bottom:
        :return:
        """
        left: int = int(left_top[0])
        top: int = int(left_top[1])
        right: int = int(right_bottom[0])
        bottom: int = int(right_bottom[1])
        if left > right:
            (right, left) = (left, right)
        if top > bottom:
            (top, bottom) = (bottom, top)
        if left < 0:
            left = 0
        if right > self.width:
            right = self.width
        if top < 0:
            top = 0
        if bottom > self.height:
            bottom = self.height
        copy = self.copy()
        pixel_access: PixelAccess = copy.__pixel_access  # pylint: disable=protected-access
        for j in range(top, bottom):
            for i in range(left, right):
                index: Point = (i, j)
                pixel_info = PixelInfo(index, rgb=pixel_access[index])
                color_out: colors.Color = transform(pixel_info)
                pixel_access[index] = color_out.rgb
        return copy

    def remap(self, transform: Transform2, color: Color = Colors.black) -> 'Picture':
        """
        Write better docstring

        :param transform:
        :param Color color:
        :return:
        """
        width = self.width
        height = self.height
        target = Picture.make_empty(width, height, color)
        target_pixel_access: PixelAccess = target.__pixel_access  # pylint: disable=protected-access
        self_pixel_access: PixelAccess = self.__pixel_access
        for j in range(0, height):
            for i in range(0, width):
                index_in: Point = (i, j)
                tuple_in: PixelInfoTuple = (index_in, Color.unpack(self_pixel_access[index_in]))
                tuple_out: PixelInfoTuple = transform(tuple_in)
                ((target_x, target_y), rgb_out) = tuple_out
                target_pixel_access[target_x % width, target_y % height] = Color.clamp(rgb_out)
        return target

    def combine(self, pixel_combine: Combine, other: 'Picture', resize=False) -> 'Picture':
        """
        Writie better docstring

        :param pixel_combine:
        :param Picture other:
        :param bool resize:
        :return:
        :rtype: Picture
        """
        copy = self.copy()
        if resize:
            if (not copy.height == other.height) or (not copy.width == other.width):
                other = other.resize(copy.height, copy.width)
        pixel_access: PixelAccess = copy.__pixel_access  # pylint: disable=protected-access
        other_pixel_access: PixelAccess = other.__pixel_access  # pylint: disable=protected-access
        for j in range(copy.height):
            for i in range(copy.width):
                index: Point = (i, j)
                pixel_info = PixelInfo(index, rgb=pixel_access[index])
                other_pixel_info = PixelInfo(index, rgb=other_pixel_access[index])
                color_out: colors.Color = pixel_combine(pixel_info, other_pixel_info)
                pixel_access[index] = color_out.rgb
        return copy

    def map_if(self, predicate: Predicate, transform: Transform) -> 'Picture':
        """
        Write better docstring

        :param predicate:
        :param transform:
        :return:
        :rtype: Picture
        """
        copy = self.copy()
        pixel_access: PixelAccess = copy.__pixel_access  # pylint: disable=protected-access
        for j in range(copy.height):
            for i in range(copy.width):
                index: Point = (i, j)
                pixel_info = PixelInfo(index, rgb=pixel_access[index])
                if predicate(pixel_info):
                    color_out: colors.Color = transform(pixel_info)
                    pixel_access[index] = color_out.rgb
        return copy

    def replace_if(self, predicate: Predicate, other: 'Picture',
                   resize=False) -> 'Picture':
        """
        Write better docstring

        :param predicate:
        :param other:
        :param bool resize:
        :return:
        :rtype: Picture
        """
        copy = self.copy()
        if resize:
            if (not copy.height == other.height) or (not copy.width == other.width):
                other = other.resize(copy.height, copy.width)
        pixel_access: PixelAccess = copy.__pixel_access  # pylint: disable=protected-access
        other_pixel_access: PixelAccess = other.__pixel_access  # pylint: disable=protected-access
        for j in range(copy.height):
            for i in range(copy.width):
                index: Point = (i, j)
                pixel_info = PixelInfo(index, rgb=pixel_access[index])
                if predicate(pixel_info):
                    pixel_access[index] = other_pixel_access[index]
        return copy
