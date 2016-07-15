from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '(+30) 69## ######',
        '+30 69## ######',
        '+3069########',
        '(+30) 2### ######',
        '+30 2### ######',
        '+302#########',
    )
