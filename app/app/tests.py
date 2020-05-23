from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_two_numbers(self):
        self.assertEquals(add(4, 19), 23)

    def test_subtract_two_positive_numbers(self):
        self.assertEquals(subtract(30, 50), -20)

    def test_subtract_two_negative_numbers(self):
        self.assertEquals(subtract(-1, -10), -11)
