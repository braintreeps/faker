from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '386 040 ### ###',
        '386 041 ### ###',
        '386 031 ### ###',
        '386 030 ### ###',
        '386 070 ### ###',
        '386 01 #### ###',
        '386 02 #### ###',
        '386 04 #### ###',
        '386 05 #### ###',
        '386 06 #### ###',
        '386 08 #### ###',
    )
