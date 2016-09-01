from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.utils import text
from .. import string_types

class el_GR_FactoryTestCase(unittest.TestCase):
    def setUp(self):
      self.factory = Factory.create('el_GR')

    def test_postcode(self):
      postcode  = self.factory.postcode()
      assert postcode
      assert isinstance(postcode, string_types)
      self.assertRegexpMatches(postcode, r'\A(\d{3}\s\d{2})|(\d{5})')
