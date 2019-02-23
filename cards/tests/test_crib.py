from unittest import TestCase
from cards import crib
from cards.card import Card


class TestAllUtils(TestCase):

    def test_pairs(self):
        hand = [Card('Spade', 11),
                Card('Diamond', 11),
                Card('Club', 6),
                Card('Heart', 2)]
        self.assertEqual(crib.score_hand(hand, Card('Club', 2)), 4)


