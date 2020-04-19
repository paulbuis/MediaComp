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
from .. import sounds

##############################################################################
#
# JES wrapper functions functions for methods of sounds.Sample
#
##############################################################################


# noinspection PyPep8Naming
def getSampleValue(sample: sounds.Sample) -> int:
    """
    Takes a Sample object and returns its value (between -32768 and 32767).

    Wrapper for :py:attr:`.sounds.Sample.value` property.

    :param sounds.Sample sample: a sample of a sound
    :return: the integer value of that sample
    :rtype: int
    :raises TypeError: if ``sample`` is not a :py:class:`~.sounds.Sample`
    """
    if not isinstance(sample, sounds.Sample):
        raise TypeError(f'getSampleValue(), expected Sample, got{type(sample)}')
    return sample.value


# noinspection PyPep8Naming
def setSampleValue(sample: sounds.Sample, value: int) -> None:
    """
    Takes a Sample object and a value (should be between -32768 and 32767),
    and sets the sample to that value.

    Wrapper for assignment to :py:attr:`.sounds.Sample.value` property.

    :param sounds.Sample sample: the sound sample you want to change the value of
    :param int value: the value you want to set the sample to
    :raises TypeError: if ``sample`` is not a :py:class:`~.sounds.Sample`
    """
    value = int(value)
    if not isinstance(sample, sounds.Sample):
        raise TypeError(f'setSampleValue(), expected Sample, got{type(sample)}')
    sample.value = value


# noinspection PyPep8Naming
def getSound(sample: sounds.Sample) -> sounds.Sound:
    """
    Takes a Sample object and returns the Sound that it belongs to.

    Wrapper for the :py:attr:`.sounds.Sample.sound` property.

    :param sounds.Sample sample: a sample belonging to a sound
    :return: the sound the sample belongs to
    :rtype: sounds.Sound
    :raises TypeError: if ``sample`` is not a :py:class:`~.sounds.Sample`
    """
    if not isinstance(sample, sounds.Sample):
        raise TypeError(f'getSound(), expected Sample, got{type(sample)}')
    return sample.sound


##############################################################################
#
# JES wrapper functions functions for methods of sounds.Sound
#
##############################################################################


# noinspection PyPep8Naming
def makeSound(path: str) -> sounds.Sound:
    """
    Takes a filename as input, reads the file, and creates
    a sound from it. Returns the sound.

    Wrapper for :py:meth:`.sounds.Sound.from_file` class method.

    :param str path: a string path of a wav file
    :return: the sound created from the file at the given path
    :rtype: sounds.Sound
    """
    return sounds.Sound.from_file(str(path))


# noinspection PyPep8Naming
def makeEmptySound(numSamples: int,
                   samplingRate: float = 22050) -> sounds.Sound:
    """
    Takes one or two integers as input. Returns an empty Sound object
    with the given number of samples and (optionally) the given sampling rate.
    Default rate is 22050 bits/second.

    The resulting sound must not be longer than 600 seconds.
    Prints an error statement if numSamples or samplingRate are less than 0,
    or if (numSamples/samplingRate) > 600.

    Wrapper for :py:meth:`.sounds.Sound.make_empty` class method.

    :param int numSamples: the number of samples in sound
    :param float samplingRate: the number of samples per second of
                sound (optional)
    :return:  An Empty Sound.
    :rtype: sounds.Sound
    :raises ValueError:
    """
    samplingRate = float(samplingRate)
    if samplingRate <= 0:
        raise ValueError(f"sampling rate must be greater than zero, samplingRate={samplingRate}")
    numSamples = int(numSamples)
    if numSamples < 0:
        raise ValueError(f"numSamples must be zero or more, numsamples={numSamples}")
    duration: float = numSamples / samplingRate
    if duration > 600.0:
        data_message = f"duration is {duration}={numSamples}/{samplingRate}"
        raise ValueError("duration must be less than 600 seconds, " + data_message)
    return sounds.Sound.make_empty(numSamples, samplingRate)


# noinspection PyPep8Naming
def makeEmptySoundBySeconds(duration: float,
                            samplingRate: float = 22050) -> sounds.Sound:
    """
    Takes a floating point number and optionally an integer as input.
    Returns an empty Sound object of the given duration and
    (optionally) the given sampling rate.

    Default rate is 22050 bits/second. If the given arguments do not
    multiply to an integer, the number of samples is rounded up.

    Prints an error statement if duration or samplingRate are less
    than 0, or if duration > 600.

    Wrapper for :py:meth:`.sounds.Sound.make_empty` class method.

    :param float duration: the time in seconds for the duration of the sound
    :param float samplingRate: the integer value representing the number
                                of samples per second of sound (optional)
    :return: An Empty Sound.
    :rtype: sounds.Sound
    """
    if duration < 0 or duration > 600:
        raise ValueError(f"duration must be between 0 and 600, duration={duration}")
    if samplingRate <= 0:
        raise ValueError(f"sampleRate must greater than zero, samplingRate={samplingRate}")
    num_samples = int(duration*samplingRate + 0.5)
    return makeEmptySound(num_samples, samplingRate)


# noinspection PyPep8Naming
def duplicateSound(sound: sounds.Sound) -> sounds.Sound:
    """

    Wrapper for :py:meth:`.sounds.Sound.copy` method.

    :param sounds.Sound sound:
    :rtype: sounds.Sound
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'duplicateSound(), expected Sound, got{type(sound)}')
    return sound.copy()


# TODO: fix this!!!
def play(sound: sounds.Sound) -> None:
    """

    :param sounds.Sound sound:
    :raises TypeError: if ``sound`` is not a :py:`~.class:sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'play(), expected Sound, got{type(sound)}')
    # noinspection PyProtectedMember
    # IPython.display.display((IPython.display.Audio(sound.samples, rate=int(sound.rate)),))
    raise NotImplementedError


# noinspection PyPep8Naming
def getDuration(sound: sounds.Sound) -> float:
    """
    Takes a sound as input and returns the number of seconds that sound lasts.

    Wrapper for :py:attr:`.sounds.Sound.duration` property.

    :param sounds.Sound sound: the sound you want to find the length
            of (in seconds)
    :return: the number of seconds the sound lasts
    :rtype: float
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getDuration(), expected Sound, got{type(sound)}')
    return sound.duration


# noinspection PyPep8Naming
def getSamplingRate(sound: sounds.Sound) -> float:
    """
    Takes a sound as input and returns the number representing the
    number of samples in each second for the sound.

    Wrapper for :py:attr:`.sounds.Sound.rate property`

    :param sounds.Sound sound: the sound you want to get the sampling rate from
    :return: the number of samples per second
    :rtype: float
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getSamplingRate(), expected Sound, got{type(sound)}')
    return sound.rate


# noinspection PyPep8Naming
def getSamples(sound: sounds.Sound) -> typing.List[sounds.Sample]:
    """
    Takes a sound as input and returns the Samples in that sound.

    :param sounds.Sound sound: the sound you want to get the samples from
    :return: a list of all the samples in the sound
    :rtype: list[sounds.Sample]
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getSamples(), expected Sound, got{type(sound)}')
    return list(sound)


# noinspection PyPep8Naming
def getSampleObjectAt(sound: sounds.Sound, index: int) -> sounds.Sample:
    """
    Takes a sound and an index (an integer value), and returns the Sample
    object at that index

    :param sounds.Sound sound: the sound you want to get the sample from
    :param int index: the index value of the sample you want to get
    :return: the sample object at that index
    :rtype: sounds.Sample
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getSampleObjectAt(), expected Sound, got{type(sound)}')
    return sounds.Sample(index, sound)


# noinspection PyPep8Naming
def getSampleValueAt(sound: sounds.Sound, index: int) -> int:
    """
    Takes a sound and an index (an integer value), and returns the value
    of the sample (between -32768 and 32767) for that object.

    :param sounds.Sound sound: the sound you want to get the sample from
    :param int index: the index of the sample you want to get the value of
    :return: the value of the sample (between -32768 and 32767)
    :rtype: int
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getSampleValueAt(), expected Sound, got{type(sound)}')
    index = int(index)
    return sound[index]


# noinspection PyPep8Naming
def setSampleValueAt(sound: sounds.Sound, index: int, value: int) -> None:
    """
    Takes a sound, an index, and a value (should be between -32768
    and 32767), and sets the value of the sample at the given index
    in the given sound to the given value.

    :param Sounds.sound sound: the sound you want to change a sample in
    :param int index: the index of the sample you want to get the value of
    :param int value: the value you want to set the sample to
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'setSampleValueAt(), expected Sound, got{type(sound)}')
    sound[index] = value


# noinspection PyPep8Naming
def getLength(sound: sounds.Sound) -> int:
    """
    Takes a sound as input and returns the number of samples in that sound.

    Wrapper for :py:attr:`.sounds.Sound.length` property.

    :param sounds.Sound sound: the sound you want to find the length
        of (how many samples it has)
    :return: the number of samples in sound
    :rtype: int
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'getLength(), expected Sound, got{type(sound)}')
    return sound.length


# noinspection PyPep8Naming
def getNumSamples(sound: sounds.Sound) -> int:
    """
    Takes a sound as input and returns the number of samples in
    that sound. (Same as getLength)

    :param sounds.Sound sound: the sound you want to find the length of
        (how many samples it has)
    :return:  the number of samples in sound
    :rtype: int
    """
    return getLength(sound)


# noinspection PyPep8Naming
def writeSoundTo(sound: sounds.Sound, path: str) -> None:
    """
    Takes a sound and a filename (a string) and writes the sound to that
    file as a WAV file.

    Make sure that the filename ends in '.wav' if you want the operating system
    to treat it right.)

    :param sounds.Sound sound: the sound you want to write out to a file
    :param str path : the path to the file you want the picture written to
    :raises TypeError: if ``sound`` is not a :py:class:`~.sounds.Sound`
    """
    path = str(path)
    if not isinstance(sound, sounds.Sound):
        raise TypeError(f'writeSoundTo(), expected Sound, got{type(sound)}')
    sound.write(path)
