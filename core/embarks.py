#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Embark profile management."""
from __future__ import print_function, unicode_literals, absolute_import

import os
from . import helpers, paths

def read_embarks():
    """Returns a list of embark profiles."""
    return tuple([
        os.path.basename(o) for o in helpers.get_text_files(
            paths.get('embarks'))])

def install_embarks(files):
    """
    Installs a list of embark profiles.

    Params:
        files
            List of files to install.
    """
    out = open(os.path.join(paths.get('init'), 'embark_profiles.txt'), 'w')
    for f in files:
        embark = open(os.path.join(paths.get('embarks'), f))
        out.write(embark.read()+"\n\n")
    out.flush()
    out.close()

