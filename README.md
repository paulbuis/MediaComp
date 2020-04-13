# MediaComp

A package of Python 3 modules intended to mimic Guzdial & Ericson's
JES Media Computation library in an IPython / Jupyter environment.

[![Documentation Status](https://readthedocs.org/projects/mediacomp/badge/?version=latest)](https://mediacomp.readthedocs.io/en/latest/?badge=latest)
## Installation

_Coming soon_

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MediaComp.

``` bash
pip install MediaComp
```

## Usage

### Using JES / Jython / Python / non-OO syntax

``` python
from MedidaComp.jes import *

pic = makePicture('foo.jpg')
pixel = getPixel(10, 20)
setColor(pixel, blue)
```

### Using Python 3 / OO syntax

``` python

from MediaComp.pictures import *
# and / or
from MediaComp.sounds import *

picture = Picture.from_file('foo.jpg')
picture[10, 20].color = colors.Colors.blue 

```

## Documentation

HTML documentation hosted on [Read The Docs](https://mediacomp.readthedocs.io/en/latest/)

### Modules

#### module `jes`


The `jes` module is the one to import with
``` python
from MediaComp.jes import *
```
to mimic the function calls in JES from Guzdial and
and Ericson.

It does *not* export the names from other modules in the package.
It simply provides functions to wrap the methods, and properties
provided by them to avoid more advanced Python notations
involving dots, iterators, and indexers. This allows students to
use syntax that is essentially equivalent to that used in
the Guzdial and Ericson textbook.

#### module `pictures`

The `pictures` module exports all the names from the `colors` module.

The `pictures` module provides the following classes:
+ `PILImage` is a simple wrapper around the PIL.Image module's
        Image class.
 `RGBImage` is a subclass of `PILImage` that adds instance
    methods for pixel-level access to RGB mode images. 
* `Picture` is a subclass of `RGBImage` adds class methods to
    create images from files or single  color images. Note that the
    constructor for the class is not intended to be used directly.
    Instead use the class methods `from_file(filename)` or
    `make_empty(width, height, color = None)`.

``` python
boat = Picture.from_file("boat.jpg")
```
or
``` python
blue_box = Picture.make_empty(640, 480, Color(0, 0, 255)
```

#### module `colors`

The `colors` module provides classes intended to support the `pictures`
module. You do not need to directly import it if you are importing
the `pictures` module

* class `BaseRGB` is a simple wrapper for a triple of `int` values. Note that
    `pictures.Pixel` is an indirect subclass that also provides
    setters corresponding to the getters provided here.
* class `Color` is the subclass of `BaseRGB` intended for normal use and
    is immutable. That is, it provides no attribute setters.
* class `Colors` is a class
    that provides class methods for creating a few
    basic named colors. These can be used to limit the number of
    instances of `Color` that needs to be created. It is intended that
    you use `Colors.blue` repeatedly rather than creating many instances 
    of Color with `Color(0, 0, 255)`

#### `sounds`

_This module is not well tested. Use with extreme caution._

* class `Sound` is a simple wrapper for a single sequence of `numpy`
    16-bit signed integer sample values. Access to the sample
    values is provided via the `Sample` class.
* class `Sample` wraps a sample value providing transation between
    `numpy` 16-bit signed intger sample values and standard Python
    `int`, ensuring that values outside the 16-bit range are clamped
    rather than discarding high order bits.

#### `files`

Has no classes, just a single value named `path` which is an
instance of the `pathlib.Path` class and is
initialized to correspond to the current working directory
and intended to be accessed via two function. This object represents
the directory for all file reading operations in modules `pictures` and
`sounds`. So, essentially, `pictures.Picture.from_file('foo.png')` will
read from `path + '/' + 'foo.png'`

* `files.media_path(file_name)` returns the result of appending 
    `file_name` to `path`.
* `file.set_media_path(dir_name)` converts the string representing
the name of the directory to read from into a `pathlib.Path` object
and stores it in `path`.

#### `turtles`

_This module is completely untested and should not be used._

* class `World`
* class `Turtle`



## License
This code is made available under the
[MIT](https://choosealicense.com/licenses/mit/)
license

## Attribution Notice

Derived from source code, power point slides, and media
(pictures, movies, sounds) from
[http://mediacomputation.org](http://mediacomputation.org)
created by Mark Guzdial and others
licensed under the Creative Commons Attribution 3.0 United States License,
See: [http://creativecommons.org/licenses/by/3.0/us/](http://creativecommons.org/licenses/by/3.0/us/).