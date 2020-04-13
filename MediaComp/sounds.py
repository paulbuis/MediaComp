#
# Package: MediaComp
# Module: pictures
# Author: Paul Buis, 00pebuis@bsu.edu
#
# Derived from source code, power point slides, and media (pictures, movies, sounds) from
# http://mediacomputation.org created by Mark Guzdial and Barbara Ericson
# licensed under the Creative Commons Attribution 3.0 United States License,
# See: http://creativecommons.org/licenses/by/3.0/us/).


# module typing is standard in Python 3.5+: https://docs.python.org/3/library/typing.html
# used for type hints used in static type checking in PEP 484
# PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484/
# PEP 525 -- Syntax for Variable Annotations: https://www.python.org/dev/peps/pep-0526/
# use mypy for static type checking of Pyhton code: http://mypy-lang.org/
# note that just because a parameter is annotated to be of a specific type, doesn't mean
# that at runtime it will actually be of that type: dynamic checking or casting/conversion still needs to be done
import typing

import os

# suppress static type checker complain "error: No library stub file for module 'numpy'"
import numpy  # type: ignore


# using read & write methods of wavfile class in scipy.io module
# See: https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html#scipy.io.wavfile.read

# suppress static type checker complain "error: No library stub file for module 'scipy.io'"
from scipy.io import wavfile  # type: ignore

# The IPython.core.display module is specific to IPython which is used in Jupyter
# See https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html
import IPython  # type: ignore

from . import files


class Sound(typing.Iterable):
    """
    represents a sound read in from a WAV format file
    """

    # TODO: edit docstring
    @classmethod
    def from_file(cls, file_name: typing.Union[str, os.PathLike]) -> 'Sound':
        """

        :param file_name:
        :return:
        """
        path = files.media_path(file_name)
        rate, data = wavfile.read(path)
        return cls(numpy.copy(data), rate)

    # TODO: edit docstring
    @classmethod
    def make_empty(cls, num_samples: int, rate: float = 22500.0):
        """

        :param num_samples:
        :param rate:
        :return:
        """
        num_samples = int(num_samples)
        if num_samples < 0:
            raise ValueError
        data: numpy.array = numpy.zeros(num_samples, dtype=numpy.int32)
        return cls(data, rate)

    def __init__(self, data, rate=None):
        self.__rate: float = float(rate)
        self.__samples: numpy.array = data

    def copy(self) -> 'Sound':
        data_copy: numpy.array = numpy.copy(self.__samples)
        new_sound: 'Sound' = Sound(data_copy, self.__rate)
        return new_sound

    def __str__(self) -> str:
        return f"Sound: {len(self)} samples at {self.__rate} sample/second"

    def __iter__(self) -> typing.Iterator['Sample']:
        for i in range(0, self.length):
            yield Sample(i, self)

    # TODO: property docstring
    @property
    def samples(self) -> typing.Iterator['Sample']:
        """

        """
        return iter(self)

    @property
    def length(self) -> int:
        """
        number of samples in the sound
        """
        return len(self.__samples)

    def __len__(self) -> int:
        return len(self.__samples)

    @property
    def duration(self) -> float:
        """
        number of seconds the sound lasts = length/rate
        """
        return float(len(self.__samples))/float(self.__rate)

    @property
    def rate(self):
        """ returns sampling rate of sound in samples per second (Hz) """
        return self.__rate

    # TODO method docstring
    def __getitem__(self, index: int) -> int:
        """

        :param index:
        :return:
        """
        index = int(index)
        if index < 0:
            raise IndexError(f'Sound.getitem({index}): Negative Index')
        if index >= len(self.__samples):
            raise IndexError(f'Sound.getitem({index}), Index too large, max={self.__samples}')
        return int(self.__samples[index])

    @staticmethod
    def clamp(value: int) -> int:
        """

        :param value:
        :return:
        """
        value = int(value)
        if value > 32767:
            value = 32767
        elif value < -32768:
            value = -32768
        return value

    def __setitem__(self, index: int, value: int) -> None:
        """

        :param index:
        :param value:
        :return:
        """
        index = int(index)
        if index < 0:
            raise IndexError(f'Sound.setitem({index}): Negative Index')
        if index >= len(self):
            raise IndexError(f'Sound.setitem({index}), Index too large, max={self.__samples}')

        value = numpy.int16(Sound.clamp(value))
        self.__samples[index] = value

    def _repr_html_(self) -> str:
        """

        :return:
        """
        audio = IPython.display.Audio(self.__samples, rate=int(self.__rate))
        # noinspection PyProtectedMember
        return audio._repr_html_()

    # TODO method docstring
    def write(self, file_name: str) -> None:
        """

        :param file_name:
        :return:
        """
        from . import files
        file_name = str(file_name)
        file_path = files.media_path(file_name)
        wavfile.write(str(file_path), int(self.rate), self.__samples)


# TODO: class docstring
class Sample:
    """

    """
    def __init__(self, index, sound: Sound):
        index = int(index)
        if index < 0:
            raise ValueError
        if index >= sound.length:
            raise ValueError
        self.__sound: Sound = sound
        self.__index: int = index

    # TODO: edit property docstring
    @property
    def value(self) -> int:
        """  ??? """
        return int(self.__sound[self.__index])

    @value.setter
    def value(self, v: int) -> None:
        self.__sound[self.__index] = numpy.int16(Sound.clamp(v))

    # TODO: edit property docstring
    @property
    def sound(self) -> Sound:
        """ ??? """
        return self.__sound
