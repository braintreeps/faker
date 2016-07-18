from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.utils import text
from .. import string_types


class fr_FR_FactoryTestCase(unittest.TestCase):
    def setUp(self):
      self.factory = Factory.create('fr_FR')

    def test_postcode(self):
      postcode  = self.factory.postcode()
      assert postcode
      assert isinstance(postcode, string_types)
      self.assertRegexpMatches(postcode, r'\A\d{5}$')
