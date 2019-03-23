from unittest import TestCase

from cards.cribbage.player import DumbComputerPlayer
from cards.cribbage.stats import Collector


class TestStats(TestCase):

    def setUp(self):
        self._p1 = DumbComputerPlayer('p1')
        self._p2 = DumbComputerPlayer('p2')

    def test_constructor(self):
        c = Collector(self._p1, self._p2)
        self.assertEqual((0, 0, 0), c.averages(self._p1))
        self.assertEqual((0, 0, 0), c.averages(self._p2))

    def test_pegging(self):
        c = Collector(self._p1, self._p2)
        c.add_pegging_score(self._p1, 4)
        c.add_pegging_score(self._p1, 6)
        c.add_pegging_score(self._p1, 8)
        self.assertEqual((6, 0, 0), c.averages(self._p1))
        c.add_pegging_score(self._p2, 1)
        c.add_pegging_score(self._p2, 2)
        c.add_pegging_score(self._p2, 3)
        self.assertEqual((2, 0, 0), c.averages(self._p2))

    def test_hand(self):
        c = Collector(self._p1, self._p2)
        c.add_hand_score(self._p1, 4)
        c.add_hand_score(self._p1, 6)
        c.add_hand_score(self._p1, 8)
        self.assertEqual((0, 6, 0), c.averages(self._p1))
        c.add_hand_score(self._p2, 1)
        c.add_hand_score(self._p2, 2)
        c.add_hand_score(self._p2, 3)
        self.assertEqual((0, 2, 0), c.averages(self._p2))

    def test_box(self):
        c = Collector(self._p1, self._p2)
        c.add_box_score(self._p1, 4)
        c.add_box_score(self._p1, 6)
        c.add_box_score(self._p1, 8)
        self.assertEqual((0, 0, 6), c.averages(self._p1))
        c.add_box_score(self._p2, 1)
        c.add_box_score(self._p2, 2)
        c.add_box_score(self._p2, 3)
        self.assertEqual((0, 0, 2), c.averages(self._p2))


