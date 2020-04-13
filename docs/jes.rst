.. py:module:: MediaComp.jes
.. py:currentmodule:: MediaComp.jes

:py:mod:`~jes` Module
*********************

Picture Objects in JES
======================

To understand how to work with pictures in JES, you must first understand the objects (or encodings) that represent pictures.

You can imagine that each picture is made up of a collection of pixels, which is made up of pixel 0, pixel 1,
pixel 2, etc, and that each pixel has it's own particular color.

Pictures
--------
Pictures are encodings of images, typically coming from a JPEG or PNG file.

Pixels
------
Pixels are a sequence of Pixel objects. They flatten the two dimensional nature of the pixels in a picture and
give you instead an arraylike sequence of pixels. pixels[0] returns the leftmost pixel in a picture.

Pixel
-----
A pixel is a dot in the Picture. It has a color and an (x, y) position associated with it. It remembers its
own Picture so that a change to the pixel changes the real dot in the picture.

Color
-----
It’s a mixture of red, green, and blue values, each between 0 and 255.

Picture Functions in JES
========================

:py:func:`~copyInto` function
-----------------------------
.. autofunction:: MediaComp.jes.copyInto

:py:func:`~duplicatePicture` function
-------------------------------------
.. autofunction:: MediaComp.jes.duplicatePicture

:py:func:`~getHeight` function
------------------------------
.. autofunction:: MediaComp.jes.getHeight

:py:func:`~getPixels` function
------------------------------
.. autofunction:: MediaComp.jes.getPixels

:py:func:`~getAllPixels` function
---------------------------------
.. autofunction:: MediaComp.jes.getAllPixels

:py:func:`~getPixels` function
------------------------------
.. autofunction:: MediaComp.jes.getPixels

:py:func:`~getWidth` function
-----------------------------
.. autofunction:: MediaComp.jes.getWidth

:py:func:`~makeEmptyPicture` function
-------------------------------------
.. autofunction:: MediaComp.jes.makeEmptyPicture

:py:func:`~setAllPixelsToAColor` function
-----------------------------------------
.. autofunction:: MediaComp.jes.setAllPixelsToAColor


Color Functions
===============

:py:func:`~distance` function
-----------------------------
.. autofunction:: MediaComp.jes.distance

:py:func:`~makeBrighter` function
---------------------------------
.. autofunction:: MediaComp.jes.makeBrighter

:py:func:`~makeColor` function
------------------------------
.. autofunction:: MediaComp.jes.makeColor

:py:func:`~makeDarker` function
-------------------------------
.. autofunction:: MediaComp.jes.makeDarker

:py:func:`~makeLighter` function
--------------------------------
.. autofunction:: MediaComp.jes.makeLighter


Pixel Functions
===============
:py:func:`~getColor` function
-----------------------------
.. autofunction:: MediaComp.jes.getColor

:py:func:`~getRed` function
---------------------------
.. autofunction:: MediaComp.jes.getRed

:py:func:`~getGreen` function
-----------------------------
.. autofunction:: MediaComp.jes.getGreen

:py:func:`~getBlue` function
----------------------------
.. autofunction:: MediaComp.jes.getBlue

:py:func:`~getX` function
-------------------------
.. autofunction:: MediaComp.jes.getX

:py:func:`~getY` function
-------------------------
.. autofunction:: MediaComp.jes.getY

:py:func:`~setColor` function
-----------------------------
.. autofunction:: MediaComp.jes.setColor

:py:func:`~setRed` function
---------------------------
.. autofunction:: MediaComp.jes.setRed

:py:func:`~setGreen` function
-----------------------------
.. autofunction:: MediaComp.jes.setGreen

:py:func:`~setBlue` function
----------------------------
.. autofunction:: MediaComp.jes.setBlue

:py:func:`~writePictureTo` function
-----------------------------------
.. autofunction:: MediaComp.jes.writePictureTo

Other Picture Functions
=======================

:py:func:`~addArc` function
---------------------------
.. autofunction:: MediaComp.jes.addArc

:py:func:`~addArcFilled` function
---------------------------------
.. autofunction:: MediaComp.jes.addArcFilled

:py:func:`~addLine` function
----------------------------
.. autofunction:: MediaComp.jes.addLine

:py:func:`~addOval` function
----------------------------
.. autofunction:: MediaComp.jes.addOval

:py:func:`~addOvalFilled` function
----------------------------------
.. autofunction:: MediaComp.jes.addOvalFilled

:py:func:`~addRect` function
----------------------------
.. autofunction:: MediaComp.jes.addRect

:py:func:`~addRectFilled` function
----------------------------------
.. autofunction:: MediaComp.jes.addRectFilled

:py:func:`~addText` function
----------------------------
.. autofunction:: MediaComp.jes.addText

:py:func:`~addTextWithStyle` function
-------------------------------------
.. autofunction:: MediaComp.jes.addTextWithStyle


Text Style Functions
====================

:py:func:`~makeStyle` function
------------------------------
.. autofunction:: MediaComp.jes.makeStyle