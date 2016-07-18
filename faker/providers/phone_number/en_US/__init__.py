from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '1'
    formats = (
        '###-###-####',
        '###-###-####x#####',
        '###-###-####x####',
        '###-###-####x###',
        '###.###.####',
        '###.###.####x#####'
        '###.###.####x####',
        '###.###.####x###',
        '(###)###-####',
        '(###)###-####x#####',
        '(###)###-####x####',
        '(###)###-####x###',
        '+##(#)##########',
        '0##########',
    )
