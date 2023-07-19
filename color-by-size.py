#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2023 Jett Pavlica, jettpav@gmail.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
"""
An extension for Inkscape geared towards plotter artists using macOS. The extension allows
users to set paths within a range of sizes to a single fill color, for use with the internal
tool "select similar fill color" to create a select by size extension.

There is a much better version of this extension for Windows and Linux users here:
https://inkscape.org/~inklinea/%E2%98%85selection-plus

"""

import inkex

class ColorBySizeExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--min_size", type=float, dest='min_size', default=0)
        pars.add_argument("--max_size", type=float, dest='max_size', default=10)
        pars.add_argument("--fill_color", type=inkex.Color, dest='fill_color')
        pars.add_argument("--from_selected", type=inkex.Boolean, dest='from_selected')


    def effect(self):
        for elem in self.svg:
            if elem.bounding_box().area < 20:
                elem.style['fill'] = 'red'
                elem.style['fill-opacity'] = 1
                elem.style['opacity'] = 1

if __name__ == '__main__':
    ColorBySizeExtension().run()
