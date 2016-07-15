# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+31### ######',
        '+31## #######',
        '+31(0)### ######',
        '+31(0)## #######',
        '+31###-######',
        '+31##-#######',
        '+31(0)###-######',
        '+31(0)##-#######',
    )
