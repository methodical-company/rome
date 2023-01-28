import rome_bridge
from unittest import TestCase

class InitTest(TestCase):

    def test_init(self):
        self.assertIsNotNone(rome_bridge.ROME_EXPLORER)
