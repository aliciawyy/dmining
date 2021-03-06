from numpy.testing import TestCase
from parameterized import parameterized

from .. import jewelry


class JewelryTest(TestCase):
    def setUp(self):
        self.jewelry = jewelry.Jewelry()

    @parameterized.expand(
        [([7, 7, 8, 9, 10, 11, 1, 2, 2, 3, 4, 5, 6], 607),
         ([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
           1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
           1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
          18252025766940),
         ([1, 2, 5, 3, 4, 5], 9),
         ([1, 2, 5, 3, 4, 5, 21], 9),
         ([1, 2, 3, 4, 5], 4),
         ([123, 217, 661, 678, 796, 964, 54, 111, 417, 526, 917, 923], 0),
         ]
    )
    def test_how_many(self, values, expected):
        self.assertEqual(self.jewelry.how_many(values), expected)
