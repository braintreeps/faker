from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        # Mobile
        # Government website: http://www.uke.gov.pl/numeracja-843
        '+48 50# ### ###',
        '+48 51# ### ###',
        '+48 53# ### ###',
        '+48 57# ### ###',
        '+48 60# ### ###',
        '+48 66# ### ###',
        '+48 69# ### ###',
        '+48 72# ### ###',
        '+48 73# ### ###',
        '+48 78# ### ###',
        '+48 79# ### ###',
        '+48 88# ### ###',
        '+48 32 ### ## ##',
        '+48 22 ### ## ##',
    )
