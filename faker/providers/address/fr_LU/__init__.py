# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    postcode_formats = ('####',)
