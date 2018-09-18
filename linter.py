#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jan T. Sott
# Copyright (c) 2018 Jan T. Sott
#
# https://github.com/idleberg/SublimeLinter-contrib-brew
#
# License: MIT
#

"""This module exports the Brew plugin class."""

from SublimeLinter.lint import Linter


class Brew(Linter):

    """Provides an interface to the Brew executable."""

    cmd = ('brew', 'audit', '--strict', '--display-filename', '${file}')
    defaults = {
        'selector': 'source.ruby'
    }
    regex = (
        r'^(?P<file>.+): \* C: (?P<line>\d+): col (?P<col>\d+): (?P<message>.+)$'
    )
    multiline = False
    line_col_base = (1, 1)
