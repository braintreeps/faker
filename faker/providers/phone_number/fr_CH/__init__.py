from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '41'
    formats = (
        '2# ### ## ##',
        '3# ### ## ##',
        '4# ### ## ##',
        '5# ### ## ##',
        '6# ### ## ##',
        '7# ### ## ##',
        '8# ### ## ##',
        '9# ### ## ##',
        '(0)2# ### ## ##',
        '(0)3# ### ## ##',
        '(0)4# ### ## ##',
        '(0)5# ### ## ##',
        '(0)6# ### ## ##',
        '(0)7# ### ## ##',
        '(0)8# ### ## ##',
        '(0)9# ### ## ##',
        '02# ### ## ##',
        '03# ### ## ##',
        '04# ### ## ##',
        '05# ### ## ##',
        '06# ### ## ##',
        '07# ### ## ##',
        '08# ### ## ##',
        '09# ### ## ##',
        #see: http://www.bakom.admin.ch/themen/telekom/00479/00607/index.html
        '084# ### ###',
        '0878 ### ###',
        '0900 ### ###',
        '0901 ### ###',
        '0906 ### ###',
    )
