# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '8 070-####-####',
        '8 080-####-####',
        '8 090-####-####',
        '8 ##-####-####',
    )
