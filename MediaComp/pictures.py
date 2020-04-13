#
# Package: MediaComp
# Module: pictures
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies, sounds) from
# http://mediacomputation.org created by Mark Guzdial and Barbara Ericson
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/).

# module base64 is standard in Python 3: https://docs.python.org/3/library/base64.html
# using base64.b64encode in JESImage.toBase64
import base64

# module io is standard in Python 3: https://docs.python.org/3/library/io.html
# using io.BytesIO in JESImage.toBase64
import io

import os


# module typing is standard in Python 3.5+: https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton code: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type, doesn't mean
# that at runtime it will actually be of that type: dynamic checking or casting/conversion still needs to be done
# static inspection may incorrectly show Tuple as an unused import, it is used for type aliases only
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

# suppress static type checker complain "error: No library stub file for module 'matplotlob.font_manager'"
# suppress static type checker complain "error: No library stub file for module 'matplotlob'"
import matplotlib.font_manager  # type: ignore

# The IPython.core.display module is specific to IPython which is used in Jupyter
# See https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html
# import IPython.core.display

# import the color and file modules in this package
from . import colors
from . import files

# make the names in the color and file modules public to
# consumers of this module
Colors = colors.Colors
Color = colors.Color
set_media_path = files.set_media_path
media_path = files.media_path

# Type aliases
RGB = typing.Tuple[int, int, int]
ImageSize = typing.Tuple[int, int]
Point = typing.Tuple[int, int]
PointSequence = typing.Sequence[Point]
BaseRGB = colors.BaseRGB
Transform = typing.Callable[['PixelInfo'], Color]
Predicate = typing.Callable[['PixelInfo'], bool]
Combine = typing.Callable[['PixelInfo', 'PixelInfo'], Color]


def type_error_message(fun_name: str, param_name: str, expected: str, actual: typing.Any) -> str:
    return f"In MediaComp.pictures.{fun_name}: {param_name} expected a {expected}, actually {type(actual)}"


# TODO: add doc string
class PixelInfo(colors.Color):
    """

    """

    # TODO: add doc string
    def __init__(self, xy: Point, *, rgb: typing.Optional[RGB] = None, pixel_color: typing.Optional[Color] = None):
        # TODO: find better way to initialize superclass value
        super().__init__()
        self._xy: Point = (int(xy[0]), int(xy[1]))
        if rgb is not None:
            # do we want a runtime type check
            # to make sure rgb is a Tuple of ints?
            # not performance friendly, and don't
            # expect direct user calls anyway
            self._BaseRGB__rgb = rgb
        elif pixel_color is not None:
            # do we want a runtime type check
            # to make sure pixel_color is an instance of BaseRGB?
            self._BaseRGB__rgb = pixel_color.rgb

    # Overrides Color.__repr__
    # TODO: add """ doc comment
    def __repr__(self) -> str:
        """

        :return:
        """
        return f"PixelInfo(xy = ({self.x}, {self.y}), " + \
               f"pixel_color = Color(red={self.red}, green={self.green}, blue={self.blue}))"

    # Overrides Color.__str__
    # TODO: add doc string
    def __str__(self) -> str:
        """

        :return:
        """
        return f"Pixel(red={self.red}, green={self.green}, blue={self.blue}, x={self.x}, y={self.y})"

    # TODO: add doc string
    @property
    def color(self) -> colors.Color:
        """

        :return:
        """
        rgb: RGB = self.rgb
        return Color(rgb[0], rgb[1], rgb[2])

    # TODO: add doc string
    @property
    def x(self) -> int:
        """

        :return:
        """
        return int(self._xy[0])

    # TODO: add doc string
    @property
    def y(self) -> int:
        """

        :return:
        """
        return int(self._xy[1])


# TODO: add doc string
class Pixel(PixelInfo):
    """

    """

    # TODO: add doc string
    def __init__(self, xy: Point, pixel_access: PixelAccess):
        """

        :param xy:
        :param pixel_access:
        """
        self.__pixel_access: PixelAccess = pixel_access
        super().__init__(xy)

    # TODO: provide __repr__ method?, do we need/want to override PixelInfo.__repr__ ??

    # TODO: add """ doc comment
    # Overrides PixelInfo.__str__ method
    def __str__(self) -> str:
        """

        :return:
        """
        return f"Pixel(xy=({self.x}, {self.y}), Color(r={self.red}, g={self.green}, b={self.blue}))"

    # TODO: add doc string
    @property
    def color(self) -> Color:
        """

        :return:
        """
        rgb: RGB = self.__pixel_access[self._xy]
        return Color(rgb[0], rgb[1], rgb[2])

    # TODO: add doc string
    @color.setter
    def color(self, rgb: colors.BaseRGB) -> None:
        """

        :param rgb:
        :return:
        """
        if not isinstance(rgb, colors.BaseRGB):
            raise TypeError
        self.rgb = rgb.rgb

    # TODO: add """ doc comment
    # Overrides BaseRGB.red property getter
    @property
    def red(self) -> int:
        """

        :return:
        """
        return self.rgb[0]

    # TODO: add """ doc comment
    @red.setter
    def red(self, value: int) -> None:
        """

        :param value:
        :return:
        """
        value = int(value)
        if value < 0:
            value = 0
        elif value > 255:
            value = 255

        rgb: RGB = self.__pixel_access[self._xy]
        self.__pixel_access[self._xy] = (value, rgb[1], rgb[2])

    # TODO: add """ doc comment
    # Overrides BaseRGB.green property getter
    @property
    def green(self) -> int:
        """

        :return:
        """
        return self.rgb[1]

    # TODO: add """ doc comment
    @green.setter
    def green(self, value: int) -> None:
        """

        :param value:
        :return:
        """
        value = int(value)
        if value < 0:
            value = 0
        elif value > 255:
            value = 255

        rgb: RGB = self.__pixel_access[self._xy]
        self.__pixel_access[self._xy] = (rgb[0], value, rgb[2])

    # TODO: add """ doc comment
    # Overrides BaseRGB.blue property getter
    @property
    def blue(self) -> int:
        """

        :return:
        """
        return self.rgb[2]

    # TODO: add """ doc comment
    @blue.setter
    def blue(self, value: int) -> None:
        """

        :param value:
        :return:
        """
        value = int(value)
        if value < 0:
            value = 0
        elif value > 255:
            value = 255

        rgb: RGB = self.__pixel_access[self._xy]
        self.__pixel_access[self._xy] = (rgb[0], rgb[1], value)

    # TODO: add """ doc comment
    # Overrides BaseRGB.rgb property getter
    @property
    def rgb(self) -> RGB:
        """

        :return:
        """
        rgb: RGB = self.__pixel_access[self._xy]
        return int(rgb[0]), int(rgb[1]), int(rgb[2])

    # TODO: add """ doc comment
    @rgb.setter
    def rgb(self, value: RGB) -> None:
        """

        :param value:
        :return:
        """
        self.__pixel_access[self._xy] = value


# TODO: add doc string
class TextStyle:
    """

    """

    @staticmethod
    def find_font_file(query: str) -> typing.Optional[str]:
        matches = list(filter(lambda path: query in os.path.basename(path), matplotlib.font_manager.findSystemFonts()))
        if len(matches) == 0:
            return None
        return matches[0]

    # TODO: add doc string
    def __init__(self, font_name: str, emphasis: str, size: float):
        """

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

    # TODO: add doc string
    @property
    def font_name(self) -> str:
        """
        name of font used to draw with
        """
        return self.__font_name

    # TODO: add doc string
    @property
    def font(self) -> PIL.ImageFont.ImageFont:
        return self.__font

    # TODO: add doc string
    @property
    def emphasis(self) -> str:
        """
        kind of emphasis to use, 'bold', 'italic', 'bold + italic'
        """
        return self.__emphasis

    # TODO: add doc string
    @property
    def size(self) -> float:
        """
        size of font in points
        """
        return self.__size


# TODO: add doc string
# class PILImage has no pixel-level operations and is agnostic about how many and what kind
# of channels are in the image. Such things will be found in subclasseses of PILImage
class PILImage:
    """

    """
    def __init__(self, pil_image: PIL.Image.Image):
        self._pil_image = pil_image

    @property
    def height(self) -> int:
        """
        height of image in pixels
        """
        h = self._pil_image.height
        return int(h)

    @property
    def width(self) -> int:
        """
        width of image in pixels
        """
        w = self._pil_image.width
        return int(w)

    @property
    def size(self) -> ImageSize:
        """
        (height, width) tuple
        """
        return self.height, self.width

    def copy(self) -> 'PILImage':
        return PILImage(self._pil_image.copy())

    # TODO test this
    def save(self, file_name: str) -> None:
        """
        save image to file
        :param file_name: name of file to save
        """
        self._pil_image.save(file_name)

    # noinspection PyPep8Naming
    def toBase64(self) -> str:
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

    def __str__(self) -> str:
        """

        :return:
        """

        return "<image> size:" + str(self.size)

    def _repr_html_(self) -> str:
        """

        :return:
        """
        return '<img src="' + self.toBase64() + '" />'

    # TODO: fix it so it uses IPython display mechanism for PNG rather than HTML
    # def _repr_png_(self):
    #    pass

    # TODO: edit doc string
    def set_color(self, color: colors.BaseRGB = colors.Colors.black):
        """

        :param color:
        :return:
        """
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.rectangle([(0,0), (self.width, self.height)], fill=color)

    # TODO: edit doc string
    def copy_into(self, big_picture: 'PILImage', x: int, y: int):
        """

        :param big_picture:
        :param x:
        :param y:
        :return:
        """
        big_picture._pil_image.paste(self._pil_image, (x, y))

    # TODO: edit doc string
    def add_arc(self, x: int, y: int, width: int, height: int,
                start: float, angle: float,
                color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param start:
        :param angle:
        :param color:
        """
        x = int(x)
        y = int(y)
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

    # TODO: edit doc string
    def add_arc_filled(self, x: int, y: int,
                       width: int, height: int,
                       start: float, angle: float,
                       color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param start:
        :param angle:
        :param color:
        """
        x = int(x)
        y = int(y)
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

    # TODO: edit doc string
    def add_line(self, x: int, y: int, width: int, height: int,
                 color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        """
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_line", "color", "Color", color))
        bounding_box: PointSequence = [(x, y), (x + width, y + height)]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.line(bounding_box, fill=color.rgb, width=1)

    # TODO: edit doc string
    def add_oval(self, x: int, y: int, width: int, height: int,
                 color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        """
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_oval", "color", "Color", color))
        bounding_box: PointSequence = [(x, y), (x + width, y + height)]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.ellipse(bounding_box, outline=color.rgb, width=1)

    # TODO: edit doc string
    def add_oval_filled(self, x: int, y: int, width: int, height: int,
                        color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        """
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_oval_filled", "color", "Color", color))
        bounding_box = [(x, y), (x + width, y + height)]
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.ellipse(bounding_box, outline=color.rgb, fill=color.rgb, width=1)

    # TODO edit doc string
    def add_rect(self, x: int, y: int, width: int, height: int,
                 color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        """
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        # TODO: make sure rectangle is inside image ???
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_rect", "color", "Color", color))
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.rectangle([(x, y), (x+width, y+height)], outline=color.rgb, width=1)

    # TODO: edit doc string
    def add_rect_filled(self, x: int, y: int, width: int, height: int,
                        color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        """
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        # TODO: make sure rectangle is inside image ???
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_rect_filled", "color", "Color", color))
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.rectangle([(x, y), (x+width, y+height)], fill=color.rgb, width=1)

    # TODO: edit doc string
    def add_text(self, x: int, y: int, text: str,
                 color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param text:
        :param color:
        """
        x = int(x)
        y = int(y)
        text = str(text)
        if color is None:
            color = colors.Colors.black
        elif not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_text", "color", "Color", color))
        draw = PIL.ImageDraw.Draw(self._pil_image)
        draw.text((x, y), text, fill=color.rgb)

    # TODO: edit doc string
    def add_text_with_style(self, x: int, y: int, text: str, style: TextStyle,
                            color: colors.BaseRGB = colors.Colors.black) -> None:
        """

        :param x:
        :param y:
        :param text:
        :param style:
        :param color:
        """
        x = int(x)
        y = int(y)
        text = str(text)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("PILImage.add_text_styled", "color", "Color", color))
        if not isinstance(style, TextStyle):
            raise TypeError(type_error_message("PILImage.add_text_styled", "style", "TextStyle", style))
        draw: PIL.ImageDraw.ImageDraw = PIL.ImageDraw.Draw(self._pil_image)
        draw.text((x, y), text, font=style.font, fill=color.rgb)


#
# class RGBImage adds pixel-level operations to PILImage
# and works only with 3-channel 8-bit/channel images
#
# TODO: add doc string
class RGBImage(PILImage, typing.Iterable):
    """

    """

    # TODO: Add doc string
    def __init__(self, pil_image: PIL.Image.Image):
        """

        :param pil_image:
        """

        if pil_image.mode == "RGB":
            super().__init__(pil_image)
        else:
            super().__init__(pil_image.convert(mode="RGB"))
        self.__pixel_access: PIL.PyAccess.PyAccess = self._pil_image.load()

    # TODO: Add doc string
    def copy(self) -> 'RGBImage':
        """

        :return:
        """
        return RGBImage(self._pil_image.copy())

    # TODO: add doc string
    def __getitem__(self, key: Point) -> Pixel:
        """

        :param key:
        :return:
        """
        x = int(key[0])
        y = int(key[1])

        if x >= self.width:
            x = self.width - 1
        if y >= self.height:
            y = self.height - 1
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        return Pixel((x, y), self.__pixel_access)

    # TODO: Add doc string
    def __setitem__(self, key: Point, value: colors.BaseRGB) -> None:
        """

        :param key:
        :param value:
        """
        x = int(key[0])
        y = int(key[1])

        # silently discard value if out of range, is that really a good thing?
        if x < 0 or x >= self.width:
            return
        if y < 0 or y >= self.height:
            return

        if not isinstance(value, colors.BaseRGB):
            raise TypeError(type_error_message("RGBImage.setitem", "value", "Color", value))

        self.__pixel_access[x, y] = value.rgb

    # TODO: add doc string
    def __iter__(self) -> typing.Iterator[Pixel]:
        """

        :yield:
        """
        for j in range(self.height):
            for i in range(self.width):
                yield Pixel((i, j), self.__pixel_access)

    # TODO: add doc string
    def resize(self, height: int, width: int) -> 'RGBImage':
        """

        :param height:
        :param width:
        :return:
        """
        height = int(height)
        width = int(width)
        new_image = self._pil_image.resize((width, height))
        return RGBImage(new_image)

    # TODO: add doc string
    def map(self, transform: Transform, left_top: Point= (0,0), right_bottom: Point= (1000000, 1000000)) -> 'RGBImage':
        """

        :param transform:
        :param left_top:
        :param right_bottom:
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
        pixel_access: PixelAccess = copy.__pixel_access
        for j in range(top, bottom):
            for i in range(left, right):
                xy = (i, j)
                pixel_info = PixelInfo(xy, rgb=pixel_access[xy])
                color_out: colors.Color = transform(pixel_info)
                pixel_access[xy] = color_out.rgb
        return copy

    # TODO: Add doc string
    def combine(self, pixel_combine: Combine, other: 'RGBImage', resize=False) -> 'RGBImage':
        """

        :param pixel_combine:
        :param other:
        :param resize:
        :return:
        """
        copy = self.copy()
        if resize:
            if (not (copy.height == other.height)) or (not (copy.width == other.width)):
                other = other.resize(copy.height, copy.width)
        pixel_access: PixelAccess = copy.__pixel_access
        other_pixel_access: PixelAccess = other.__pixel_access
        for j in range(copy.height):
            for i in range(copy.width):
                xy = (i, j)
                pixel_info = PixelInfo(xy, rgb=pixel_access[xy])
                other_pixel_info = PixelInfo(xy, rgb=other_pixel_access[xy])
                color_out: colors.Color = pixel_combine(pixel_info, other_pixel_info)
                pixel_access[xy] = color_out.rgb
        return copy

    # TODO: add doc string
    def difference(self, other: 'RGBImage', scale: float = 1.0) -> 'RGBImage':
        """

        :param other:
        :param scale:
        :return:
        """
        def diff(color1: PixelInfo, color2: PixelInfo) -> colors.Color:
            d: int = int(color1.distance(color2) * scale)
            return colors.Color(d, d, d)
        return self.combine(diff, other)

    # TODO: add doc string
    def map_if(self, predicate: Predicate, transform: Transform) -> 'RGBImage':
        """

        :param predicate:
        :param transform:
        :return:
        """
        copy = self.copy()
        pixel_access: PixelAccess = copy.__pixel_access
        for j in range(copy.height):
            for i in range(copy.width):
                xy = (i, j)
                pixel_info = PixelInfo(xy, rgb=pixel_access[xy])
                if predicate(pixel_info):
                    color_out: colors.Color = transform(pixel_info)
                    pixel_access[xy] = color_out.rgb
        return copy

    # TODO: Add doc string
    def replace_if(self, predicate: Predicate, other: 'RGBImage', resize=False) -> 'RGBImage':
        """

        :param predicate:
        :param other:
        :param resize:
        :return:
        """
        copy = self.copy()
        if resize:
            if (not (copy.height == other.height)) or (not (copy.width == other.width)):
                other = other.resize(copy.height, copy.width)
        pixel_access: PixelAccess = copy.__pixel_access
        other_pixel_access: PixelAccess = other.__pixel_access
        for j in range(copy.height):
            for i in range(copy.width):
                xy = (i, j)
                pixel_info = PixelInfo(xy, rgb=pixel_access[xy])
                if predicate(pixel_info):
                    pixel_access[xy] = other_pixel_access[xy]
        return copy


#
# Picture operates on files containing RGB images
#
# All interactions with the filesystem should be here
# not in superclasses
#
# TODO: add doc string
class Picture(RGBImage):
    """

    """

    # TODO: edit doc string
    @classmethod
    def from_file(cls, filename: typing.Union[str, os.PathLike]) -> 'Picture':
        """

        :param filename:
        :return:
        """
        if not isinstance(filename, os.PathLike):
            filename = files.media_path(str(filename))
        img = PIL.Image.open(filename)
        img.load()
        return cls(img)

    # TODO: add doc string
    @classmethod
    def make_empty(cls, width: int, height: int, color: colors.BaseRGB = colors.Colors.black):
        """

        :param width:
        :param height:
        :param color:
        :return:
        """
        height = int(height)
        width = int(width)
        if not isinstance(color, colors.BaseRGB):
            raise TypeError(type_error_message("setAllPixelsToAColor", "color", "Color", color))
        return cls(PIL.Image.new("RGB", (width, height), color.rgb))

    # TODO: add doc string
    def __init__(self, image: PIL.Image.Image):
        """

        :param image:
        """
        super().__init__(image)

    def __str__(self) -> str:
        return f"Picture, image height={self.height}, width={self.width}"

    def copy(self) -> 'Picture':
        """

        :return:
        """
        return Picture(self._pil_image.copy())
