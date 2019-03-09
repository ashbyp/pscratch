from unittest import TestCase
from cards.card import Card


class TestCard(TestCase):

    def setUp(self):
        self.ace_of_diamonds = Card(1, 'Diamond')
        self.ten_of_spades = Card(10, 'Spade')
        self.five_of_clubs = Card(5, 'Club')
        self.jack_of_hearts = Card(11, 'Heart')

    def test_card_constructor_throws_appropriate_exceptions(self):
        with self.assertRaises(ValueError):
            Card('15', 'Spade')
        with self.assertRaises(ValueError):
            Card('xx', 'Spade')
        with self.assertRaises(ValueError):
            Card('10', 'NotExist')

    def test_cards_from_str_list(self):
        cards = Card.from_str_list('AD,1D,10S')
        self.assertEqual(cards[0], self.ace_of_diamonds)
        self.assertEqual(cards[1], self.ace_of_diamonds)
        self.assertEqual(cards[2], self.ten_of_spades)

        Card.from_str_list('AD, 1D, 10S')

        with self.assertRaises(ValueError):
            Card.from_str_list('AD,1x,10S')

    def test_from_str(self):
        self.assertEqual(Card.from_str('AD'), self.ace_of_diamonds)
        self.assertEqual(Card.from_str('1D'), self.ace_of_diamonds)
        self.assertEqual(Card.from_str('ad'), self.ace_of_diamonds)
        self.assertEqual(Card.from_str('1d'), self.ace_of_diamonds)

        self.assertEqual(Card.from_str('10S'), self.ten_of_spades)
        self.assertEqual(Card.from_str('10s'), self.ten_of_spades)

        self.assertEqual(Card.from_str('5C'), self.five_of_clubs)
        self.assertEqual(Card.from_str('5c'), self.five_of_clubs)

        self.assertEqual(Card.from_str('JH'), self.jack_of_hearts)
        self.assertEqual(Card.from_str('Jh'), self.jack_of_hearts)
        self.assertEqual(Card.from_str('11H'), self.jack_of_hearts)
        self.assertEqual(Card.from_str('11h'), self.jack_of_hearts)

    def test_set_equality(self):
        c1 = Card.from_str('JH')
        c2 = Card.from_str('JH')
        self.assertEqual(c1, c2)
        self.assertEqual(set([c1]), set([c2]))


