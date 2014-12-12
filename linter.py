#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Zeke Sonxx
# Copyright (c) 2014 Zeke Sonxx <github.com/zekesonxx>
#
# License: MIT
#

"""This module exports the Spider plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Spider(NodeLinter):

    """Provides an interface to spider."""

    syntax = 'spiderscript'
    cmd = ('spider', '-c', '--disable-source-map')
    executable = 'spider'
    npm_name = 'spider'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.7'
    regex = r'\s*line\s*(?P<line>[0-9]+)\s+col\s+(?P<col>[0-9]+)\s+(?P<message>unexpected (?P<near>.+))$'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'spider'
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = None
    defaults = {
        'enable_if_dependency': True,
        'disable_if_not_dependency': True
    }
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
