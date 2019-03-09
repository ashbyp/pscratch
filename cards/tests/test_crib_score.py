from unittest import TestCase
from cards import crib_score
from cards.card import Card


class TestCrib(TestCase):

    def test_runs(self):
        self.assertEqual(4, crib_score.score_hand(Card.from_str_list('2d,3d,4d'), Card.from_str('5D')))
        self.assertEqual(8, crib_score.score_hand(Card.from_str_list('2d,3d,4d'), Card.from_str('4c')))
        self.assertEqual(17, crib_score.score_hand(Card.from_str_list('2d,3d,4d,4c'), Card.from_str('4s')))

    def test_pairs(self):
        self.assertEqual(4, crib_score.score_hand(Card.from_str_list('JS, JD, 6C, 2H'), Card.from_str('2C')))
        self.assertEqual(2, crib_score.score_hand(Card.from_str_list('QS, JD, 6C, 2H'), Card.from_str('2C')))
        self.assertEqual(2, crib_score.score_hand(Card.from_str_list('JS, QD, 3C, 3H'), Card.from_str('4C')))
        self.assertEqual(4, crib_score.score_hand(Card.from_str_list('JS, JD, 3C, 3H'), Card.from_str('AC')))

    def test_pairs_no_turn(self):
        self.assertEqual(2, crib_score.score_hand(Card.from_str_list('JS, JD, 6C, 2H'), None))
        self.assertEqual(0, crib_score.score_hand(Card.from_str_list('QS, JD, 6C, 2H'), None))

    def test_three_of_a_kind(self):
        self.assertEqual(6, crib_score.score_hand(Card.from_str_list('JC, JD, JH, 2H'), Card.from_str('6S')))
        self.assertEqual(6, crib_score.score_hand(Card.from_str_list('3c, 3d, 3s, qh'), Card.from_str('kh')))
        self.assertEqual(8, crib_score.score_hand(Card.from_str_list('JC, JD, JH, 2H'), Card.from_str('2S')))

    def test_four_of_a_kind(self):
        self.assertEqual(12, crib_score.score_hand(Card.from_str_list('QC, QD, QH, QS'), Card.from_str('6S')))

    def test_fifteens(self):
        self.assertEqual(6, crib_score.score_hand(Card.from_str_list('10C, QD, KH, 2H'), Card.from_str('3S')))
        self.assertEqual(2, crib_score.score_hand(Card.from_str_list('JC, 5D, 4H, 9S'), Card.from_str('7S')))
        self.assertEqual(4, crib_score.score_hand(Card.from_str_list('JC, QD, 4H, 3S'), Card.from_str('AS')))

    def test_flush(self):
        self.assertEqual(5, crib_score.score_hand(Card.from_str_list('ac, 2c, 9c, 7c'), Card.from_str('Jc')))
        self.assertEqual(4, crib_score.score_hand(Card.from_str_list('ac, 2c, 9c, 7c'), Card.from_str('Jh')))
        self.assertEqual(0, crib_score.score_hand(Card.from_str_list('ad, 2c, 9c, 7c'), Card.from_str('Jc')))

    def test_flush_no_turn(self):
        self.assertEqual(4, crib_score.score_hand(Card.from_str_list('ac, 2c, 9c, 7c'), None))

    def test_nob(self):
        self.assertEqual(1, crib_score.score_hand(Card.from_str_list('Jc, 2c, Qc, 6h'), Card.from_str('4c')))
        self.assertEqual(0, crib_score.score_hand(Card.from_str_list('Jc, 2c, Qc, 6h'), Card.from_str('4s')))

    def test_score_hand_with_breakdown(self):
        score, bd = crib_score.score_hand_with_breakdown(Card.from_str_list('JS, JD, 6C, 2H'), Card.from_str('2C'))
        self.assertEqual(4, score)
        self.assertEqual(2, len(bd['pairs']))

    def test_complex_hands(self):
        score, bd = crib_score.score_hand_with_breakdown(Card.from_str_list('2d, 3d, 4d, 5d'), Card.from_str('5s'))
        self.assertEqual(1, len(bd['pairs']))
        self.assertEqual(2, len(bd['runs']))
        self.assertEqual(1, len(bd['flushes']))
        self.assertEqual(1, len(bd['fifteens']))
        self.assertEqual(16, score)

        score, bd = crib_score.score_hand_with_breakdown(Card.from_str_list('jc, qc, kc, jd'), Card.from_str('js'))
        self.assertEqual(3, len(bd['pairs']))
        self.assertEqual(3, len(bd['runs']))
        self.assertEqual(15, score)

        self.assertEqual(29, crib_score.score_hand(Card.from_str_list('jc,5d,5h,5s'), Card.from_str('5c')))

    def test_choose_best_hand_multiple_matches(self):
        best = crib_score.choose_best_hand(Card.from_str_list('ac,2c,9c,7c,3s,kd'), 4)
        self.assertEqual(2, len(best))
        self.assertEqual(5, best[0][0])
        self.assertTrue(set(Card.from_str_list('AC,2C,9C,3S')) in [set(x[1]) for x in best])
        self.assertTrue(set(Card.from_str_list('AC, 2C, 3S, KD')) in [set(x[1]) for x in best])

    def test_choose_best_hand_single_match(self):
        best = crib_score.choose_best_hand(Card.from_str_list('2d, 3d, 4d, 5d, 9c, 9s'), 4)
        self.assertEqual(1, len(best))
        self.assertEqual(8, best[0][0])
        self.assertTrue(set(Card.from_str_list('2d, 3d, 4d, 5d')) in [set(x[1]) for x in best])

