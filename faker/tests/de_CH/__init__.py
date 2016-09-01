from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.utils import text
from .. import string_types


class de_CH_FactoryTestCase(unittest.TestCase):
    def setUp(self):
      self.factory = Factory.create('de_CH')

    def test_postcode(self):
      postcode  = self.factory.postcode()
      assert postcode
      assert isinstance(postcode, string_types)
      self.assertRegexpMatches(postcode, r'\A\d{4}$')
