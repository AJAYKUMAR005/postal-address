# -*- coding: utf-8 -*-

from __future__ import (unicode_literals, print_function, absolute_import,
                        division)


class Address(object):
    """ Defines an address.

    Only provides address validation for the moment, but may be used in the
    future for l10n-aware normalization and rendering.

    Addresses are not persisted yet, as we don't allow organizations to have
    more than one active at the same time.
    """
    # Set default values
    line1 = None
    line2 = None
    zip_code = None
    state = None
    city = None
    country = None

    # Fields tested on validate()
    REQUIRED_FIELDS = ['line1', 'zip_code', 'city', 'country']

    def __init__(self, line1=None, line2=None, zip_code=None, state=None,
                 city=None, country=None):
        self.line1 = line1
        self.line2 = line2
        self.zip_code = zip_code
        self.state = state
        self.city = city
        self.country = country

    def validate(self):
        """ Checks required fields are set. """
        for field in self.REQUIRED_FIELDS:
            if not getattr(self, field):
                raise ValueError("Address requires {}.".format(field))
        return True
