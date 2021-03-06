# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import os
import sys
import time

# Expose package to autodoc.
sys.path.insert(0, os.path.abspath('..'))
import postal_address  # noqa  # isort:skip

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

master_doc = 'index'

project = "Postal Address"
author = "Scaleway"

# We use our own copyright template instead of the default as the latter strip
# HTML content.
html_show_copyright = False
copyright = (
    "2013-{}, <a href='https://scaleway.com'>{}</a> and <a href='https://"
    "github.com/scaleway/postal-address/graphs/contributors'>"
    "contributors</a>").format(time.strftime('%Y'), author)

version = release = postal_address.__version__

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

nitpicky = True
# We need a recent sphinx because of the last update format.
needs_sphinx = '1.4'
html_last_updated_fmt = 'YYYY-MM-dd'
templates_path = ['templates']

# Keep the same ordering as in original source code.
autodoc_member_order = 'bysource'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Use RTD theme both locally and online. Source: https://github.com/snide
# /sphinx_rtd_theme#using-this-theme-locally-then-building-on-read-the-docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

htmlhelp_basename = project
