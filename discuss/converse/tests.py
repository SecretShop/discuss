from django.test import TestCase


class ExampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_a_math(self):
        """Just an example"""
        self.assertEqual(1 + 1, 2)
