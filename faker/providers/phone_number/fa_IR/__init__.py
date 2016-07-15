from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        # Mobile
        '+98 91# ### ####',
        '+98 920 ### ####',
        '+98 921 ### ####',
        '+98 93# ### ####',
        # Land lines
        '+98 21 #### ####',
        '+98 25 #### ####',
        '+98 26 #### ####',
        '+98 ### #### ####',
    )
