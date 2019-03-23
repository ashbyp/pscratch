import timeit
import numpy as np
import concurrent.futures
import multiprocessing

from cards.base import card
from cards.cribbage import score


class TargetScoreSimulation:

    @staticmethod
    def attempts_for_score_v1(deck, target_score, verbose=False):
        if verbose:
            print(f'Looking for score of {target_score}')
        attempts = 1
        while True:
            deck.shuffle()
            h = deck.deal_one(4)
            t = deck.next_card()
            hs = score.score_hand(h, t)
            deck.return_cards(h)
            deck.return_card(t)
            if hs == target_score:
                if verbose:
                    print(f'Found score of {target_score} after {attempts} attempts')
                break
            attempts += 1
        return attempts

    @staticmethod
    def attempts_for_score(deck, target_score, verbose=False):
        if verbose:
            print(f'Looking for score of {target_score}')
        attempts = 1
        while True:
            deck.shuffle()
            h = deck.deal_one(6)
            sh = score.choose_best_hand(h, 4)
            t = deck.next_card()
            hs = score.score_hand(sh[0][1], t)
            deck.return_cards(h)
            deck.return_card(t)
            if hs == target_score:
                if verbose:
                    print(f'Found score of {target_score} after {attempts} attempts')
                break
            attempts += 1
        return attempts

    def _single_thread(self, target_score, num_attempts):
        deck = card.Deck()
        return [self.attempts_for_score(deck, target_score) for _ in range(num_attempts)]

    def _multi_threaded(self, target_score, num_attempts):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            return list(executor.map(self.attempts_for_score, [card.Deck() for _ in range(num_attempts)], [target_score] * num_attempts))

    def _multi_process(self, target_score, num_attempts):
        with multiprocessing.Pool() as pool:
            return pool.starmap(self.attempts_for_score, [(card.Deck(), target_score)] * num_attempts)

    def run(self, target_score, num_attempts):
        if target_score > 19 or num_attempts > 50:
            fn = self._multi_process
        elif num_attempts > 10:
            fn = self._multi_threaded
        else:
            fn = self._single_thread

        print(f'Run sim: {fn}')

        start_time = timeit.default_timer()
        results = fn(target_score, num_attempts)
        time_taken = timeit.default_timer() - start_time
        print(f'Score {target_score}, Num attempts {num_attempts}, avg = {np.mean(results)}, Time={time_taken}')


if __name__ == '__main__':
    sim = TargetScoreSimulation()
    sim.run(20, 20)









