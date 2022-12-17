from unittest import TestCase

from algorithms.m.abc import getSum
from algorithms.m.allwrong import getWrongAnswers
from algorithms.m.battleships import getHitProbability
from algorithms.m.kaitenzushi import getMaximumEatenDishCount
from algorithms.m.rotarylock import getMinCodeEntryTime
from algorithms.m.uniform import getUniformIntegerCountInInterval


class AllTests(TestCase):

    def test_abc(self):
        self.assertEqual(getSum(1, 2, 3), 6)
        self.assertEqual(getSum(100, 100, 100), 300)
        self.assertEqual(getSum(85, 16, 93), 194)

    def test_allwrong(self):
        self.assertEqual('BAB', getWrongAnswers(3, 'ABA'))
        self.assertEqual('AAAAA', getWrongAnswers(5, 'BBBBB'))

    def test_battleships(self):
        self.assertEqual(0.5, getHitProbability(2, 3, [[0, 0, 1], [1, 0, 1]]))
        self.assertEqual(1.0, getHitProbability(2, 2, [[1, 1], [1, 1]]))

    def test_kaitenzushi(self):
        self.assertEqual(5, getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1))
        self.assertEqual(4, getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2))
        self.assertEqual(2, getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2))

    def test_rotarylock(self):
        self.assertEqual(2, getMinCodeEntryTime(3, 3, [1, 2, 3]))
        self.assertEqual(11, getMinCodeEntryTime(10, 4, [9, 4, 4, 8]))

    def test_uniform(self):
        self.assertEqual(5, getUniformIntegerCountInInterval(75, 300))
        self.assertEqual(9, getUniformIntegerCountInInterval(1, 9))
        self.assertEqual(1, getUniformIntegerCountInInterval(999999999, 999999999))



